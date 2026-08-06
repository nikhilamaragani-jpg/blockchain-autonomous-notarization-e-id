# Project walkthrough — Blockchain Notarization + eID

## 60-second pitch

My mini project (2024–25, guide Ch. Prabhakar, roll 22X31A0513) is *Blockchain Based Autonomous Notarization System Using National E-ID*. I also practiced the implementation path with Conscience Technologies mentoring. The GitHub demo proves the integrity core: SHA-256 fingerprint, timestamped record, ledger storage, and MATCH vs MISMATCH verification.

## Demo

```bash
pip install -r requirements.txt
python src/main.py
```

## Questions

**Why store hashes not full files?** Privacy, size, integrity proof.  
**What does eID add conceptually?** Stronger binding of who created the record.  
**Is this on a public blockchain?** No — SQLite ledger prototype; chain/contracts are roadmap.
