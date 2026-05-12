from etl.transform.aging import calculate_aging


def transform_invoices(df_invoices, currency_rates, collectors_map):
    """Transform issued invoices and split rows that cannot be completed safely."""
    df = df_invoices.copy()

    df["usd_rate"] = df["currency_code"].map(currency_rates)
    rejected = df[df["usd_rate"].isna()].copy()
    rejected["rejection_stage"] = "currency_lookup"
    rejected["rejection_reason"] = rejected["currency_code"].map(
        lambda code: f"Missing USD currency rate for '{code}'"
    )

    df = df[df["usd_rate"].notna()].copy()

    # create new columns
    df["total_amount"] = df["amount"]
    df["balance_amount"] = df["amount"]
    df["status"] = "OPEN"
    df["comment"] = None

    # convert amounts to USD and create usd columns
    df["amount_usd"] = df["amount"] * df["usd_rate"]
    df["balance_amount_usd"] = df["balance_amount"] * df["usd_rate"]

    # calculate aging
    df = calculate_aging(df)

    # add collector column
    df["collector"] = df["customer_id"].map(collectors_map).fillna("Unassigned")

    transformed = df[
        [
            "doc_number",
            "customer_id",
            "document_type",
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

    rejected = rejected[
        [
            "doc_number",
            "customer_id",
            "document_type",
            "contract_number",
            "issue_date",
            "due_date",
            "amount",
            "currency_code",
            "rejection_stage",
            "rejection_reason",
            "created_at",
        ]
    ]

    return transformed, rejected
