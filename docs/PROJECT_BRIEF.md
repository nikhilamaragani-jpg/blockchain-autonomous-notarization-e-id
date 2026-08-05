# Project Brief — Blockchain Autonomous Notarization (BANS) + National eID

## Snapshot

| Field | Detail |
|-------|--------|
| Project type | B.Tech Mini Project |
| Title | Blockchain Based Autonomous Notarization System Using National E-ID |
| Author | A. Nikhil Sai (22X31A0513) |
| Institution | Sri Indu Institute of Engineering and Technology (JNTUH) |
| Guide | Ch. Prabhakar |
| Industry | Conscience Technologies (Apr–May 2025) |
| Year | 2024–2025 |

## Motivation

Manual notarization is slow and inconvenient. Blockchain immutability + national eID authentication create a path to autonomous, remotely verifiable document notarization.

## Problem definition

Existing systems rely on physical presence and manual checks → delays, fraud risk, limited scalability, weak digital integration.

## Objectives

- Secure digital document authentication without mandatory physical notary visits
- Tamper-proof recording of document fingerprints
- Transparent, independently verifiable records
- Reduced operational cost and turnaround time

## Proposed system highlights

- Remote submission through a secure web interface (report)
- eID + PIN / biometric / digital signature style authentication
- Document encryption + timestamp + unique hash on decentralized ledger
- Smart contracts for validation automation
- Verifier role for authorized authenticity checks

## Technology stack (report)

- Frontend: HTML, CSS, JavaScript
- Backend: Python + Django
- Hashing: Python `hashlib` SHA-256
- DB: SQLite (metadata, users, notary entries)
- Blockchain interaction concepts: Web3.py / Ethereum test network
- Optional: IPFS for document storage (hash reference on ledger)
- Optional analytics libs mentioned: NumPy, Pandas, Matplotlib; future ML anomaly ideas

## Repo mapping

This GitHub project focuses on the **integrity core** (hash → record → verify → ledger) so recruiters can assess applied security thinking without needing a full blockchain testnet setup.

## Interview talking points

1. Why store hashes instead of full documents on-chain?
2. How does eID authentication change trust assumptions?
3. What are legal recognition limits across jurisdictions?
4. How would you design verifier permissions and audit trails?
