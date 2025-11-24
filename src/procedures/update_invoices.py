import pandas as pd
import numpy as np
from sqlalchemy import text
from src.config.db import engine  # postgres connection
from src.utils.get_last_run_time import get_last_run_time
from src.utils.log_run import log_run
from src.utils.calculate_aging import calculate_aging
from src.utils.get_currency import get_currency

PROCESS_NAME = "update_invoices"
   

def get_new_invoices(last_run_time):
    query = """
    SELECT *
    FROM public.issued_invoices
    WHERE created_at > :last_run_time
    """
    df = pd.read_sql_query(text(query), engine, params={'last_run_time': last_run_time})
    return df

def transform_invoices(df_invoices):
    # transform to Open AR df
    df = df_invoices.copy()
    
    df_currency = get_currency()

    #merge with df_currency to get currency per invoice
    df = df.merge(
    df_currency,
    how="left",
    left_on="currency",
    right_on="currency_code")

    # create new columns
    df['total_amount'] = df['amount']
    df['balance_amount'] = df['amount']
    df['status'] = "OPEN"
    df['comment'] = None
    
    # convert amounts to USD and create usd columns
    df["amount_usd"] = df["total_amount"] * df["usd_rate"]
    df["balance_amount_usd"] = df["balance_amount"] * df["usd_rate"]

    # calculate aging and returns df with aging_group column
    df = calculate_aging(df)

    return df[['doc_number', 'customer_id', 'contract_number',
               'issue_date', 'due_date', 'total_amount', 'balance_amount', 'amount_usd', 'balance_amount_usd',
               'aging_group', 'status', 'comment', 'created_at']]


def insert_open_ar(df):
    df_records = df.to_dict(orient="records")

    query = """
    INSERT INTO public.open_ar (
        doc_number, customer_id, contract_number,
        issue_date, due_date,
        total_amount, balance_amount, amount_usd, balance_amount_usd,
        aging_group, status, comment, created_at
    ) VALUES (
        :doc_number, :customer_id, :contract_number,
        :issue_date, :due_date,
        :total_amount, :balance_amount, :amount_usd, :balance_amount_usd,
        :aging_group, :status, :comment, :created_at
    )
    ON CONFLICT (doc_number) DO NOTHING;
    """

    with engine.begin() as connection:
        connection.execute(text(query), df_records)   # automatic executemany 



def update_invoices():
    last_run = get_last_run_time(PROCESS_NAME)
    new_invoices = get_new_invoices(last_run)

    if new_invoices.empty:
        log_run(PROCESS_NAME, "0 rows inserted")
        return

    # transform df and count
    df_transformed = transform_invoices(new_invoices)

    count_processed = len(df_transformed)
    info = f"{count_processed} new invoices inserted"

    insert_open_ar(df_transformed)

    log_run(PROCESS_NAME, info)

update_invoices()