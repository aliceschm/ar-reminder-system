from etl.extract.process_log import get_last_run_time
from etl.extract.invoices import get_new_invoices
from etl.extract.currency import get_currency_rates
from etl.extract.collectors import get_collectors_map

from etl.transform.invoices import transform_invoices

from etl.load.open_ar import insert_open_ar
from etl.load.rejected_invoices import insert_rejected_invoices
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
            log_run(PROCESS_NAME, "0 invoices inserted; 0 invoices rejected")
            print("[SUCCESS] Process run logged")
            print("[END] Pipeline finished successfully")
            print()
            print("=" * 50)
            return

        currency_rates = get_currency_rates()
        collectors_map = get_collectors_map()

        df_transformed, df_rejected = transform_invoices(
            new_invoices,
            currency_rates,
            collectors_map,
        )
        print(f"[TRANSFORM] Invoices transformed: {len(df_transformed)}")
        print(f"[TRANSFORM] Invoices rejected: {len(df_rejected)}")
        print()

        inserted_count = insert_open_ar(df_transformed)
        rejected_count = insert_rejected_invoices(df_rejected)

        missing_currency_codes = sorted(
            set(new_invoices["currency_code"]) - set(currency_rates.keys())
        )
        all_currency_found = not missing_currency_codes
        collector_assignments = new_invoices["customer_id"].map(collectors_map)
        missing_collector_customers = sorted(
            set(new_invoices.loc[collector_assignments.isna(), "customer_id"])
        )
        all_collectors_assigned = not missing_collector_customers

        print(
            "[CHECK] Currency found for all invoice currencies: "
            f"{'YES' if all_currency_found else 'NO'}"
        )
        if missing_currency_codes:
            print(f"[CHECK] Missing currency codes: {', '.join(missing_currency_codes)}")

        print(
            "[CHECK] All collectors assigned correctly: "
            f"{'YES' if all_collectors_assigned else 'NO'}"
        )
        if missing_collector_customers:
            print(
                "[CHECK] Customers without collectors: "
                f"{', '.join(missing_collector_customers)}"
            )
        print()

        print(f"[LOAD] Open AR updated: {inserted_count} rows inserted")
        print(f"[LOAD] Rejected invoices stored: {rejected_count} rows inserted")
        print()

        info = (
            f"{inserted_count} invoices inserted; "
            f"{rejected_count} invoices rejected; "
            f"currency_complete={'yes' if all_currency_found else 'no'}; "
            f"collectors_complete={'yes' if all_collectors_assigned else 'no'}"
        )
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
