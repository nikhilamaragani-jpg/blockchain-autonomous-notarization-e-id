# Academic Report Summary — BANS Mini Project

**Title:** Blockchain Based Autonomous Notarization System Using National E-ID  
**Student:** A. Nikhil Sai · 22X31A0513  
**Institution:** Sri Indu Institute of Engineering and Technology (JNTUH)  
**Guide:** Ch. Prabhakar  
**Industry:** Conscience Technologies (1 Apr 2025 – 27 May 2025)  
**Year:** 2024–2025

## Introduction (condensed)

Traditional notarization often requires physical presence and manual verification. BANS combines blockchain immutability with national eID authentication to enable secure, autonomous digital notarization.

## Objectives

- Autonomous digital notarization integrating blockchain + national eID
- Reduce manual intervention
- Improve security, transparency, accessibility, turnaround time
- Enable real-time verification of document fingerprints

## Key features (report)

1. Remote document submission
2. eID-based identity verification (PIN / biometric / digital signature concepts)
3. Blockchain integration for hash recording
4. Smart contract verification
5. Notary management functions
6. Verifier access for authorized validation
7. Real-time transparency
8. User-friendly interface

## Tech stack (report)

HTML/CSS/JS frontend · Python Django backend · hashlib SHA-256 · SQLite · Web3.py / Ethereum concepts · optional IPFS

## Screens documented

Signup · Login · Create/Add Notary · Notary details · Verifier login · Verify notary · Verification result/fail

## Repository mapping

| Report concept | Repo module |
|----------------|-------------|
| Document fingerprint | `src/hasher.py` |
| Notarization + verify | `src/notarization.py` |
| Ledger | `src/database.py` |
| Demo entry | `src/main.py` |

## Full PDF

Place official mini project PDF at:

`docs/reports/MINI_PROJECT_BLOCKCHAIN_NOTARIZATION_EID.pdf`

(Local source: `OneDrive/Documents/B.TECH PROJECTS/FINAL MINI PROJECT.pdf`)
