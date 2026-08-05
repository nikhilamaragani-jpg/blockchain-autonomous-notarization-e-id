"""
Blockchain-Based Autonomous Notarization (Concept Demo)
Hashing + verification + SQLite ledger
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from hasher import generate_document_hash
from notarization import create_notarization_record, verify_record
from database import init_db, save_record, list_records


def main():
    print("=" * 55)
    print("Blockchain Notarization Concept - Prototype")
    print("=" * 55)

    init_db()

    document_content = "Sample academic document for notarization demo."
    doc_hash = generate_document_hash(document_content)

    record = create_notarization_record(
        document_hash=doc_hash,
        owner="Amaragani Nikhil Sai",
        document_name="Sample_Document.pdf",
    )

    save_record(
        document_name=record["document_name"],
        document_hash=record["document_hash"],
        owner=record["owner"],
        status=record["status"],
    )

    print("\nNotarization Record Created:")
    for key, value in record.items():
        print(f"  {key}: {value}")

    print("\nVerification:", verify_record(record, document_content))

    print("\n--- Recent Ledger Records ---")
    for row in list_records(3):
        print(row)


if __name__ == "__main__":
    main()
