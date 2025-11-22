CREATE TABLE public.cntrl_logs (
    log_id SERIAL PRIMARY KEY,
    process_name TEXT NOT NULL,        -- ex: update_invoices, update_payments
    last_updt_time TIMESTAMP NOT NULL DEFAULT now(),
    info TEXT                          -- description
);
