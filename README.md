# AR Reminder System

Modular Accounts Receivable system designed to consolidate invoice data,
expose read models via API, and enable automation and analytical workflows.

---

## Current Status — Phase 1: Data Layer (Implemented)

The data foundation of the system is fully implemented.

- Incremental extraction from `issued_invoices`
- Currency normalization (USD conversion)
- Aging bucket calculation
- Collector assignment
- Materialization into `open_ar`
- Execution logging and run control

This phase establishes a stable read model to support future API, automation, and interface layers.

---

## Roadmap

| Phase | Scope | Status |
|-------|-------|--------|
| 1. Data Layer (ETL) | Incremental pipeline → `open_ar` materialization | ✅ Implemented |
| 2. Read API | `GET /open-ar`, filters, pagination, dashboard aggregations | 🔄 Planned |
| 3. Interface (separate repository) | Collector view + management dashboard | ⏳ Planned |
| 4. Automation | Scheduled reminders based on aging buckets | ⏳ Planned |
| 5. Actions (Transactional) | Apply payment, write-off, manual reminder, audit trail | ⏳ Planned |
| 6. AI Assistant | Prioritization insights and risk signals | ⏳ Planned |

---

## Tech Stack (Current Phase)

- Python
- Pandas
- PostgreSQL
- SQLAlchemy (engine-level usage)
- Raw SQL for explicit query control

Future phases will introduce:

- FastAPI (REST layer)
- Frontend interface
- Workflow automation
- AI-driven insight layer

---

## Design Principles

- Data-first architecture (stable read model before transactional complexity)
- Clear separation between data processing and API layers
- Modular evolution to avoid large refactors in future phases
