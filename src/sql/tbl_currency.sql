CREATE TABLE public.currency (
    date DATE NOT NULL,
    currency_code VARCHAR(3) NOT NULL,
    usd_rate NUMERIC(18,6) NOT NULL,
    PRIMARY KEY (date, currency_code)
);
