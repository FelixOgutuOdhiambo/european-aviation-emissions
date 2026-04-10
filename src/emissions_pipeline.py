from data_ingestion import load_co2_data
from data_transformation import transform_co2_data
from data_enrichment import fetch_country_data, enrich_co2_data
from data_storage import write_to_lakehouse

START_YEAR = 2010
END_YEAR = 2025
TABLE_NAME = "EU_co2_emissions"

def run_pipeline(spark):

    print("Starting pipeline...")

    co2_raw = load_co2_data(spark, START_YEAR, END_YEAR)

    co2_clean = transform_co2_data(co2_raw)

    geo_df = fetch_country_data(spark)

    enriched_df = enrich_co2_data(co2_clean, geo_df)

    write_to_lakehouse(enriched_df, TABLE_NAME)

    print("Pipeline completed successfully")


# Entry point
if __name__ == "__main__":
    print("Run inside Spark environment")