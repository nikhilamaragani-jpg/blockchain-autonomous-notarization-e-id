"""
Simple notarization record logic (conceptual demo)
"""

from datetime import datetime
from hasher import generate_document_hash


def create_notarization_record(document_hash: str, owner: str, document_name: str) -> dict:
    """
    Creates a simple notarization-style record.
    In a real system this would interact with a blockchain.
    """
    return {
        "document_name": document_name,
        "document_hash": document_hash,
        "owner": owner,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "status": "notarized_concept_demo"
    }


def verify_record(record: dict, original_content: str) -> str:
    """
    Verifies whether the stored hash matches the original content.
    """
    current_hash = generate_document_hash(original_content)
    if current_hash == record.get("document_hash"):
        return "Valid - Document integrity verified (prototype)"
    return "Invalid - Hash mismatch"
