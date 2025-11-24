import pandas as pd
import numpy as np
from datetime import datetime

def calculate_aging(df, reference_date=None):
    # reference date as datetime.date
    if reference_date is None:
        reference_date = datetime.today().date()

    # calculate days overdue
    df['days_overdue'] = (reference_date - df['due_date']).dt.days

    conditions = [
        df['days_overdue'] < 0,
        df['days_overdue'] <= 30,
        df['days_overdue'] <= 60,
        df['days_overdue'] <= 90,
        df['days_overdue'] <= 180,
        df['days_overdue'] <= 365
    ]

    labels = [
        "Not due",
        "0-30",
        "31-60",
        "61-90",
        "91-180",
        "181-365"
    ]

    # creates aging_group column with group labels according to the days overdue conditions
    df['aging_group'] = np.select(conditions, labels, default="Unknown")
    return df

