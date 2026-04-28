import requests
import pandas as pd
import sqlite3
import logging
from datetime import datetime
import config

# ----------------------------
# Logging setup
# ----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ----------------------------
# Extract
# ----------------------------
def extract(api_url):
    logging.info("Starting data extraction")

    response = requests.get(api_url)
    response.raise_for_status()

    data = response.json()

    logging.info(f"Extracted {len(data)} records")

    return data

# ----------------------------
# Transform
# ----------------------------
def transform(data):
    logging.info("Starting transformation")

    df = pd.DataFrame(data)

    df = df[["id", "title", "price", "category"]]
    df["price"] = df["price"].astype(float)

    df["price_category"] = df["price"].apply(
        lambda x: "expensive" if x > 100 else "cheap"
    )

    df["loaded_at"] = datetime.utcnow()

    logging.info("Transformation completed")

    return df

# ----------------------------
# Load
# ----------------------------
def load(df, db_name):
    logging.info("Loading data into database")

    conn = sqlite3.connect(db_name)

    # RAW layer
    df[["id", "title", "price", "category", "loaded_at"]] \
        .to_sql("products_raw", conn, if_exists="append", index=False)

    # CLEAN layer
    df.to_sql("products_clean", conn, if_exists="append", index=False)

    conn.close()

    logging.info("Data loaded successfully")

# ----------------------------
# Analytics 
# ----------------------------
def run_analytics(db_name):
    logging.info("Running analytics queries")

    conn = sqlite3.connect(db_name)

    query = """
    SELECT category, AVG(price) as avg_price
    FROM products_clean
    GROUP BY category
    ORDER BY avg_price DESC
    """

    result = pd.read_sql(query, conn)

    logging.info("Analytics result:")
    print(result)

    conn.close()

# ----------------------------
# Pipeline runner
# ----------------------------
def run_pipeline():
    try:
        logging.info("ETL pipeline started")

        data = extract(config.API_URL)
        df = transform(data)
        load(df, config.DB_NAME)
        run_analytics(config.DB_NAME)

        logging.info("ETL pipeline finished successfully")

    except Exception as e:
        logging.error(f"Pipeline failed: {e}")


if __name__ == "__main__":
    run_pipeline()
