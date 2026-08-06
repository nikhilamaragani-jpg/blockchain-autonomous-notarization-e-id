<div align="center">

# Blockchain-Based Autonomous Notarization using National eID

### B.Tech Mini Project (2024–2025) · Cryptography · Digital Identity

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](Dockerfile)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Amaragani Nikhil Sai** · Roll **22X31A0513** · SIIET (JNTUH)  
**Guide:** Ch. Prabhakar · Industry mentoring: **Conscience Technologies** (Apr–May 2025)

SQLite ledger demo — not a mainnet deployment.  
Report notes: [docs/REPORT_SUMMARY.md](docs/REPORT_SUMMARY.md)

</div>

---

## Problem

Traditional notarization is often physical, slow, and hard to verify remotely. This mini project explores cryptographic fingerprints, eID-oriented identity concepts, and integrity verification.

---

## Solution

Runnable prototype: **hash document → create notarization record → store ledger row → verify original vs tampered content**.

---

## Architecture

![Architecture](images/architecture.svg)

```text
Document → SHA-256 → Record (owner / eID concept, timestamp)
  → Ledger (SQLite demo) → Verify MATCH / MISMATCH
```

---

## Tech stack

Python · hashlib (SHA-256) · SQLite · Docker · pytest

---

## Installation & usage

```bash
git clone https://github.com/nikhilamaragani-jpg/blockchain-autonomous-notarization-e-id.git
cd blockchain-autonomous-notarization-e-id
pip install -r requirements.txt
python src/main.py
pytest -q
```

---

## Documentation

[REPORT_SUMMARY](docs/REPORT_SUMMARY.md) · [PROJECT_BRIEF](docs/PROJECT_BRIEF.md) · [DEMO](docs/DEMO.md) · [INTERVIEW](docs/INTERVIEW.md) · [RESUME_BULLETS](docs/RESUME_BULLETS.md)

## License

MIT · **Author:** Amaragani Nikhil Sai · https://nikhilamaragani-jpg.github.io/
