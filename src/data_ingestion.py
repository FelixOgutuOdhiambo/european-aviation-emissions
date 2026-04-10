import pandas as pd

CO2_BASE_URL = "https://www.eurocontrol.int/performance/data/download/csv"

def load_co2_data(spark, start_year, end_year):
    combined_df = None

    for year in range(start_year, end_year + 1):
        file_url = f"{CO2_BASE_URL}/co2_emmissions_by_state_{year}.csv"

        try:
            pdf = pd.read_csv(file_url)

            if "FLIGHT_MONTH" not in pdf.columns:
                pdf["FLIGHT_MONTH"] = None

            pdf["YEAR_SOURCE"] = year

            spark_df = spark.createDataFrame(pdf)

            combined_df = (
                spark_df if combined_df is None
                else combined_df.unionByName(spark_df, allowMissingColumns=True)
            )

            print(f"Loaded {year}")

        except Exception as e:
            print(f"Failed {year}: {e}")

    return combined_df