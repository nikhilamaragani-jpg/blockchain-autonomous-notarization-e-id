import csv
import hashlib
import sqlite3
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import database
from hasher import generate_document_hash, generate_file_hash
from main import main
from notarization import (
    create_notarization_record,
    is_document_match,
    verify_record,
)


def test_hash_stable_for_text_and_bytes():
    assert generate_document_hash("hello") == hashlib.sha256(b"hello").hexdigest()
    assert generate_document_hash(b"\x00\xff") == hashlib.sha256(b"\x00\xff").hexdigest()


def test_hash_rejects_unsupported_content():
    with pytest.raises(TypeError, match="str or bytes"):
        generate_document_hash(123)  # type: ignore[arg-type]


def test_file_hash_streams_binary_content(tmp_path):
    content = bytes(range(256)) * 8192
    file_path = tmp_path / "document.bin"
    file_path.write_bytes(content)

    digest, size = generate_file_hash(file_path)

    assert digest == hashlib.sha256(content).hexdigest()
    assert size == len(content)


def test_verify_match_and_mismatch():
    doc = "agreement body"
    record = create_notarization_record(
        generate_document_hash(doc), "demo-owner", "doc.txt"
    )

    assert is_document_match(record, doc)
    assert not is_document_match(record, doc + "x")
    assert verify_record(record, doc).startswith("Valid")
    assert verify_record(record, doc + "x").startswith("Invalid")


def test_database_migrates_legacy_ledger(tmp_path, monkeypatch):
    db_path = tmp_path / "legacy.db"
    monkeypatch.setattr(database, "DB_PATH", str(db_path))
    with sqlite3.connect(db_path) as connection:
        connection.execute(
            """
            CREATE TABLE ledger (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                document_name TEXT NOT NULL,
                document_hash TEXT NOT NULL,
                owner TEXT NOT NULL,
                status TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        connection.execute(
            """
            INSERT INTO ledger
                (document_name, document_hash, owner, status, created_at)
            VALUES ('legacy.txt', ?, 'alias', 'notarized', '2025-01-01T00:00:00+00:00')
            """,
            (generate_document_hash("legacy"),),
        )

    database.init_db()

    record = database.list_records_with_ids()[0]
    assert record[1] == "legacy.txt"
    assert record[-1] == 0
    assert database.get_ledger_analytics()["total_notarizations"] == 1


def test_database_rejects_invalid_record_metadata(tmp_path, monkeypatch):
    monkeypatch.setattr(database, "DB_PATH", str(tmp_path / "ledger.db"))
    database.init_db()

    with pytest.raises(ValueError, match="SHA-256"):
        database.save_record("doc.txt", "not-a-hash", "alias", "notarized")
    with pytest.raises(ValueError, match="must not be blank"):
        database.save_record("doc.txt", generate_document_hash("doc"), " ", "notarized")


def test_cli_notarize_verify_analytics_and_csv(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(database, "DB_PATH", str(tmp_path / "ledger.db"))
    document = tmp_path / "contract.txt"
    document.write_text("signed agreement", encoding="utf-8")

    assert main(["notarize", str(document), "--owner", "analyst-alias"]) == 0
    notarize_output = capsys.readouterr().out
    assert "Record ID: 1" in notarize_output
    assert "content was not stored" in notarize_output

    assert main(["verify", "1", str(document)]) == 0
    assert "integrity verified" in capsys.readouterr().out

    document.write_text("tampered agreement", encoding="utf-8")
    assert main(["verify", "1", str(document)]) == 1
    assert "Hash mismatch" in capsys.readouterr().out

    assert main(["analytics", "--format", "json"]) == 0
    analytics = capsys.readouterr().out
    assert '"total_verifications": 2' in analytics
    assert '"matches": 1' in analytics
    assert '"mismatches": 1' in analytics

    export_path = tmp_path / "ledger.csv"
    assert main(["export-csv", str(export_path)]) == 0
    with export_path.open(newline="", encoding="utf-8") as exported:
        rows = list(csv.DictReader(exported))
    assert len(rows) == 1
    assert rows[0]["document_name"] == "contract.txt"
    assert rows[0]["file_size_bytes"] == str(len("signed agreement"))


def test_cli_reports_missing_record(tmp_path, monkeypatch, capsys):
    monkeypatch.setattr(database, "DB_PATH", str(tmp_path / "ledger.db"))
    document = tmp_path / "contract.txt"
    document.write_text("content", encoding="utf-8")

    assert main(["verify", "42", str(document)]) == 1
    assert "No ledger record found" in capsys.readouterr().err
