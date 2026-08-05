# Demo Walkthrough — BANS Notarization Prototype

## Expected flow

```text
============================================================
 Blockchain Autonomous Notarization (BANS) Prototype
 Hash · Record · Verify · Ledger
============================================================
1) Create notarization record
2) Verify document integrity
...
Record stored with SHA-256 fingerprint + timestamp
Verification: MATCH / MISMATCH
```

## Architecture

```mermaid
flowchart TD
  U[User + eID concept] --> H[SHA-256 Hash]
  H --> R[Notarization Record]
  R --> L[(Ledger SQLite / Blockchain vision)]
  L --> V[Verify by re-hash]
  V --> C{Match?}
  C -->|Yes| OK[Integrity confirmed]
  C -->|No| BAD[Tamper suspected]
```
