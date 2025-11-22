-- contracts: agreements belonging to customers (a customer may have multiple contracts)
CREATE TABLE public.contracts (
    contract_id     SERIAL PRIMARY KEY,
    customer_id     CHAR(8) NOT NULL REFERENCES public.customers(customer_id) ON DELETE CASCADE,
    contract_number VARCHAR(100) UNIQUE,          -- external contract identifier
    contract_type   VARCHAR(100),                 -- e.g., "Subscription", "Service Agreement", "Purchase Order"
    start_date      DATE,
    end_date        DATE,
    currency        VARCHAR(10),                  -- default currency for invoices under this contract
    notes           TEXT,                         -- optional internal notes
    created_at      TIMESTAMPTZ DEFAULT NOW()
);