# Blockchain-Based Autonomous Notarization System Using National E-ID

**B.Tech Mini Project** | Blockchain Concepts | Digital Identity | Document Integrity | Smart Contracts

A prototype demonstrating core principles of autonomous digital notarization: document hashing, integrity verification, and ledger-style record keeping. The full project explores fixed-date notarization combining national eID, Public Key Infrastructure (PKI), and blockchain/smart contracts so that a transaction receipt itself serves as a notarization certificate.

---

## Overview

Traditional notarization often requires manual verification of content. Fixed-date notarization only guarantees that a document existed at a certain time (without validating content authenticity). This enables automation via:

- National eID-based authentication of the creator
- Cryptographic hashing of the document
- Storage of the hash + metadata on a blockchain / ledger
- Smart-contract verification of signatures and timestamps
- Transaction receipt acting as the notarization certificate

**Status:** Runnable hashing + verification + SQLite ledger prototype  
**Focus:** Document integrity, autonomous recording, and verifiable audit trails

---

## System Architecture (Aligned with Project Report)

```text
User + National eID (concept)
        |
        v
+---------------------------+
| Document Upload / Hash    |  SHA-256 fingerprint
+---------------------------+
        |
        v
+---------------------------+
| Notarization Record       |  Owner, hash, timestamp, signature concept
+---------------------------+
        |
        v
+---------------------------+
| Ledger / Blockchain Layer |  SQLite (demo) or smart-contract storage
+---------------------------+
        |
        v
Verification + Transaction Receipt as Certificate
```

Full-stack vision from the report includes Django backend, web frontend, Web3.py / Ethereum interaction, and optional IPFS for document storage (hash only on-chain).

---

## Tech Stack

| Area              | Technology / Concept                     |
|-------------------|------------------------------------------|
| Language          | Python 3                                 |
| Cryptography      | SHA-256 (hashlib)                        |
| Storage           | SQLite ledger                            |
| Full Scope        | Django, HTML/CSS/JS, Web3.py, smart contracts, eID/PKI |

---

## Project Structure

```text
blockchain-autonomous-notarization-e-id/
├── src/
│   ├── main.py           # CLI demo entry
│   ├── hasher.py         # SHA-256 document hashing
│   ├── notarization.py   # Record creation & verification
│   └── database.py       # SQLite ledger
├── requirements.txt
└── README.md
```

---

## How to Run

```bash
git clone https://github.com/nikhilamaragani-jpg/blockchain-autonomous-notarization-e-id.git
cd blockchain-autonomous-notarization-e-id
pip install -r requirements.txt
python src/main.py
```

Demo flow: create a notarization record from text/content → store hash + metadata → verify integrity later.

---

## Current Status vs Full Scope

- [x] Cryptographic hashing of documents
- [x] Notarization record creation with timestamp
- [x] Integrity verification by re-hashing
- [x] Persistent SQLite ledger
- [ ] Smart contract deployment & on-chain verification
- [ ] Real national eID / PKI integration
- [ ] Web UI (Django) and transaction-receipt certificates

---

## Author

**Amaragani Nikhil Sai**  
B.Tech in Computer Science and Engineering  
Sri Indu Institute of Engineering and Technology

- GitHub: [nikhilamaragani-jpg](https://github.com/nikhilamaragani-jpg)
- LinkedIn: [Amaragani Nikhil Sai](https://linkedin.com/in/amaraganinikhilsai)
- Email: nikhilamaragani@gmail.com

---

## License

MIT License
