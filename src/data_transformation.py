from pyspark.sql.functions import *

def transform_co2_data(df):

    df_clean = (
        df
        .drop("FLIGHT_MONTH", "NOTE", "YEAR_SOURCE")
        .withColumnRenamed("TF", "FLIGHTS")
        .withColumn("STATE_NAME_CLEAN", upper(trim(regexp_replace(col("STATE_NAME"), " ", ""))))
        .withColumn("STATE_CODE", regexp_replace(col("STATE_CODE"), " ", ""))
    )

    df_mapped = df_clean.withColumn(
        "STATE_NAME",
        when(col("STATE_NAME_CLEAN") == "BOSNIAANDHERZEGOVINA", "BOSNIA AND HERZEGOVINA")
        .when(col("STATE_NAME_CLEAN") == "NORTHMACEDONIA", "NORTH MACEDONIA")
        .when(col("STATE_NAME_CLEAN") == "TÜRKIYE", "TURKEY")
        .when(col("STATE_NAME_CLEAN") == "MOLDOVA,REPUBLICOF", "MOLDOVA")
        .when(col("STATE_NAME_CLEAN") == "UNITEDKINGDOM", "UNITED KINGDOM")
        .otherwise(col("STATE_NAME_CLEAN"))
    )

    df_final = (
        df_mapped
        .withColumn("CO2_QTY_TONNES", col("CO2_QTY_TONNES").cast("long"))
        .withColumn("DATE", make_date(col("YEAR"), col("MONTH"), lit(1)))
        .drop("STATE_NAME_CLEAN")
    )

    return df_final