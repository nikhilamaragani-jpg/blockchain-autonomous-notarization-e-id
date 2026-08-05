# Interview Guide — Blockchain Notarization + National eID (BANS)

## 60-second pitch

> Traditional notarization is physical, slow, and hard to verify remotely. My mini project designs BANS — a Blockchain-Based Autonomous Notarization System using national eID concepts. The runnable prototype hashes documents with SHA-256, stores timestamped notarization records in a ledger-style SQLite store, and verifies integrity by re-hashing. Full scope includes Django UI, smart contracts, and eID/PKI authentication, completed with industry mentoring at Conscience Technologies.

## Problem → Solution → Impact

| | |
|--|--|
| **Problem** | Manual notarization: delay, fraud risk, poor digital UX |
| **Solution** | eID auth + hash fingerprint + immutable ledger + verify path |
| **Impact** | Remote, transparent, tamper-evident document integrity |

## Core flow

1. Authenticate user (eID concept)
2. Hash document content (SHA-256)
3. Store hash + metadata + timestamp
4. Later: re-hash candidate document and compare

## Expected questions

**Q: Why hash instead of storing the full file on-chain?**  
A: Privacy, cost, and size. The hash proves integrity; document can live off-chain/IPFS.

**Q: What does eID add?**  
A: Stronger identity binding than email/password — important for legal notarization trust.

**Q: Legal recognition?**  
A: Varies by jurisdiction; technical integrity ≠ automatic legal validity everywhere.

**Q: Europe relevance?**  
A: Aligns with digital identity, eIDAS-style thinking, and public-sector trust infrastructure themes.

## Demo

```bash
pip install -r requirements.txt
python src/main.py
```

## Resume bullets

- Designed a **blockchain + national eID** autonomous notarization concept with SHA-256 integrity, ledger records, and verification workflow.
- Implemented a runnable Python prototype for hash → record → verify with SQLite ledger persistence.
- Completed industry-linked mini project with Conscience Technologies (Apr–May 2025).
