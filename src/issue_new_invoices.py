import argparse
from datetime import date, timedelta
from itertools import cycle
from uuid import uuid4

from sqlalchemy import text

from config.db import engine


def parse_args():
    parser = argparse.ArgumentParser(
        description="Insert fresh issued invoices so the incremental pipeline can run again."
    )
    parser.add_argument(
        "--count",
        type=int,
        default=5,
        help="Number of invoices to issue. Default: 5.",
    )
    parser.add_argument(
        "--document-type",
        default="INVOICE",
        help="Document type stored with the new invoices. Default: INVOICE.",
    )
    return parser.parse_args()


def get_seed_values():
    customers_query = """
    SELECT customer_id
    FROM public.customers
    ORDER BY customer_id
    """
    currencies_query = """
    SELECT DISTINCT currency_code
    FROM public.currency
    ORDER BY currency_code
    """

    with engine.connect() as connection:
        customers = [row.customer_id for row in connection.execute(text(customers_query))]
        currencies = [row.currency_code for row in connection.execute(text(currencies_query))]

    if not customers:
        raise RuntimeError("No customers found. Seed or create customers before issuing invoices.")
    if not currencies:
        raise RuntimeError("No currencies found. Seed or create currency rates before issuing invoices.")

    return customers, currencies


def build_invoice_rows(count, document_type):
    customers, currencies = get_seed_values()
    today = date.today()
    due_date = today + timedelta(days=30)
    customer_cycle = cycle(customers)
    currency_cycle = cycle(currencies)

    rows = []
    for index in range(1, count + 1):
        token = uuid4().hex[:10].upper()
        rows.append(
            {
                "doc_number": f"INV-AUTO-{token}",
                "customer_id": next(customer_cycle),
                "contract_number": f"CTR-AUTO-{index:03d}",
                "issue_date": today,
                "due_date": due_date,
                "amount": 1000 + (index * 125),
                "currency_code": next(currency_cycle),
                "description": f"Auto-issued invoice batch item {index}",
                "document_type": document_type,
            }
        )

    return rows


def insert_invoices(rows):
    query = """
    INSERT INTO public.issued_invoices (
        doc_number,
        customer_id,
        contract_number,
        issue_date,
        due_date,
        amount,
        currency_code,
        description,
        document_type
    ) VALUES (
        :doc_number,
        :customer_id,
        :contract_number,
        :issue_date,
        :due_date,
        :amount,
        :currency_code,
        :description,
        :document_type
    )
    """

    with engine.begin() as connection:
        result = connection.execute(text(query), rows)
        return result.rowcount or 0


def main():
    args = parse_args()
    if args.count < 1:
        raise ValueError("--count must be at least 1.")

    rows = build_invoice_rows(args.count, args.document_type)
    inserted_count = insert_invoices(rows)

    print(f"[ISSUE] New invoices inserted: {inserted_count}")
    print("[ISSUE] Run `python src/main.py` to process them into open_ar.")


if __name__ == "__main__":
    main()
