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
    ('CUST0002', 'Globex Inc', '98.765.432/0001-11', 'Manufacturing', 'USA', 2),
    ('CUST0003', 'No Collector LLC', '11.222.333/0001-44', 'Services', 'Canada', NULL);


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
    ),
    (
        'INV-1003',
        'CUST0003',
        'CTR-003',
        '2026-01-10',
        '2026-02-20',
        4200.00,
        'USD',
        'Valid currency with missing collector assignment',
        'INVOICE'
    ),
    (
        'INV-1004',
        'CUST0001',
        'CTR-004',
        '2026-01-10',
        '2026-02-25',
        9100.00,
        'CAD',
        'Unsupported currency used to test rejected invoices',
        'INVOICE'
    ),
    ('INV-1005', 'CUST0001', 'CTR-005', '2026-01-11', '2026-02-10', 1250.00, 'USD', 'Monthly service invoice', 'INVOICE'),
    ('INV-1006', 'CUST0002', 'CTR-006', '2026-01-12', '2026-02-11', 2325.50, 'EUR', 'Equipment rental invoice', 'INVOICE'),
    ('INV-1007', 'CUST0003', 'CTR-007', '2026-01-13', '2026-02-12', 1780.00, 'BRL', 'Collector assignment check invoice', 'INVOICE'),
    ('INV-1008', 'CUST0001', 'CTR-008', '2026-01-14', '2026-02-13', 6400.00, 'USD', 'Quarterly maintenance invoice', 'INVOICE'),
    ('INV-1009', 'CUST0002', 'CTR-009', '2026-01-15', '2026-02-14', 3150.75, 'EUR', 'Parts replacement invoice', 'INVOICE'),
    ('INV-1010', 'CUST0001', 'CTR-010', '2026-01-16', '2026-02-15', 2220.00, 'JPY', 'Unsupported currency rejection sample', 'INVOICE'),
    ('INV-1011', 'CUST0003', 'CTR-011', '2026-01-17', '2026-02-16', 4890.00, 'USD', 'Unassigned collector recurring invoice', 'INVOICE'),
    ('INV-1012', 'CUST0002', 'CTR-012', '2026-01-18', '2026-02-17', 5120.00, 'BRL', 'Regional services invoice', 'INVOICE'),
    ('INV-1013', 'CUST0001', 'CTR-013', '2026-01-19', '2026-02-18', 7600.00, 'EUR', 'Lease adjustment invoice', 'INVOICE'),
    ('INV-1014', 'CUST0002', 'CTR-014', '2026-01-20', '2026-02-19', 2890.00, 'USD', 'Support package invoice', 'INVOICE'),
    ('INV-1015', 'CUST0003', 'CTR-015', '2026-01-21', '2026-02-20', 1980.00, 'BRL', 'Collector review sample', 'INVOICE'),
    ('INV-1016', 'CUST0001', 'CTR-016', '2026-01-22', '2026-02-21', 8425.00, 'USD', 'Annual licensing invoice', 'INVOICE'),
    ('INV-1017', 'CUST0002', 'CTR-017', '2026-01-23', '2026-02-22', 3650.00, 'CAD', 'Unsupported currency rejection sample', 'INVOICE'),
    ('INV-1018', 'CUST0001', 'CTR-018', '2026-01-24', '2026-02-23', 4510.00, 'EUR', 'Implementation invoice', 'INVOICE'),
    ('INV-1019', 'CUST0003', 'CTR-019', '2026-01-25', '2026-02-24', 2740.00, 'USD', 'Collector assignment exception invoice', 'INVOICE'),
    ('INV-1020', 'CUST0002', 'CTR-020', '2026-01-26', '2026-02-25', 6300.00, 'BRL', 'Manufacturing support invoice', 'INVOICE'),
    ('INV-1021', 'CUST0001', 'CTR-021', '2026-01-27', '2026-02-26', 915.00, 'USD', 'Small balance invoice', 'INVOICE'),
    ('INV-1022', 'CUST0002', 'CTR-022', '2026-01-28', '2026-02-27', 7100.00, 'EUR', 'Large contract invoice', 'INVOICE'),
    ('INV-1023', 'CUST0003', 'CTR-023', '2026-01-29', '2026-02-28', 3325.00, 'BRL', 'Unassigned collector service invoice', 'INVOICE'),
    ('INV-1024', 'CUST0001', 'CTR-024', '2026-01-30', '2026-03-01', 2675.00, 'USD', 'Month-end recurring invoice', 'INVOICE'),
    ('INV-1025', 'CUST0002', 'CTR-025', '2026-01-31', '2026-03-02', 4010.00, 'GBP', 'Unsupported currency rejection sample', 'INVOICE'),
    ('INV-1026', 'CUST0001', 'CTR-026', '2026-02-01', '2026-03-03', 5580.00, 'EUR', 'Expansion project invoice', 'INVOICE'),
    ('INV-1027', 'CUST0003', 'CTR-027', '2026-02-02', '2026-03-04', 1895.00, 'USD', 'Collector exception follow-up invoice', 'INVOICE'),
    ('INV-1028', 'CUST0002', 'CTR-028', '2026-02-03', '2026-03-05', 9475.00, 'BRL', 'Capital equipment invoice', 'INVOICE'),
    ('INV-1029', 'CUST0001', 'CTR-029', '2026-02-04', '2026-03-06', 1180.00, 'USD', 'Subscription adjustment invoice', 'INVOICE'),
    ('INV-1030', 'CUST0002', 'CTR-030', '2026-02-05', '2026-03-07', 6800.00, 'EUR', 'Transport services invoice', 'INVOICE'),
    ('INV-1031', 'CUST0003', 'CTR-031', '2026-02-06', '2026-03-08', 2450.00, 'BRL', 'Collector gap validation invoice', 'INVOICE'),
    ('INV-1032', 'CUST0001', 'CTR-032', '2026-02-07', '2026-03-09', 7990.00, 'USD', 'Upgrade services invoice', 'INVOICE'),
    ('INV-1033', 'CUST0002', 'CTR-033', '2026-02-08', '2026-03-10', 1560.00, 'AUD', 'Unsupported currency rejection sample', 'INVOICE'),
    ('INV-1034', 'CUST0001', 'CTR-034', '2026-02-09', '2026-03-11', 3860.00, 'EUR', 'Consulting package invoice', 'INVOICE'),
    ('INV-1035', 'CUST0003', 'CTR-035', '2026-02-10', '2026-03-12', 4720.00, 'USD', 'Collector assignment control invoice', 'INVOICE'),
    ('INV-1036', 'CUST0002', 'CTR-036', '2026-02-11', '2026-03-13', 5290.00, 'BRL', 'Renewal charge invoice', 'INVOICE'),
    ('INV-1037', 'CUST0001', 'CTR-037', '2026-02-12', '2026-03-14', 2140.00, 'USD', 'Usage fee invoice', 'INVOICE'),
    ('INV-1038', 'CUST0002', 'CTR-038', '2026-02-13', '2026-03-15', 6440.00, 'EUR', 'Regional contract invoice', 'INVOICE'),
    ('INV-1039', 'CUST0003', 'CTR-039', '2026-02-14', '2026-03-16', 3580.00, 'BRL', 'Missing collector validation invoice', 'INVOICE'),
    ('INV-1040', 'CUST0001', 'CTR-040', '2026-02-15', '2026-03-17', 9050.00, 'USD', 'Premium service invoice', 'INVOICE'),
    ('INV-1041', 'CUST0002', 'CTR-041', '2026-02-16', '2026-03-18', 2980.00, 'MXN', 'Unsupported currency rejection sample', 'INVOICE'),
    ('INV-1042', 'CUST0001', 'CTR-042', '2026-02-17', '2026-03-19', 4875.00, 'EUR', 'Contract milestone invoice', 'INVOICE'),
    ('INV-1043', 'CUST0003', 'CTR-043', '2026-02-18', '2026-03-20', 2670.00, 'USD', 'Unassigned collector invoice sample', 'INVOICE'),
    ('INV-1044', 'CUST0002', 'CTR-044', '2026-02-19', '2026-03-21', 7440.00, 'BRL', 'Supply chain services invoice', 'INVOICE'),
    ('INV-1045', 'CUST0001', 'CTR-045', '2026-02-20', '2026-03-22', 1320.00, 'USD', 'Late cycle service invoice', 'INVOICE'),
    ('INV-1046', 'CUST0002', 'CTR-046', '2026-02-21', '2026-03-23', 8210.00, 'EUR', 'Enterprise renewal invoice', 'INVOICE'),
    ('INV-1047', 'CUST0003', 'CTR-047', '2026-02-22', '2026-03-24', 3090.00, 'BRL', 'Collector assignment audit invoice', 'INVOICE'),
    ('INV-1048', 'CUST0001', 'CTR-048', '2026-02-23', '2026-03-25', 5560.00, 'USD', 'Operational services invoice', 'INVOICE'),
    ('INV-1049', 'CUST0002', 'CTR-049', '2026-02-24', '2026-03-26', 4700.00, 'CHF', 'Unsupported currency rejection sample', 'INVOICE'),
    ('INV-1050', 'CUST0003', 'CTR-050', '2026-02-25', '2026-03-27', 3925.00, 'EUR', 'Collector assignment final sample', 'INVOICE');
