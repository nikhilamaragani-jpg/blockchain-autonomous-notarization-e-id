"""
Simple notarization record logic (conceptual demo)
"""

from datetime import datetime, timezone
import hmac

from hasher import generate_document_hash


def create_notarization_record(
    document_hash: str, owner: str, document_name: str
) -> dict[str, str]:
    return {
        "document_name": document_name,
        "document_hash": document_hash,
        "owner": owner,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": "notarized_concept_demo",
    }


def is_document_match(record: dict[str, str], original_content: str | bytes) -> bool:
    return is_hash_match(record, generate_document_hash(original_content))


def is_hash_match(record: dict[str, str], current_hash: str) -> bool:
    recorded_hash = record.get("document_hash", "")
    return hmac.compare_digest(current_hash, recorded_hash)


def verify_record(record: dict[str, str], original_content: str | bytes) -> str:
    if is_document_match(record, original_content):
        return "Valid - Document integrity verified (prototype)"
    return "Invalid - Hash mismatch"
