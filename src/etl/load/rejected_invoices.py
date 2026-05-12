from sqlalchemy import text

from config.db import engine


def insert_rejected_invoices(df):
    """Persist invoices rejected during transformation and return inserted row count."""
    if df.empty:
        return 0

    query = """
    INSERT INTO public.rejected_invoices (
        doc_number,
        customer_id,
        document_type,
        contract_number,
        issue_date,
        due_date,
        amount,
        currency_code,
        rejection_stage,
        rejection_reason,
        created_at
    ) VALUES (
        :doc_number,
        :customer_id,
        :document_type,
        :contract_number,
        :issue_date,
        :due_date,
        :amount,
        :currency_code,
        :rejection_stage,
        :rejection_reason,
        :created_at
    )
    """

    with engine.begin() as connection:
        result = connection.execute(text(query), df.to_dict(orient="records"))
        return result.rowcount or 0
