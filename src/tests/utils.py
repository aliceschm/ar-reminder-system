
from src.etl.extract.process_log import get_last_run_time
from src.etl.extract.currency import get_currency
from src.etl.extract.collectors import get_collector

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