
from sqlalchemy import text
from src.config.db import engine  # postgres connection

# returns the most recent execution timestamp for a specified process.
def get_last_run_time(process_name):
    """Fetch the most recent last_updt_time for the given process_name from cntrl_logs table, return as string 'YYYY-MM-DD'"""
    query = """
    SELECT MAX(last_updt_time) AS last_run_time
    FROM public.cntrl_logs
    WHERE process_name = :process_name
    """
    
    with engine.connect() as connection:
        result = connection.execute(text(query), {"process_name": process_name}).fetchone()
        if result is None or result.last_run_time is None:
            return "1970-01-01"
    return result.last_run_time
