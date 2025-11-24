from sqlalchemy import text
from src.config.db import engine
import pandas as pd

def get_collector():
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
