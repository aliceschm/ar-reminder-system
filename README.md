# Open AR Pipeline

Python ETL pipeline for Accounts Receivable operations that incrementally builds and maintains an open_ar table from issued invoices.
The pipeline extracts newly issued invoices, enriches them with currency conversion and collector ownership data, transforms the information into an operational receivables view, and logs each execution for traceability.

---

## Features

- Incremental invoice extraction
- Currency normalization to USD
- Collector ownership enrichment
- Aging bucket calculation
- Open AR materialization
- Pipeline execution logging
- Dockerized PostgreSQL environment

---

## Tech Stack

- Python
- Pandas
- SQLAlchemy
- PostgreSQL
- Docker Compose

---

## Architecture

```txt
issued_invoices
        ↓
extract
        ↓
transform
  - currency conversion
  - collector enrichment
  - aging calculation
        ↓
load
        ↓
open_ar
```
---

## How to run it locally

### 1. Start PostgreSQL

```bash
docker compose up -d
```

### 2. Create environment file

```bash
cp .env.example .env
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the pipeline

```bash
python src/main.py
```

### 5. Issue more invoices without resetting PostgreSQL

```bash
python src/issue_new_invoices.py --count 10
python src/main.py
```

The helper script inserts fresh rows into `issued_invoices` with new document numbers and current timestamps, so the incremental pipeline picks them up on the next run.

---

## Example Queries

### Open invoices

```sql
SELECT * FROM open_ar;
```

### Collector portfolio totals

```sql
SELECT
    collector,
    SUM(balance_amount_usd) AS total_balance_usd
FROM open_ar
GROUP BY collector;
```

### Overdue invoices

```sql
SELECT
    doc_number,
    customer_id,
    due_date,
    aging_group,
    balance_amount_usd
FROM open_ar
WHERE aging_group != 'Not due';
```

---

## Sample Output

```txt
==================================================
OPEN AR PIPELINE
==================================================

[START] Pipeline execution started

[INFO] Last run: first execution
[INFO] New invoices found: 50

[TRANSFORM] Invoices transformed: 43
[TRANSFORM] Invoices rejected: 7

[CHECK] Currency found for all invoice currencies: NO
[CHECK] Missing currency codes: AUD, CAD, CHF, GBP, JPY, MXN
[CHECK] All collectors assigned correctly: NO
[CHECK] Customers without collectors: CUST0003

[LOAD] Open AR updated: 43 rows inserted
[LOAD] Rejected invoices stored: 7 rows inserted

[SUCCESS] Process run logged
[END] Pipeline finished successfully

==================================================
```

---

## Database Initialization

The PostgreSQL container automatically initializes:

- schema creation
- seed data
- sample invoices
- sample currency rates
- sample collectors/customers

using:

```txt
sql/01_schema.sql
sql/02_seed.sql
```
