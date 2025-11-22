-- payments: payments received from customers (not directly linked to invoices)
CREATE TABLE public.payments (
    payment_id        VARCHAR(100) PRIMARY KEY,
    customer_id       CHAR(8) NOT NULL REFERENCES public.customers(customer_id) ON DELETE CASCADE,
    payment_date      DATE NOT NULL,
    payment_amount    NUMERIC(12,2) NOT NULL,
    payment_currency  VARCHAR(10) NOT NULL,   -- currency used in the payment
    created_at        TIMESTAMPTZ DEFAULT NOW()
);