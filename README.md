<div align="center">

# Blockchain-Based Autonomous Notarization using National eID

### An analytics-ready document integrity prototype

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![CI](https://github.com/nikhilamaragani-jpg/blockchain-autonomous-notarization-e-id/actions/workflows/ci.yml/badge.svg)](https://github.com/nikhilamaragani-jpg/blockchain-autonomous-notarization-e-id/actions/workflows/ci.yml)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker)](Dockerfile)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Amaragani Nikhil Sai** · B.Tech mini project · SIIET (JNTUH)
Cryptography · Digital identity concepts · Data analysis

**Scope:** local SHA-256 integrity checks and an SQLite audit ledger. This is not a production notary, blockchain deployment, legal service, or national eID integration.

</div>

---

## Project

The prototype demonstrates how a document fingerprint can be notarized and checked later without storing the document itself. It also turns ledger activity into reproducible metrics for a data-analyst portfolio: notarization volume, unique and repeated fingerprints, average file size, verification outcomes, match rate, and daily activity.

```text
File ──SHA-256──> SQLite integrity record ──> verify original / changed file
                         │
                         └──> SQL metrics · JSON summary · CSV metadata export
```

### What is implemented

- Binary-safe, streaming SHA-256 file hashing; files are never copied into the ledger.
- SQLite records with a UTC timestamp, owner label, file name, fingerprint, and byte size.
- Verification history for match/mismatch reporting, including a migration for existing ledgers.
- CLI commands for notarizing, verifying, listing, analyzing, and exporting records.
- No-argument demo retained for presentations and classroom use.

## Quick start

Requires Python 3.10 or newer.

```bash
git clone https://github.com/nikhilamaragani-jpg/blockchain-autonomous-notarization-e-id.git
cd blockchain-autonomous-notarization-e-id
python -m venv .venv
```

Activate the environment (`.venv\Scripts\Activate.ps1` on Windows or `source .venv/bin/activate` on macOS/Linux), then:

```bash
python -m pip install -r requirements.txt
python src/main.py --help
```

## Try the workflow

```bash
python src/main.py notarize path/to/agreement.pdf --owner analyst-demo
python src/main.py verify 1 path/to/agreement.pdf
python src/main.py list --limit 10
python src/main.py analytics
python src/main.py analytics --format json
python src/main.py export-csv ledger.csv
```

The `notarize` command prints the record ID needed for verification. A changed document returns a nonzero exit code and records a mismatch. Use a pseudonym or demo label for `--owner`; do not enter national identity numbers or other sensitive personal data. By default, the ledger is written to `data/notarization_ledger.db`. Set `NOTARIZATION_DB_PATH` to choose another database location.

Run the original guided demo with:

```bash
python src/main.py
```

## Analytics

`analytics` reports SQL-derived metrics over the local ledger. Metrics and their definitions, sample queries, and interpretation limits are documented in [docs/ANALYTICS.md](docs/ANALYTICS.md). CSV and JSON exports contain ledger metadata and hashes, not document contents; hashes can still be sensitive linkable data, so protect exports appropriately.

## Development

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

The project uses only Python's standard library at runtime. See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for the module map and contribution workflow.

## Documentation

[Academic report](docs/reports/Mini_Project_Blockchain_Notarization_eID_Report.pdf) · [Report summary](docs/REPORT_SUMMARY.md) · [Project brief](docs/PROJECT_BRIEF.md) · [Demo guide](docs/DEMO.md) · [Analytics notes](docs/ANALYTICS.md) · [Security policy](SECURITY.md)

## Roadmap and limitations

This repository is an educational prototype, not a tamper-proof distributed ledger. SQLite rows can be modified by anyone with database access, and a hash alone does not prove who created a document, when it was created, or whether the owner is trustworthy. Production use would require a threat model, authenticated identity/PKI, key management, access controls, privacy/legal review, independent audits, and a deployed consensus-backed chain or trusted timestamping service. Those integrations are not present here.

## License

MIT. See [LICENSE](LICENSE).

## Portfolio positioning

This is an academic / industry-mentored technical project kept as supporting evidence. Its strongest portfolio relevance is auditable data, SQLite analytics, hashing, and reproducible reporting; it is not part of the primary Data Analyst flagship work.

For the current Data Analyst portfolio, see: https://nikhilamaragani-jpg.github.io/
