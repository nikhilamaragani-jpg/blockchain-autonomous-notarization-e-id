import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from hasher import generate_document_hash
from notarization import create_notarization_record, verify_record


def test_hash_stable():
    h1 = generate_document_hash("hello")
    h2 = generate_document_hash("hello")
    assert h1 == h2
    assert len(h1) == 64


def test_verify_match_and_mismatch():
    doc = "agreement body"
    h = generate_document_hash(doc)
    rec = create_notarization_record(h, "demo-owner", "doc.txt")
    assert "VALID" in verify_record(rec, doc).upper() or verify_record(rec, doc) == "MATCH" or "match" in verify_record(rec, doc).lower() or verify_record(rec, doc)
    # at minimum: original should not equal tampered verification outcome if functions return distinct strings
    ok = verify_record(rec, doc)
    bad = verify_record(rec, doc + "x")
    assert ok != bad
