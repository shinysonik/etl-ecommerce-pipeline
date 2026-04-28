# ETL E-commerce Data Pipeline

## Overview

This project implements a simple yet structured ETL (Extract–Transform–Load) pipeline for ingesting and processing product data from a public API. The pipeline demonstrates core data engineering concepts including data ingestion, transformation, storage, and analytical querying.

The goal of the project is to showcase practical skills in Python, SQL, and data pipeline design aligned with typical entry-level data engineering requirements.

---

## Architecture

The pipeline consists of three main stages:

* **Extract**
  Data is retrieved from an external REST API.

* **Transform**
  Raw data is cleaned, validated, and enriched with additional attributes.

* **Load**
  Data is stored in a relational database with separation between raw and processed layers.

---

## Data Model

The project follows a simplified layered approach:

* **`products_raw`**
  Stores ingested data in its original structure with a load timestamp.
  Enables traceability and historical tracking.

* **`products_clean`**
  Stores transformed and enriched data ready for analysis.

This separation reflects common practices in data engineering pipelines.

---

## Tech Stack

* Python
* pandas
* requests
* SQLite
* SQL

---

## Key Features

* Modular pipeline design (separation of concerns)
* Incremental data loading (append-only strategy)
* Basic data enrichment (derived columns)
* Logging for pipeline execution
* SQL-based analytical queries
* Use of window functions and joins

---

## SQL Capabilities Demonstrated

The project includes example queries covering:

* Aggregations (`GROUP BY`)
* Sorting (`ORDER BY`)
* Joins between tables
* Window functions (`OVER PARTITION BY`)

These are provided in the `sql/analytics.sql` file.

---

## Project Structure

```
etl-ecommerce-pipeline/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   ├── db.py
│   └── main.py
│
├── sql/
│   ├── create_tables.sql
│   └── analytics.sql
│
├── config.py
├── requirements.txt
└── README.md
```

---

## How to Run

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run the pipeline:

```
python src/main.py
```

---

## What This Project Demonstrates

* Understanding of ETL pipeline design
* Ability to work with APIs and structured data
* Practical SQL skills including joins and window functions
* Basic data modeling concepts
* Writing maintainable and modular Python code

---

## Future Improvements

* Migration to PostgreSQL
* Containerization with Docker
* Scheduling (e.g., cron or orchestration tools)
* Data validation and testing layer
* Incremental loading based on change tracking

---

## Author

This project was created as part of a data engineering learning path and portfolio development.
