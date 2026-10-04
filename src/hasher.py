"""
Document hashing utilities.
"""

import hashlib
from pathlib import Path


def generate_document_hash(content: str | bytes) -> str:
    """
    Generate a SHA-256 hash for text or binary document content.
    """
    if isinstance(content, str):
        content = content.encode("utf-8")
    if not isinstance(content, bytes):
        raise TypeError("Document content must be str or bytes")
    return hashlib.sha256(content).hexdigest()


def generate_file_hash(file_path: str | Path) -> tuple[str, int]:
    """Hash a file in chunks and return its hexadecimal digest and byte size."""
    digest = hashlib.sha256()
    file_size_bytes = 0
    with Path(file_path).open("rb") as document:
        for chunk in iter(lambda: document.read(1024 * 1024), b""):
            digest.update(chunk)
            file_size_bytes += len(chunk)
    return digest.hexdigest(), file_size_bytes
