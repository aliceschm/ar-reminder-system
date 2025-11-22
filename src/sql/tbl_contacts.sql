-- contacts: contacts related to each customer
CREATE TABLE public.contacts (
    contact_id      SERIAL PRIMARY KEY,
    customer_id     CHAR(8) NOT NULL REFERENCES public.customers(customer_id) ON DELETE CASCADE,
    contact_name    VARCHAR(255),
    email           VARCHAR(255),
    phone           VARCHAR(50),
    role            VARCHAR(100),                 -- contact role (e.g., billing, finance, legal)
    created_at      TIMESTAMPTZ DEFAULT NOW()
);