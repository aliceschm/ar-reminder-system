from sqlalchemy import text
from src.config.db import engine
import pandas as pd

# function to return usd_rate per country currency_code, used to transform invoice original amounts to USD in open AR
def get_currency():
    query = """
        SELECT DISTINCT ON (currency_code) -- returns only the latest currency rate per code
            currency_code,
            usd_rate,
            date
        FROM public.currency
        ORDER BY currency_code, date DESC
    """
    return pd.read_sql_query(text(query), engine)
