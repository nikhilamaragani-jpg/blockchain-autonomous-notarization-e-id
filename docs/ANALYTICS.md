# Ledger analytics

The CLI's `analytics` command uses SQL aggregates over the local SQLite ledger and verification history. It analyzes metadata only; document contents are never stored.

```bash
python src/main.py analytics
python src/main.py analytics --format json > analytics.json
python src/main.py export-csv ledger.csv
```

## Metric definitions

| Metric | Definition |
| --- | --- |
| Total notarizations | Number of ledger records, including repeat notarizations of the same file |
| Unique documents | Distinct SHA-256 fingerprints in the ledger |
| Duplicate notarizations | Total records minus unique fingerprints |
| Average file size | Mean recorded file size in bytes; pre-migration records count as zero because their sizes were not captured |
| Total verifications | Number of verification attempts made with the CLI |
| Matches / mismatches | Attempts whose file fingerprint did / did not match the selected record |
| Match rate | Matches divided by all verification attempts, as a percentage; `N/A` when there are no attempts |
| Daily activity | Number of notarization records grouped by UTC calendar date |

Example SQL for investigating repeat notarizations:

```sql
SELECT document_hash,
       COUNT(*) AS notarization_count,
       MIN(created_at) AS first_notarized_at,
       MAX(created_at) AS last_notarized_at
FROM ledger
GROUP BY document_hash
HAVING COUNT(*) > 1
ORDER BY notarization_count DESC;
```

Verification outcome query:

```sql
SELECT matched, COUNT(*) AS attempts
FROM verification_events
GROUP BY matched;
```

## Interpretation and privacy

These are descriptive metrics for the records in one local database, not evidence of network-wide adoption, fraud, or legal validity. Repeat fingerprints may represent legitimate repeat submissions. Verification outcomes are recorded only when verification is run through this CLI; they are not an independently authenticated audit log. Small samples and demo runs should not be used to infer population-level trends.

The CSV export includes names, owner labels, timestamps, file sizes, and hashes. Never use a real national ID as the owner label. A cryptographic hash is not document encryption and may be linkable to known documents; restrict access to the database and exported files.
