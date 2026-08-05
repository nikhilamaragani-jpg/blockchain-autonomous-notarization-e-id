# Project walkthrough — Blockchain Notarization + eID

## 60-second summary

Notarization is often physical and hard to verify remotely. My mini project explores BANS: cryptographic document fingerprints (SHA-256), timestamped records, ledger storage, and integrity verification. The runnable prototype proves the integrity core; the report covers eID, smart contracts, and web UI vision. Completed with Conscience Technologies mentoring.

## Demo

```bash
pip install -r requirements.txt
python src/main.py
```

## Questions

**Why store hashes not full files?** Privacy, size, and cost; hash proves integrity.  
**What does eID add conceptually?** Stronger identity binding for the creator of the record.  
**Prototype honesty?** SQLite ledger demo ≠ deployed blockchain + real eID.
