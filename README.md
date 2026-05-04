# AR Reminder System

Accounts Receivable system designed to consolidate invoice data, expose financial state via read models, and enable automation and analytical workflows.

---

## Overview

This project started as a full AR system, with planned support for:
- API access
- collector interfaces
- automation (reminders)
- transactional operations (payments, write-offs)

The initial implementation focused on building a **reliable financial read model** as the foundation for these features.

---

## Implemented — Data Layer (Phase 1)

The data foundation of the system is fully implemented.

- Incremental extraction from `issued_invoices`
- Currency normalization (USD conversion)
- Aging bucket calculation
- Collector assignment
- Materialization into `open_ar`
- Execution logging and run control

This phase produces a consistent and queryable view of open receivables, designed to support dashboards, automation, and downstream services.

---

## Original Design Approach

The system was designed around a **data-first architecture**, where:

- financial state is computed via ETL
- `open_ar` acts as the central read model
- APIs, automation, and interfaces consume this derived state

Planned evolution included:

- Read API (`GET /open-ar`, filters, aggregations)
- Collector interface and dashboards
- Automated reminders based on aging buckets
- Transactional actions (payments, write-offs, adjustments)
- AI-driven prioritization

---

## Limitations Identified

During development, some limitations of this approach became clear:

- Financial state is **derived but not explicitly modeled**
- No clear representation of **state changes over time**
- Operational actions (payments, adjustments) are difficult to model cleanly
- Limited auditability of how invoice state evolves
- Tight coupling between data computation and business logic

These constraints make it harder to evolve the system into a full operational AR platform.

---

## Architecture Evolution

Based on these limitations, the system is being redesigned using an **event-driven approach**, where:

- document ingestion produces domain events
- invoice lifecycle is modeled through operations
- financial state is derived from events, not recomputed
- read models (like `open_ar`) become projections, not the source of truth

This repository represents the **first iteration** of the system, focused on building a stable financial read model.

The next iteration focuses on modeling Accounts Receivable as a set of domain operations and state transitions.

---

## Next Iteration

The system is currently being redesigned as a separate project (`ar-ops`) using an event-driven approach.

This iteration focuses on:
- modeling invoice lifecycle through domain events
- explicit state transitions (payments, adjustments, write-offs)
- projections for read models (e.g. `open_ar`)

(Repository will be published soon)
