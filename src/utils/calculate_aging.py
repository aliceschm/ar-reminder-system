import pandas as pd
import numpy as np
from datetime import datetime

def calculate_aging(df, reference_date=None):
    # if reference_date is None, use today
    if reference_date is None:
        reference_date = pd.Timestamp.today()
    else:
        reference_date = pd.Timestamp(reference_date)

    # ensure due_date is datetime
    df['due_date'] = pd.to_datetime(df['due_date'])

    # calculate days overdue
    df['days_overdue'] = (reference_date - df['due_date']).dt.days

    # define the bins for aging groups
    bins = [-np.inf, -1, 30, 60, 90, 180, 365, np.inf]
    labels = ["Not due", "0-30", "31-60", "61-90", "91-180", "181-365", "Over 365"]

    # creates aging_group column using pd.cut to categorize the days_overdue into aging groups
    df['aging_group'] = pd.cut(df['days_overdue'], bins=bins, labels=labels)

    return df
