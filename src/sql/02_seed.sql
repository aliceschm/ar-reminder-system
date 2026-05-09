INSERT INTO public.collectors (
    collector_name,
    email,
    region
)
VALUES
    ('Alice', 'alice@example.com', 'LATAM'),
    ('Jupiter', 'jupiter@example.com', 'North America');


INSERT INTO public.customers (
    customer_id,
    customer_name,
    tax_id,
    segment,
    country,
    collector_id
)
VALUES
    ('CUST0001', 'Acme Corp', '12.345.678/0001-99', 'Retail', 'Brazil', 1),
    ('CUST0002', 'Globex Inc', '98.765.432/0001-11', 'Manufacturing', 'USA', 2);


INSERT INTO public.currency (
    date,
    currency_code,
    usd_rate
)
VALUES
    ('2026-01-10', 'USD', 1.000000),
    ('2026-01-10', 'EUR', 1.080000),
    ('2026-01-10', 'BRL', 0.180000);


INSERT INTO public.issued_invoices (
    doc_number,
    customer_id,
    contract_number,
    issue_date,
    due_date,
    amount,
    currency_code,
    description,
    document_type
)
VALUES
    (
        'INV-1001',
        'CUST0001',
        'CTR-001',
        '2026-01-10',
        '2026-02-10',
        15000.00,
        'BRL',
        'January leasing invoice',
        'INVOICE'
    ),
    (
        'INV-1002',
        'CUST0002',
        'CTR-002',
        '2026-01-10',
        '2026-02-15',
        8000.00,
        'EUR',
        'Industrial equipment lease',
        'INVOICE'
    );