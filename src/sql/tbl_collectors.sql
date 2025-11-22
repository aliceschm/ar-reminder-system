-- collectors: accounts receivable team responsible for collections
CREATE TABLE public.collectors (
    collector_id    SERIAL PRIMARY KEY,
    collector_name  VARCHAR(255) NOT NULL,
    email           VARCHAR(255),
    region          VARCHAR(100),                 -- region or customer portfolio
    created_at      TIMESTAMPTZ DEFAULT NOW()
);