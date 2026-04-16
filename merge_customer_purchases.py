def merge_group_sort(transactions_df, customers_df):
    merged_df = transactions_df.merge(customers_df, on="Customer_ID", how="left")

    grouped = merged_df.groupby("Segment", as_index=False)["Amount"].sum()
    grouped.rename(columns={"Amount": "Total_Amount"}, inplace=True)

    grouped = grouped.sort_values(
        by=["Total_Amount", "Segment"],
        ascending=[False, True]
    ).reset_index(drop=True)

    top4 = grouped.head(4)
    return [[row["Segment"], int(row["Total_Amount"])] for _, row in top4.iterrows()]
