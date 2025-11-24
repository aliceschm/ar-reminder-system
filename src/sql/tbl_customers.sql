-- customers: basic customer registry
CREATE TABLE public.customers (
    customer_id     CHAR(8) PRIMARY KEY,           -- 8-digit alphanumeric ID
    customer_name   VARCHAR(255) NOT NULL,
    tax_id          VARCHAR(50),                  -- fiscal identifier (optional)
    segment         VARCHAR(100),                 -- customer segment/industry (optional)
    country         VARCHAR(100),
    collector_id    INT REFERENCES public.collectors(collector_id),
    created_at      TIMESTAMPTZ DEFAULT NOW()
);
