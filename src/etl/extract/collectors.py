import pandas as pd
from sqlalchemy import text
from src.config.db import engine


def get_collectors_map():
    """Fetch collector names for each customer_id and return as dict {customer_id: collector_name}"""
    query = """
        SELECT
            cust.customer_id,
            col.collector_name
        FROM public.customers cust
        LEFT JOIN public.collectors col
            ON cust.collector_id = col.collector_id
    """
    
    df = pd.read_sql_query(text(query), engine)
    print('Extract collectors Successful')
    return dict(zip(df['customer_id'], df['collector_name']))


