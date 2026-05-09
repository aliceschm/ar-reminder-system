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
    try:
        print("=" * 50)
        print("OPEN AR PIPELINE")
        print("=" * 50)
        print()
        print("[START] Pipeline execution started")
        print()

        last_run = get_last_run_time(PROCESS_NAME)
        if str(last_run) == "1970-01-01":
            print("[INFO] Last run: first execution")
        else:
            print(f"[INFO] Last run: {last_run}")

        new_invoices = get_new_invoices(last_run)
        print(f"[INFO] New invoices found: {len(new_invoices)}")
        print()

        if new_invoices.empty:
            print("[INFO] No new invoices found. Nothing to insert into open_ar.")
            print()
            log_run(PROCESS_NAME, "0 invoices inserted")
            print("[SUCCESS] Process run logged")
            print("[END] Pipeline finished successfully")
            print()
            print("=" * 50)
            return

        currency_rates = get_currency_rates()
        print(f"[EXTRACT] Currency rates loaded: {len(currency_rates)}")

        collectors_map = get_collectors_map()
        print(f"[EXTRACT] Collectors loaded: {len(collectors_map)}")
        print()

        df_transformed = transform_invoices(
            new_invoices,
            currency_rates,
            collectors_map,
        )
        print(f"[TRANSFORM] Invoices transformed: {len(df_transformed)}")
        print()

        count_processed = len(df_transformed)
        info = f"{count_processed} new invoices inserted"

        insert_open_ar(df_transformed)
        print(f"[LOAD] Open AR updated: {count_processed} rows inserted")
        print()

        log_run(PROCESS_NAME, info)
        print("[SUCCESS] Process run logged")
        print("[END] Pipeline finished successfully")
        print()
        print("=" * 50)
    except Exception as e:
        print(f"[ERROR] Pipeline failed: {e}")
        raise


if __name__ == "__main__":
    build_open_ar()
