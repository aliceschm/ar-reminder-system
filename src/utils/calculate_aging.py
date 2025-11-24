import pandas as pd
import numpy as np
from datetime import datetime

# returns the aging group for a given due date.
# aging groups:
#     - Not due
#     - 0-30
#     - 31-60
#     - 61-90
#     - 91-180
#     - 181-365
#     - >365

def calculate_aging(due_date, reference_date=None):
    if reference_date is None:
        reference_date = datetime.today()

    days_overdue = (reference_date.date() - due_date).days

    if days_overdue < 0:
        return "Not due"
    elif days_overdue <= 30:
        return "0-30"
    elif days_overdue <= 60:
        return "31-60"
    elif days_overdue <= 90:
        return "61-90"
    elif days_overdue <= 180:
        return "91-180"
    elif days_overdue <= 365:
        return "181-365"
    else:
        return ">365"

