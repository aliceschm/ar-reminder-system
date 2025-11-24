-- table with open balance for AR reminder system and API consumption
CREATE TABLE public.open_ar (
    doc_number          VARCHAR(100) PRIMARY KEY,  
    customer_id         CHAR(8) NOT NULL,
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
    updated_at          TIMESTAMP DEFAULT NOW()

);
