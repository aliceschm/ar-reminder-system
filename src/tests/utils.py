
from src.utils.get_last_run_time import get_last_run_time
from src.utils.get_currency import get_currency
from src.utils.get_collector import get_collector

def test_get_last_run_time():
    result = get_last_run_time('update_invoices')
    print(result)

#test_get_last_run_time()

def test_get_currency():
    result = get_currency()
    print(result)

#test_get_currency()

def test_get_collector():
    result = get_collector()
    print(result)

#test_get_collector()