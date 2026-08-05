<div align="center">

# Blockchain-Based Autonomous Notarization System Using National eID

### B.Tech Mini Project · Blockchain · Digital Identity · Document Integrity

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Crypto](https://img.shields.io/badge/Hashing-SHA--256-informational)](https://github.com/nikhilamaragani-jpg/blockchain-autonomous-notarization-e-id)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Portfolio](https://img.shields.io/badge/Portfolio-Website-5b8cff)](https://nikhilamaragani-jpg.github.io/portfolio/)

**Author:** Amaragani Nikhil Sai (22X31A0513)  
**Guide:** Ch. Prabhakar · **Industry:** Conscience Technologies (Apr–May 2025)

[Run](#quick-start) · [Interview](docs/INTERVIEW.md) · [Demo](docs/DEMO.md) · [Report](docs/REPORT_SUMMARY.md) · [Resume bullets](docs/RESUME_BULLETS.md)

</div>

---

## Executive Summary

Traditional notarization is physical and slow. **BANS** combines national eID concepts with cryptographic document fingerprints and ledger-style storage so integrity can be verified remotely. This repo includes a **runnable** hash → record → verify → ledger prototype.

---

## Quick Start

```bash
git clone https://github.com/nikhilamaragani-jpg/blockchain-autonomous-notarization-e-id.git
cd blockchain-autonomous-notarization-e-id
pip install -r requirements.txt
python src/main.py
```

---

## Documentation suite

| Doc | Purpose |
|-----|---------|
| [INTERVIEW.md](docs/INTERVIEW.md) | Pitch, Europe/eID talking points, Q&A |
| [DEMO.md](docs/DEMO.md) | Terminal walkthrough + mermaid |
| [REPORT_SUMMARY.md](docs/REPORT_SUMMARY.md) | Academic + industry context |
| [RESUME_BULLETS.md](docs/RESUME_BULLETS.md) | Copy-ready bullets |
| [CONTRIBUTING.md](docs/CONTRIBUTING.md) | Dev notes |
| [PROJECT_BRIEF.md](docs/PROJECT_BRIEF.md) | Hiring-manager brief |

---

## Implementation status

- [x] SHA-256 hashing
- [x] Timestamped notarization records
- [x] Integrity verification (match / mismatch)
- [x] SQLite ledger
- [ ] On-chain smart contracts
- [ ] Real national eID / PKI
- [ ] Full Django UI from report screens

## Author

**Amaragani Nikhil Sai** · https://nikhilamaragani-jpg.github.io/portfolio/  
LinkedIn: https://www.linkedin.com/in/nikhil-sai-amaragani-219115382 · Email: nikhilamaragani@gmail.com

## License
MIT — see [LICENSE](LICENSE).
