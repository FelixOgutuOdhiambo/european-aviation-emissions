def write_to_lakehouse(df, table_name):

    (
        df.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(table_name)
    )

    print(f"Saved to {table_name}")