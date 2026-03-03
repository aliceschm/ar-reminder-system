from sqlalchemy import text
from src.config.db import engine
import pandas as pd

# function to return usd_rate per country currency_code, used to transform invoice original amounts to USD in open AR
def get_currency():
    """Fetch latest usd_rate for each currency_code and return as dict {currency_code: usd_rate}"""
    query = """
        SELECT DISTINCT ON (currency_code)
            currency_code,
            usd_rate
        FROM public.currency
        ORDER BY currency_code, date DESC
    """
    df = pd.read_sql_query(text(query), engine)
    return dict(zip(df['currency_code'], df['usd_rate']))
