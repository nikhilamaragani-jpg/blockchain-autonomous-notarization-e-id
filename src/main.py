"""
Blockchain-Based Autonomous Notarization (Concept Demo)
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from hasher import generate_document_hash
from notarization import create_notarization_record, verify_record


def main():
    print("=" * 50)
    print("Blockchain Notarization Concept - Prototype")
    print("=" * 50)

    document_content = "Sample academic document for notarization demo."
    doc_hash = generate_document_hash(document_content)

    record = create_notarization_record(
        document_hash=doc_hash,
        owner="Amaragani Nikhil Sai",
        document_name="Sample_Document.pdf"
    )

    print("\nNotarization Record Created:")
    for key, value in record.items():
        print(f"  {key}: {value}")

    print("\nVerification:", verify_record(record, document_content))


if __name__ == "__main__":
    main()
