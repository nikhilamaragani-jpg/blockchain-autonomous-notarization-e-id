"""
Blockchain-inspired notarization prototype and analytics CLI.
"""

import argparse
import csv
import json
import os
import sqlite3
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database import (
    get_ledger_analytics,
    get_record,
    init_db,
    list_records,
    list_records_with_ids,
    record_verification,
    save_record,
)
from hasher import generate_document_hash, generate_file_hash
from notarization import (
    create_notarization_record,
    is_hash_match,
)


def banner() -> None:
    print("=" * 60)
    print("  Notarization + eID Concepts  |  Integrity & Analytics Demo")
    print("  SHA-256 · SQLite audit ledger · Verification metrics")
    print("=" * 60)


def run_demo() -> None:
    banner()
    init_db()

    sample_doc = (
        "Sample agreement: Party A and Party B agree to the terms "
        "dated 2025-05-01 for digital service delivery."
    )
    owner = "A. Nikhil Sai (demo eID: DEMO-22X31A0513)"
    document_name = "service_agreement_demo.txt"

    print("\n[1] Hashing document content (SHA-256)...")
    doc_hash = generate_document_hash(sample_doc)
    print(f"    SHA-256   : {doc_hash}")

    print("\n[2] Creating notarization record...")
    record = create_notarization_record(
        document_hash=doc_hash,
        owner=owner,
        document_name=document_name,
    )
    save_record(
        document_name=record["document_name"],
        document_hash=record["document_hash"],
        owner=record["owner"],
        status=record["status"],
    )
    print(f"    Owner     : {record['owner']}")
    print(f"    Document  : {record['document_name']}")
    print(f"    Timestamp : {record['timestamp']}")
    print(f"    Status    : {record['status']}")

    print("\n[3] Verifying original content...")
    result_ok = verify_record(record, sample_doc)
    print(f"    Result    : {result_ok}")

    print("\n[4] Verifying tampered content...")
    tampered = sample_doc + " [unauthorized edit]"
    result_bad = verify_record(record, tampered)
    print(f"    Result    : {result_bad}")

    print("\n[5] Ledger snapshot")
    rows = list_records(limit=5)
    print(f"    Records stored (showing up to 5): {len(rows)}")
    for name, h, own, status, created in rows:
        print(f"    - {name} | {own} | {status} | {created}")
        print(f"      hash={h[:16]}...")

    print("\nDone. Integrity core demonstrated (portfolio scope).")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Hash documents, record integrity metadata, verify files, "
            "and analyze the local SQLite ledger."
        )
    )
    commands = parser.add_subparsers(dest="command", required=True)

    notarize = commands.add_parser("notarize", help="Create a record for a file")
    notarize.add_argument("file", help="Path to the document (content is not stored)")
    notarize.add_argument("--owner", required=True, help="Demo owner label or pseudonym")
    notarize.add_argument(
        "--name", help="Display name stored in the ledger (defaults to the file name)"
    )

    verify = commands.add_parser("verify", help="Verify a file against a ledger record")
    verify.add_argument("record_id", type=int, help="ID printed by the notarize command")
    verify.add_argument("file", help="Path to the file to verify")

    list_command = commands.add_parser("list", help="List recent ledger records")
    list_command.add_argument("--limit", type=int, default=10)

    analytics = commands.add_parser("analytics", help="Summarize ledger activity")
    analytics.add_argument(
        "--format", choices=("text", "json"), default="text", dest="output_format"
    )

    export = commands.add_parser("export-csv", help="Export ledger metadata to CSV")
    export.add_argument("file", help="Destination CSV path")
    return parser


def _run_command(args: argparse.Namespace) -> int:
    init_db()

    if args.command == "notarize":
        file_path = os.path.abspath(args.file)
        document_hash, file_size_bytes = generate_file_hash(file_path)
        record = create_notarization_record(
            document_hash=document_hash,
            owner=args.owner,
            document_name=args.name or os.path.basename(file_path),
        )
        record_id = save_record(
            document_name=record["document_name"],
            document_hash=record["document_hash"],
            owner=record["owner"],
            status=record["status"],
            file_size_bytes=file_size_bytes,
            created_at=record["timestamp"],
        )
        print(f"Record ID: {record_id}")
        print(f"Document: {record['document_name']}")
        print(f"SHA-256: {document_hash}")
        print(f"Size: {file_size_bytes} bytes")
        print(f"Created: {record['timestamp']}")
        print("Document content was not stored.")
        return 0

    if args.command == "verify":
        record = get_record(args.record_id)
        if record is None:
            print(f"No ledger record found with ID {args.record_id}.", file=sys.stderr)
            return 1
        document_hash, _ = generate_file_hash(args.file)
        matched = is_hash_match(record, document_hash)
        record_verification(args.record_id, matched)
        if matched:
            print("Valid - Document integrity verified (prototype)")
        else:
            print("Invalid - Hash mismatch")
        print(f"Record ID: {args.record_id}")
        return 0 if matched else 1

    if args.command == "list":
        for record in list_records_with_ids(args.limit):
            record_id, name, digest, owner, status, created_at, size = record
            print(
                f"#{record_id} | {name} | {owner} | {status} | "
                f"{created_at} | {size} bytes | sha256:{digest[:16]}..."
            )
        return 0

    if args.command == "analytics":
        metrics = get_ledger_analytics()
        if args.output_format == "json":
            print(json.dumps(metrics, indent=2))
        else:
            print("Ledger analytics (local SQLite prototype)")
            for key, value in metrics.items():
                if key != "daily_activity":
                    label = key.replace("_", " ").title()
                    display = "N/A" if value is None else value
                    print(f"{label}: {display}")
            print("Daily activity:")
            if metrics["daily_activity"]:
                for row in metrics["daily_activity"]:
                    print(f"  {row['date']}: {row['notarizations']} notarizations")
            else:
                print("  No notarizations recorded.")
        return 0

    if args.command == "export-csv":
        records = list_records_with_ids(limit=2**31 - 1)
        fields = (
            "record_id",
            "document_name",
            "document_hash",
            "owner",
            "status",
            "created_at",
            "file_size_bytes",
        )
        with open(args.file, "w", newline="", encoding="utf-8") as output:
            writer = csv.writer(output)
            writer.writerow(fields)
            writer.writerows(records)
        print(f"Exported {len(records)} records to {os.path.abspath(args.file)}")
        return 0

    raise ValueError(f"Unsupported command: {args.command}")


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        run_demo()
        return 0
    args = build_parser().parse_args(argv)
    try:
        return _run_command(args)
    except (OSError, sqlite3.Error, ValueError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
