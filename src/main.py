"""
Blockchain-Based Autonomous Notarization System (BANS)
Prototype: hash · record · verify · ledger
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from hasher import generate_document_hash
from notarization import create_notarization_record, verify_record
from database import init_db, save_record, list_records


def banner() -> None:
    print("=" * 60)
    print("  BANS Notarization Prototype  |  B.Tech Mini Project")
    print("  SHA-256 · Ledger record · Integrity verification")
    print("=" * 60)


def main() -> None:
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

    print("\n[3] Verifying original content (expect VALID)...")
    result_ok = verify_record(record, sample_doc)
    print(f"    Result    : {result_ok}")

    print("\n[4] Verifying tampered content (expect INVALID)...")
    tampered = sample_doc + " [unauthorized edit]"
    result_bad = verify_record(record, tampered)
    print(f"    Result    : {result_bad}")

    print("\n[5] Ledger snapshot")
    rows = list_records(limit=5)
    print(f"    Records stored (showing up to 5): {len(rows)}")
    for name, h, own, status, created in rows:
        print(f"    - {name} | {own} | {status} | {created}")
        print(f"      hash={h[:16]}...")

    print("\nDone. Core integrity workflow demonstrated.")
    print("Full scope: eID/PKI, smart contracts, Django UI — see docs/REPORT_SUMMARY.md")


if __name__ == "__main__":
    main()
