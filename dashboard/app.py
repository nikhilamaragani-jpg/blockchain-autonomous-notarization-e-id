"""Optional Streamlit dashboard for the local notarization ledger."""

import os
import sys
from pathlib import Path

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from database import get_ledger_analytics, init_db, list_records_with_ids

st.set_page_config(
    page_title="Notarization Ledger | Analytics",
    page_icon="🔏",
    layout="wide",
)

st.title("Notarization Ledger")
st.caption("Local document-integrity activity | Educational prototype")

database_path = os.environ.get(
    "NOTARIZATION_DB_PATH",
    str(PROJECT_ROOT / "data" / "notarization_ledger.db"),
)
st.caption(f"Data source: local SQLite ledger (`{Path(database_path).name}`)")

init_db()
analytics = get_ledger_analytics()

if st.button("Refresh ledger"):
    st.rerun()

if analytics["total_notarizations"] == 0:
    st.info(
        "No notarizations yet. Use the CLI to record a document, then refresh "
        "this page to explore your ledger."
    )
else:
    metric_columns = st.columns(4)
    metric_columns[0].metric("Notarizations", analytics["total_notarizations"])
    metric_columns[1].metric("Unique fingerprints", analytics["unique_documents"])
    metric_columns[2].metric(
        "Repeat notarizations", analytics["duplicate_notarizations"]
    )
    metric_columns[3].metric(
        "Average file size",
        f"{analytics['average_file_size_bytes']:,.0f} bytes",
    )

    verification_row = st.columns(3)
    verification_row[0].metric(
        "Verification attempts", analytics["total_verifications"]
    )
    verification_row[1].metric("Matches", analytics["matches"])
    verification_row[2].metric("Mismatches", analytics["mismatches"])
    match_rate = analytics["match_rate_percent"]
    st.caption(
        "Verification match rate: "
        + (f"{match_rate:.1f}%" if match_rate is not None else "N/A")
    )

    activity_column, outcome_column = st.columns(2)
    with activity_column:
        st.subheader("Notarizations over time")
        activity = analytics["daily_activity"]
        if activity:
            st.line_chart(
                {
                    "date": [row["date"] for row in activity],
                    "notarizations": [
                        row["notarizations"] for row in activity
                    ],
                },
                x="date",
                y="notarizations",
                x_label="UTC date",
                y_label="Records",
            )
        else:
            st.info("No daily activity is available.")

    with outcome_column:
        st.subheader("Verification outcomes")
        if analytics["total_verifications"]:
            st.bar_chart(
                {
                    "outcome": ["Matches", "Mismatches"],
                    "attempts": [
                        analytics["matches"],
                        analytics["mismatches"],
                    ],
                },
                x="outcome",
                y="attempts",
                x_label="Outcome",
                y_label="Attempts",
            )
        else:
            st.info("No verification attempts have been recorded.")

    st.subheader("Recent ledger records")
    records = list_records_with_ids(limit=20)
    st.dataframe(
        {
            "Record ID": [row[0] for row in records],
            "Status": [row[4] for row in records],
            "Created (UTC)": [row[5] for row in records],
            "File size (bytes)": [row[6] for row in records],
            "SHA-256 fingerprint (prefix)": [
                f"{row[2][:16]}..." for row in records
            ],
        },
        hide_index=True,
        width="stretch",
    )

st.divider()
st.caption(
    "This dashboard reports descriptive metrics from one local SQLite database. "
    "It hides file names and owner labels, but hashes and exported metadata may "
    "still be sensitive. A local SQLite ledger is mutable and is not a "
    "blockchain, legal notarization service, or national eID integration."
)
