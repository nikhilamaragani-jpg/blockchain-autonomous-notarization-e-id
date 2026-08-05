<div align="center">

# Blockchain-Based Autonomous Notarization using National eID

### B.Tech Mini Project · Cryptography · Digital Identity · Ledger concepts

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Hashing](https://img.shields.io/badge/Hashing-SHA--256-informational)](https://github.com/nikhilamaragani-jpg/blockchain-autonomous-notarization-e-id)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Runnable%20Prototype-success)](https://github.com/nikhilamaragani-jpg/blockchain-autonomous-notarization-e-id)

**Amaragani Nikhil Sai** · 22X31A0513 · SIIET (JNTUH) · Guide: Ch. Prabhakar  
Industry mentoring: **Conscience Technologies** (Apr–May 2025)

[Quick start](#quick-start) · [Architecture](#system-architecture) · [Scope](#implementation-status) · [Docs](#documentation)

</div>

---

## Problem

Traditional notarization is often physical, slow, and hard to verify remotely. This mini project explores **BANS** ideas: national eID-style identity concepts, cryptographic document fingerprints, and ledger-style integrity verification.

| Traditional limit | Project response |
|-------------------|------------------|
| Paper / manual process | Digital hash + record flow |
| Hard remote verification | Re-hash and compare |
| Weak audit trail | Timestamped ledger records |

---

## System architecture

```text
User + eID concept
        |
        v
Document content → SHA-256 fingerprint
        |
        v
Notarization record (owner, hash, timestamp, status)
        |
        v
Ledger (SQLite demo · blockchain/smart-contract vision)
        |
        v
Verify: re-hash → MATCH / MISMATCH
```

---

## Tech stack

| Area | Technology |
|------|------------|
| Language | Python 3 |
| Hashing | `hashlib` SHA-256 |
| Demo storage | SQLite ledger |
| Report vision | Django UI, Web3/smart contracts, eID/PKI |

---

## Quick start

```bash
git clone https://github.com/nikhilamaragani-jpg/blockchain-autonomous-notarization-e-id.git
cd blockchain-autonomous-notarization-e-id
pip install -r requirements.txt
python src/main.py
```

Demo: hash → create record → verify original (MATCH) → verify tampered (MISMATCH) → list ledger.

---

## Skills demonstrated

| Skill | Evidence |
|-------|----------|
| Security mindset | Integrity via cryptographic hashing |
| Systems thinking | Identity + record + verify flow |
| Applied crypto basics | SHA-256 fingerprints |
| Honest scoping | Prototype vs full stack checklist |

---

## Implementation status

**Runnable prototype**
- [x] SHA-256 hashing  
- [x] Notarization record creation  
- [x] Integrity verification  
- [x] SQLite ledger  

**Full report / future work**
- [ ] On-chain smart contracts  
- [ ] Real national eID / PKI  
- [ ] Full Django web UI from report screens  

---

## Documentation

| File | Purpose |
|------|---------|
| [docs/PROJECT_BRIEF.md](docs/PROJECT_BRIEF.md) | Brief |
| [docs/DEMO.md](docs/DEMO.md) | Demo |
| [docs/INTERVIEW.md](docs/INTERVIEW.md) | Walkthrough |
| [docs/RESUME_BULLETS.md](docs/RESUME_BULLETS.md) | Bullets |
| [docs/ABOUT_TOPICS.md](docs/ABOUT_TOPICS.md) | Topics |

**Suggested topics:** `python` · `blockchain` · `cryptography` · `digital-identity` · `security`

---

## Author

**Amaragani Nikhil Sai** · B.Tech CSE  
Portfolio: https://nikhilamaragani-jpg.github.io/  
Email: nikhilamaragani@gmail.com

## License

MIT — see [LICENSE](LICENSE).
