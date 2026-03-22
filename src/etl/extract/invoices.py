import pandas as pd
from sqlalchemy import text
from src.config.db import engine  

def get_new_invoices(last_run_time):
    """Fetch new invoices from issued_invoices table created after last_run_time"""
    query = """
    SELECT *
    FROM public.issued_invoices
    WHERE created_at > :last_run_time
    """
    df = pd.read_sql_query(text(query), engine, params={'last_run_time': last_run_time})
    return df
