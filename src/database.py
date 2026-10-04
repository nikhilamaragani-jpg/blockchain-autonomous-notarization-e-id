"""
SQLite ledger and privacy-preserving verification analytics (prototype).
"""

import os
import sqlite3
from contextlib import closing
from datetime import datetime, timezone

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DB_PATH = os.environ.get(
    "NOTARIZATION_DB_PATH",
    os.path.join(BASE_DIR, "data", "notarization_ledger.db"),
)


def _connect() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH, timeout=30)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    parent = os.path.dirname(DB_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with closing(_connect()) as conn:
        with conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS ledger (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    document_name TEXT NOT NULL,
                    document_hash TEXT NOT NULL,
                    owner TEXT NOT NULL,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    file_size_bytes INTEGER NOT NULL DEFAULT 0
                        CHECK (file_size_bytes >= 0)
                )
                """
            )
            columns = {
                row[1] for row in conn.execute("PRAGMA table_info(ledger)")
            }
            if "file_size_bytes" not in columns:
                conn.execute(
                    "ALTER TABLE ledger ADD COLUMN file_size_bytes "
                    "INTEGER NOT NULL DEFAULT 0 CHECK (file_size_bytes >= 0)"
                )
            conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_ledger_hash ON ledger(document_hash)"
            )
            conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_ledger_created_at "
                "ON ledger(created_at)"
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS verification_events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    record_id INTEGER NOT NULL REFERENCES ledger(id),
                    verified_at TEXT NOT NULL,
                    matched INTEGER NOT NULL CHECK (matched IN (0, 1))
                )
                """
            )
            conn.execute(
                "CREATE INDEX IF NOT EXISTS idx_verification_record "
                "ON verification_events(record_id)"
            )


def save_record(
    document_name: str,
    document_hash: str,
    owner: str,
    status: str,
    file_size_bytes: int = 0,
    created_at: str | None = None,
) -> int:
    if not document_name.strip() or not owner.strip() or not status.strip():
        raise ValueError("document_name, owner, and status must not be blank")
    if len(document_hash) != 64 or any(
        character not in "0123456789abcdefABCDEF" for character in document_hash
    ):
        raise ValueError("document_hash must be a 64-character SHA-256 hex digest")
    if file_size_bytes < 0:
        raise ValueError("file_size_bytes cannot be negative")
    with closing(_connect()) as conn:
        with conn:
            cursor = conn.execute(
                """
                INSERT INTO ledger
                    (document_name, document_hash, owner, status, created_at,
                     file_size_bytes)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    document_name,
                    document_hash,
                    owner,
                    status,
                    created_at or datetime.now(timezone.utc).isoformat(),
                    file_size_bytes,
                ),
            )
            return cursor.lastrowid


def list_records(limit: int = 5):
    _validate_limit(limit)
    with closing(_connect()) as conn:
        return conn.execute(
            """
            SELECT document_name, document_hash, owner, status, created_at
            FROM ledger ORDER BY id DESC LIMIT ?
            """,
            (limit,),
        ).fetchall()


def list_records_with_ids(limit: int = 10):
    _validate_limit(limit)
    with closing(_connect()) as conn:
        return conn.execute(
            """
            SELECT id, document_name, document_hash, owner, status, created_at,
                   file_size_bytes
            FROM ledger ORDER BY id DESC LIMIT ?
            """,
            (limit,),
        ).fetchall()


def get_record(record_id: int) -> dict | None:
    with closing(_connect()) as conn:
        conn.row_factory = sqlite3.Row
        row = conn.execute(
            "SELECT * FROM ledger WHERE id = ?", (record_id,)
        ).fetchone()
        return dict(row) if row else None


def record_verification(record_id: int, matched: bool) -> None:
    with closing(_connect()) as conn:
        with conn:
            conn.execute(
                """
                INSERT INTO verification_events (record_id, verified_at, matched)
                VALUES (?, ?, ?)
                """,
                (
                    record_id,
                    datetime.now(timezone.utc).isoformat(),
                    int(matched),
                ),
            )


def get_ledger_analytics() -> dict:
    with closing(_connect()) as conn:
        conn.row_factory = sqlite3.Row
        ledger = conn.execute(
            """
            SELECT COUNT(*) AS total_notarizations,
                   COUNT(DISTINCT document_hash) AS unique_documents,
                   COALESCE(AVG(file_size_bytes), 0) AS average_file_size_bytes
            FROM ledger
            """
        ).fetchone()
        verifications = conn.execute(
            """
            SELECT COUNT(*) AS total_verifications,
                   COALESCE(SUM(matched), 0) AS matches,
                   COUNT(*) - COALESCE(SUM(matched), 0) AS mismatches
            FROM verification_events
            """
        ).fetchone()
        daily_activity = conn.execute(
            """
            SELECT date(created_at) AS date, COUNT(*) AS notarizations
            FROM ledger
            GROUP BY date(created_at)
            ORDER BY date
            """
        ).fetchall()

    total_verifications = verifications["total_verifications"]
    matches = verifications["matches"]
    return {
        "total_notarizations": ledger["total_notarizations"],
        "unique_documents": ledger["unique_documents"],
        "duplicate_notarizations": (
            ledger["total_notarizations"] - ledger["unique_documents"]
        ),
        "average_file_size_bytes": round(ledger["average_file_size_bytes"], 2),
        "total_verifications": total_verifications,
        "matches": matches,
        "mismatches": verifications["mismatches"],
        "match_rate_percent": (
            round(matches * 100 / total_verifications, 2)
            if total_verifications
            else None
        ),
        "daily_activity": [dict(row) for row in daily_activity],
    }


def _validate_limit(limit: int) -> None:
    if limit < 1:
        raise ValueError("limit must be at least 1")
