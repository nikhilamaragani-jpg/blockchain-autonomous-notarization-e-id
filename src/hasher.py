"""
Document hashing utility
"""

import hashlib


def generate_document_hash(content: str) -> str:
    """
    Generates a SHA-256 hash for the given document content.
    """
    return hashlib.sha256(content.encode("utf-8")).hexdigest()
