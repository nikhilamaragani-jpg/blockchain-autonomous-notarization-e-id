from pathlib import Path
import sys

import pytest

streamlit_testing = pytest.importorskip("streamlit.testing.v1")
AppTest = streamlit_testing.AppTest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import database
from hasher import generate_document_hash

DASHBOARD_PATH = Path(__file__).resolve().parents[1] / "dashboard" / "app.py"


def test_dashboard_handles_empty_ledger(tmp_path, monkeypatch):
    monkeypatch.setattr(database, "DB_PATH", str(tmp_path / "empty.db"))

    app = AppTest.from_file(str(DASHBOARD_PATH)).run(timeout=30)

    assert not app.exception
    assert any("No notarizations yet" in message.value for message in app.info)


def test_dashboard_shows_metrics_without_document_identity(tmp_path, monkeypatch):
    monkeypatch.setattr(database, "DB_PATH", str(tmp_path / "ledger.db"))
    database.init_db()
    record_id = database.save_record(
        "private-contract.pdf",
        generate_document_hash("confidential sample"),
        "private-owner",
        "notarized_concept_demo",
        file_size_bytes=20,
        created_at="2026-10-01T12:00:00+00:00",
    )
    database.record_verification(record_id, matched=True)
    database.record_verification(record_id, matched=False)

    app = AppTest.from_file(str(DASHBOARD_PATH)).run(timeout=30)

    assert not app.exception
    assert {metric.label for metric in app.metric} >= {
        "Notarizations",
        "Unique fingerprints",
        "Repeat notarizations",
        "Verification attempts",
        "Matches",
        "Mismatches",
    }
    table_data = app.dataframe[0].value
    assert "private-contract.pdf" not in str(table_data)
    assert "private-owner" not in str(table_data)
