# Demo

## Interactive integrity demonstration

```bash
python -m pip install -r requirements.txt
python src/main.py
```

The no-argument demo hashes a sample agreement, saves a record, verifies the original, and detects a changed version. It adds a demonstration record to the default local database each time it is run.

## File and analytics workflow

```bash
python src/main.py notarize path/to/agreement.pdf --owner demo-alias
# Use the ID printed above:
python src/main.py verify 1 path/to/agreement.pdf
python src/main.py analytics
python src/main.py analytics --format json
python src/main.py export-csv ledger.csv
```

Change a copy of the file and verify it again to demonstrate a mismatch. A mismatch is a useful verification result and is recorded in the analytics, but the CLI returns exit code `1` so scripts can detect it.

The database contains document fingerprints and metadata, not document contents. The SQLite file is mutable and does not provide blockchain consensus, national eID authentication, legal notarization, or trusted timestamping.
