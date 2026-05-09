from etl.transform.aging import calculate_aging


def transform_invoices(df_invoices, currency_rates, collectors_map):
    """Transform issued_invoices df to match open_ar structure and add necessary columns"""
    df = df_invoices.copy()

    # create new columns
    df["total_amount"] = df["amount"]
    df["balance_amount"] = df["amount"]
    df["status"] = "OPEN"
    df["comment"] = None

    # convert amounts to USD and create usd columns
    df["usd_rate"] = df["currency_code"].map(currency_rates)
    df["amount_usd"] = df["amount"] * df["usd_rate"]
    df["balance_amount_usd"] = df["balance_amount"] * df["usd_rate"]

    # calculate aging
    df = calculate_aging(df)

    # add collector column
    df["collector"] = df["customer_id"].map(collectors_map).fillna("Unassigned")

    return df[
        [
            "doc_number",
            "customer_id",
            "contract_number",
            "issue_date",
            "due_date",
            "total_amount",
            "balance_amount",
            "amount_usd",
            "balance_amount_usd",
            "aging_group",
            "status",
            "comment",
            "created_at",
            "collector",
        ]
    ]