from sqlalchemy import text
from src.config.db import engine
import pandas as pd

def get_collector():
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
    return dict(zip(df['customer_id'], df['collector_name']))
