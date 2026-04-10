import requests
import pandas as pd
from pyspark.sql.functions import *

COUNTRIES_API_URL = "https://restcountries.com/v3.1/all?fields=name,cca2,cca3,region,subregion,latlng,population"

def fetch_country_data(spark):
    response = requests.get(COUNTRIES_API_URL)
    data = response.json()

    records = [
        {
            "COUNTRY": c.get("name", {}).get("common"),
            "ISO2": c.get("cca2"),
            "REGION": c.get("region"),
            "SUBREGION": c.get("subregion"),
            "LATITUDE": (c.get("latlng") or [None, None])[0],
            "LONGITUDE": (c.get("latlng") or [None, None])[1],
            "POPULATION": c.get("population")
        }
        for c in data if isinstance(c, dict)
    ]

    return (
        spark.createDataFrame(pd.DataFrame(records))
        .withColumn("COUNTRY", upper(trim(col("COUNTRY"))))
    )

def enrich_co2_data(co2_df, geo_df):
    return co2_df.join(
        geo_df,
        co2_df["STATE_NAME"] == geo_df["COUNTRY"],
        "left"
    )