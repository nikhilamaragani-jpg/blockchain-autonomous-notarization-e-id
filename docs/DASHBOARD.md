# Optional analytics dashboard

The Streamlit dashboard visualizes real records in the local SQLite ledger. It does not generate sample data or contact an external service. The core CLI and test suite remain usable without Streamlit.

## Install and run

Install the optional dashboard dependency:

```bash
python -m pip install -r requirements-dashboard.txt
```

Start it from the repository root:

```bash
python -m streamlit run dashboard/app.py
```

The app uses `data/notarization_ledger.db` by default, matching the CLI. To select a different ledger, set `NOTARIZATION_DB_PATH` before starting Streamlit.

PowerShell:

```powershell
$env:NOTARIZATION_DB_PATH = "data\portfolio-demo.db"
python -m streamlit run dashboard/app.py
```

macOS/Linux:

```bash
NOTARIZATION_DB_PATH=data/portfolio-demo.db python -m streamlit run dashboard/app.py
```

To populate a ledger with your own non-sensitive demo files, run the CLI with the same `NOTARIZATION_DB_PATH`:

```bash
python src/main.py notarize path/to/demo-document.txt --owner portfolio-demo
python src/main.py verify 1 path/to/demo-document.txt
```

The dashboard shows notarization counts, unique fingerprints, repeat records, average file size, verification outcomes, match rate, daily activity, and the latest 20 ledger entries. The record table deliberately excludes document names and owner labels. Select **Refresh ledger** after making changes from the CLI.

## Interpretation and data quality

Metrics describe only the selected local database. Repeat notarizations are counts of records with the same hash, not necessarily redundant or suspicious behavior. Match rates reflect only verification attempts made through this prototype. Older ledger rows migrated from the original schema have an unknown file size represented as zero; interpret their average size accordingly. No metrics are presented when the ledger has no records.

This dashboard is not an immutable audit system. Anyone with write access to the SQLite file can alter the ledger and its verification events. Protect the database and any exports; a file hash can still reveal information about a known document.
