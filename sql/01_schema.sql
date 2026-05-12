CREATE TABLE public.collectors (
    collector_id    SERIAL PRIMARY KEY,
    collector_name  VARCHAR(255) NOT NULL,
    email           VARCHAR(255),
    region          VARCHAR(100),
    created_at      TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE public.customers (
    customer_id     CHAR(8) PRIMARY KEY,
    customer_name   VARCHAR(255) NOT NULL,
    tax_id          VARCHAR(50),
    segment         VARCHAR(100),
    country         VARCHAR(100),
    created_at      TIMESTAMPTZ DEFAULT NOW(),
    collector_id    INTEGER REFERENCES public.collectors(collector_id)
);

CREATE TABLE public.currency (
    date            DATE NOT NULL,
    currency_code   VARCHAR(3) NOT NULL,
    usd_rate        NUMERIC(18, 6) NOT NULL,
    PRIMARY KEY (date, currency_code)
);

CREATE TABLE public.issued_invoices (
    doc_number       VARCHAR(100) NOT NULL,
    customer_id      CHAR(8) NOT NULL REFERENCES public.customers(customer_id) ON DELETE CASCADE,
    contract_number  VARCHAR(100),
    issue_date       DATE NOT NULL,
    due_date         DATE NOT NULL,
    amount           NUMERIC(12, 2) NOT NULL,
    currency_code    VARCHAR(10) NOT NULL,
    description      TEXT,
    created_at       TIMESTAMPTZ DEFAULT NOW(),
    document_type    VARCHAR(20) NOT NULL DEFAULT 'INVOICE',
    type             TEXT DEFAULT 'Leasing',
    doc_reference    VARCHAR(100),
    PRIMARY KEY (doc_number, customer_id, document_type)
);

CREATE TABLE public.open_ar (
    doc_number          VARCHAR(100) NOT NULL,
    customer_id         CHAR(8) NOT NULL,
    document_type       VARCHAR(20) NOT NULL,
    contract_number     VARCHAR(100),
    issue_date          DATE NOT NULL,
    due_date            DATE NOT NULL,
    total_amount        NUMERIC(18, 6) NOT NULL,
    balance_amount      NUMERIC(18, 6) NOT NULL,
    amount_usd          NUMERIC(18, 6),
    balance_amount_usd  NUMERIC(18, 6),
    aging_group         VARCHAR(20),
    status              VARCHAR(20) NOT NULL DEFAULT 'OPEN',
    comment             TEXT,
    created_at          TIMESTAMP NOT NULL,
    last_updt_time      TIMESTAMP DEFAULT NOW(),
    collector           VARCHAR(255),
    last_reminder_dt    TIMESTAMP,
    PRIMARY KEY (doc_number, customer_id, document_type)
);

CREATE TABLE public.rejected_invoices (
    rejected_invoice_id SERIAL PRIMARY KEY,
    doc_number          VARCHAR(100),
    customer_id         CHAR(8),
    document_type       VARCHAR(20),
    contract_number     VARCHAR(100),
    issue_date          DATE,
    due_date            DATE,
    amount              NUMERIC(12, 2),
    currency_code       VARCHAR(10),
    rejection_stage     VARCHAR(100) NOT NULL,
    rejection_reason    TEXT NOT NULL,
    created_at          TIMESTAMPTZ,
    rejected_at         TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE TABLE public.process_runs (
    log_id          SERIAL PRIMARY KEY,
    process_name    TEXT NOT NULL,
    last_updt_time  TIMESTAMP NOT NULL DEFAULT NOW(),
    info            TEXT
);
