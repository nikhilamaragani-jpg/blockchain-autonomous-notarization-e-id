"""
Blockchain-Based Autonomous Notarization System (BANS)
Prototype: hash · record · verify · ledger
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from hasher import hash_content
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

    print("\n[1] Creating notarization record...")
    record = create_notarization_record(owner=owner, content=sample_doc)
    save_record(record)
    print(f"    Owner     : {record.get('owner', owner)}")
    print(f"    SHA-256   : {record.get('hash', record.get('content_hash', 'n/a'))}")
    print(f"    Timestamp : {record.get('timestamp', record.get('created_at', 'n/a'))}")

    print("\n[2] Verifying original content (expect MATCH)...")
    ok = verify_record(record, sample_doc)
    print(f"    Result    : {'MATCH — integrity confirmed' if ok else 'MISMATCH'}")

    print("\n[3] Verifying tampered content (expect MISMATCH)...")
    tampered = sample_doc + " [unauthorized edit]"
    ok2 = verify_record(record, tampered)
    print(f"    Result    : {'MATCH' if ok2 else 'MISMATCH — tampering detected'}")

    print("\n[4] Ledger snapshot")
    try:
        rows = list_records()
        print(f"    Records stored: {len(rows)}")
    except Exception:
        print("    (ledger list helper unavailable — record save still executed)")

    print("\nDone. Core integrity workflow demonstrated.")
    print("Full scope: eID/PKI, smart contracts, Django UI — see docs/REPORT_SUMMARY.md")


if __name__ == "__main__":
    main()
