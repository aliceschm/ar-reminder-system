from etl.extract.process_log import get_last_run_time
from etl.extract.invoices import get_new_invoices
from etl.extract.currency import get_currency_rates
from etl.extract.collectors import get_collectors_map

from etl.transform.invoices import transform_invoices

from etl.load.open_ar import insert_open_ar
from etl.load.log_run import log_run


PROCESS_NAME = "build_open_ar"


def build_open_ar():
    """Main procedure to orchestrate updating open_ar with new invoices from issued_invoices"""
    last_run = get_last_run_time(PROCESS_NAME)
    new_invoices = get_new_invoices(last_run)

    if new_invoices.empty:
        log_run(PROCESS_NAME, "0 invoices inserted")
        return

    currency_rates = get_currency_rates()
    collectors_map = get_collectors_map()

    df_transformed = transform_invoices(
        new_invoices,
        currency_rates,
        collectors_map,
    )

    count_processed = len(df_transformed)
    info = f"{count_processed} new invoices inserted"

    insert_open_ar(df_transformed)
    log_run(PROCESS_NAME, info)


if __name__ == "__main__":
    build_open_ar()