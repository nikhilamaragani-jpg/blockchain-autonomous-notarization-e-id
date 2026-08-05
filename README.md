# Blockchain-Based Autonomous Notarization Using National E-ID

**B.Tech Mini Project** | Blockchain Concepts | Digital Identity | Document Integrity

A prototype that demonstrates document hashing, verification, and ledger-style storage for a digital notarization workflow.

---

## Overview

This project focuses on core ideas behind trustworthy digital notarization:

- Generate a cryptographic hash of document content
- Create a notarization-style record
- Verify integrity by re-hashing
- Store records in a local ledger (SQLite)

**Project Type:** Academic Prototype  
**Status:** Runnable hashing + verification + ledger demo

---

## Architecture

```text
Document Content
      |
      v
+------------------+
| Hash Generator   |  (SHA-256)
+------------------+
      |
      v
+------------------+
| Notarization     |  (create record with owner + timestamp)
+------------------+
      |
      v
+------------------+
| SQLite Ledger    |  (persistent record storage)
+------------------+
      |
      v
Integrity Verification
```

---

## Tech Stack

| Area | Technology |
|------|------------|
| Language | Python |
| Cryptography | SHA-256 hashing |
| Storage | SQLite |
| Concepts | Digital identity, immutable records |

---

## Project Structure

```text
blockchain-autonomous-notarization-e-id/
├── README.md
├── requirements.txt
├── data/
├── src/
│   ├── main.py
│   ├── hasher.py
│   ├── notarization.py
│   └── database.py
└── LICENSE
```

---

## How to Run

```bash
git clone https://github.com/nikhilamaragani-jpg/blockchain-autonomous-notarization-e-id.git
cd blockchain-autonomous-notarization-e-id

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python src/main.py
```

---

## Current Status

- [x] Hash-based integrity demo
- [x] Notarization record creation
- [x] Verification logic
- [x] SQLite ledger storage
- [ ] Smart contract implementation
- [ ] Real E-ID provider integration

---

## Author

**Amaragani Nikhil Sai**  
B.Tech in Computer Science and Engineering

- GitHub: [nikhilamaragani-jpg](https://github.com/nikhilamaragani-jpg)
- LinkedIn: [Amaragani Nikhil Sai](https://linkedin.com/in/amaraganinikhilsai)
- Email: nikhilamaragani@gmail.com

---

## License

MIT License
