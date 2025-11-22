-- adjustments: link multiple items (payments, invoices, credit notes)
CREATE TABLE public.adjustments (
    adjustment_id       SERIAL NOT NULL,        -- unique adjustment batch
    customer_id         CHAR(8) NOT NULL REFERENCES public.customers(customer_id) ON DELETE CASCADE,
    item_id             VARCHAR(100),           -- id of the item (payment_id or invoice_id)
    item_type           VARCHAR(20) NOT NULL,   -- 'INVOICE', 'PAYMENT', 'CREDIT_NOTE'
    item_currency       VARCHAR(10) NOT NULL,   -- currency of the item
    adjustment_amount   NUMERIC(12,2) NOT NULL, -- amount applied/adjusted
    adjustment_type     CHAR(2) NOT NULL,       -- adjustment code, e.g., 'A1', 'C1', 'M1'
    last_updt_time      TIMESTAMPTZ DEFAULT NOW()
    PRIMARY KEY (adjustment_id, item_id)

);