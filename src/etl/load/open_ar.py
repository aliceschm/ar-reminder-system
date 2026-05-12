from sqlalchemy import text
from config.db import engine  

def insert_open_ar(df):
    """Insert transformed invoices into open_ar and ignore duplicate business keys."""
    if df.empty:
        return 0

    df_records = df.to_dict(orient="records")

    query = """
    INSERT INTO public.open_ar (
        doc_number, customer_id, document_type, contract_number,
        issue_date, due_date,
        total_amount, balance_amount, amount_usd, balance_amount_usd,
        aging_group, status, comment, created_at, collector
    ) VALUES (
        :doc_number, :customer_id, :document_type, :contract_number,
        :issue_date, :due_date,
        :total_amount, :balance_amount, :amount_usd, :balance_amount_usd,
        :aging_group, :status, :comment, :created_at, :collector
    )
    ON CONFLICT (doc_number, customer_id, document_type) DO NOTHING;
    """

    with engine.begin() as connection:
        result = connection.execute(text(query), df_records)
        return result.rowcount or 0
