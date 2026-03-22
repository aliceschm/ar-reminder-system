from sqlalchemy import text
from src.config.db import engine  

def insert_open_ar(df):
    """Insert transformed invoices into open_ar table, ignore duplicates based on doc_number"""
    df_records = df.to_dict(orient="records")

    query = """
    INSERT INTO public.open_ar (
        doc_number, customer_id, contract_number,
        issue_date, due_date,
        total_amount, balance_amount, amount_usd, balance_amount_usd,
        aging_group, status, comment, created_at, collector
    ) VALUES (
        :doc_number, :customer_id, :contract_number,
        :issue_date, :due_date,
        :total_amount, :balance_amount, :amount_usd, :balance_amount_usd,
        :aging_group, :status, :comment, :created_at, :collector
    )
    ON CONFLICT (doc_number) DO NOTHING;
    """

    with engine.begin() as connection:
        connection.execute(text(query), df_records)   # automatic executemany 