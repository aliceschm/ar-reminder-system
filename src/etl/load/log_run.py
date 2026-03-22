from sqlalchemy import text
from src.config.db import engine  # postgres connection

# insert a log entry in the process_runs table.
def log_run(process_name, info):
    """Insert a log entry into process_runs table with process_name, current timestamp, and info message"""
    query = """
    INSERT INTO public.process_runs (process_name, last_updt_time, info)
    VALUES (:process_name, now(), :info)
    """

    # begin a transaction, automatically commit if successful or rollback on error
    with engine.begin() as connection:
        connection.execute(text(query), {"process_name": process_name, "info": info})
