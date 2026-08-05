<div align="center">

# Blockchain-Based Autonomous Notarization System Using National eID

### B.Tech Mini Project · Blockchain · Digital Identity · Document Integrity

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Crypto](https://img.shields.io/badge/Hashing-SHA--256-informational)](https://github.com/nikhilamaragani-jpg/blockchain-autonomous-notarization-e-id)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Runnable%20Prototype-success)](https://github.com/nikhilamaragani-jpg/blockchain-autonomous-notarization-e-id)

**Author:** Amaragani Nikhil Sai (22X31A0513)  
**Institution:** Sri Indu Institute of Engineering and Technology (JNTUH)  
**Guide:** Ch. Prabhakar · Industry mentor: Conscience Technologies (Apr–May 2025)

[Run](#quick-start) · [Architecture](#system-architecture) · [Skills](#skills-recruiters-care-about) · [Docs](docs/PROJECT_BRIEF.md)

</div>

---

## Executive Summary (for recruiters)

Traditional notarization often requires physical presence, paper processes, and manual verification — slow, costly, and hard to scale for digital-first workflows.

This mini project introduces **BANS (Blockchain-Based Autonomous Notarization System)** concepts that combine:

- **National eID-style identity verification** (PIN / biometric / digital signature concepts)
- **Cryptographic document fingerprints** (SHA-256)
- **Immutable ledger-style storage** of hashes + metadata
- **Smart-contract style verification vision**
- **Independent later verification** of document integrity

The repository includes a **runnable hashing + verification + SQLite ledger prototype** that demonstrates the core integrity workflow recruiters and interviewers can execute immediately.

---

## Problem Statement

| Traditional limitation | BANS response |
|------------------------|---------------|
| Physical notary visits | Remote, digital workflow concepts |
| Paper / manual risk of fraud | Hash + ledger immutability |
| Hard remote verification | Re-hash and compare records |
| Centralized trust only | Decentralized ledger principles |
| High operational cost | Automated notarization path |

---

## Objectives (from project report)

- Develop autonomous digital notarization integrating blockchain + national eID concepts
- Reduce manual intervention in authentication workflows
- Improve security, transparency, accessibility, and turnaround time
- Enable real-time verification of notarized document fingerprints

---

## System Architecture

```text
User + National eID (concept: PIN / biometric / digital signature)
                    |
                    v
         Document upload / input
                    |
                    v
         SHA-256 document fingerprint
                    |
                    v
   Notarization record (owner, hash, timestamp, signature concept)
                    |
                    v
   Ledger layer (SQLite demo · blockchain / smart contract vision)
                    |
                    v
   Verification + transaction receipt as certificate (concept)
```

**Full-stack vision from report:** Django backend · HTML/CSS/JS frontend · Web3.py / Ethereum interaction · optional IPFS for document storage (hash on-chain only) · verifier login for authorized validation.

---

## Key Features (report)

1. Remote document submission concepts  
2. eID-based identity verification concepts  
3. Blockchain / ledger recording of hashes  
4. Smart contract verification vision  
5. Notary management (add / view / delete records)  
6. Verifier access for validation  
7. Real-time transparency of notarization records  
8. User-friendly interface design (screens documented in report)

---

## Tech Stack

| Area | Technology |
|------|------------|
| Language | Python 3 |
| Hashing | `hashlib` SHA-256 |
| Demo storage | SQLite ledger |
| Report stack | Django · HTML/CSS/JS · Web3.py · smart contracts · eID/PKI · IPFS (optional) |

---

## Repository Structure

```text
blockchain-autonomous-notarization-e-id/
├── docs/
│   └── PROJECT_BRIEF.md
├── src/
│   ├── main.py
│   ├── hasher.py
│   ├── notarization.py
│   └── database.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## Quick Start

```bash
git clone https://github.com/nikhilamaragani-jpg/blockchain-autonomous-notarization-e-id.git
cd blockchain-autonomous-notarization-e-id
pip install -r requirements.txt
python src/main.py
```

Demo flow: create notarization record → store hash + metadata → verify integrity by re-hashing.

---

## Implementation Status

- [x] Cryptographic hashing of content/documents
- [x] Timestamped notarization records
- [x] Integrity verification
- [x] Persistent SQLite ledger
- [ ] On-chain smart contract deployment
- [ ] Real national eID / PKI integration
- [ ] Full Django web UI from report screens

---

## Skills Recruiters Care About

| Skill | Evidence |
|-------|----------|
| Security mindset | Hashing, integrity, tamper resistance |
| Systems thinking | Identity + ledger + verification flow |
| Applied cryptography basics | SHA-256 fingerprints |
| Product/domain framing | Notarization modernization |
| Honest engineering | Clear prototype vs full-scope checklist |
| Europe-relevant themes | eID, digital public services, trust infrastructure |

---

## Academic & Industry Context

- **College project** under Ch. Prabhakar (SIIET)
- **Industry mini-project certificate:** Conscience Technologies (1 Apr 2025 – 27 May 2025)
- Report includes UML diagrams, signup/login/notary/verifier screens, and testing strategy

---

## Author

**Amaragani Nikhil Sai**  
B.Tech CSE · Secure systems & applied AI focus

- GitHub: [nikhilamaragani-jpg](https://github.com/nikhilamaragani-jpg)
- LinkedIn: [nikhil-sai-amaragani](https://www.linkedin.com/in/nikhil-sai-amaragani-219115382)
- Email: nikhilamaragani@gmail.com

---

## License

MIT License — see [LICENSE](LICENSE).
