# Contributing

## Setup and tests

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

The runtime uses only the Python standard library. Tests use temporary databases; they do not need a real eID, network, or blockchain node.

## Module map

- `src/hasher.py` — text, bytes, and streaming file SHA-256 helpers
- `src/notarization.py` — record creation and integrity comparison
- `src/database.py` — SQLite schema, legacy migration, and analytics queries
- `src/main.py` — CLI commands and retained classroom demo
- `tests/` — hashing, migration, database, CLI, and analytics coverage

Keep the prototype's scope clear: do not claim real blockchain immutability, legal notarization, or national eID/PKI authentication. New analytics should state their definitions, data source, and interpretation limits. Do not commit personal documents, identity data, generated databases, or exported ledger files.

## Future extensions

- Authenticated eID/PKI integration using a documented sandbox
- Trusted timestamping and independently verifiable audit proofs
- A deployed smart-contract implementation and threat model
- A dashboard for exploring aggregate ledger metrics
