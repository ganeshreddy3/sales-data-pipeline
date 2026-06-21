"""
config.py

Project configuration.
"""

DB_USERNAME = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "sales_db"

INPUT_FILE = "data/raw/sales.csv"
OUTPUT_FILE = "data/processed/clean_sales.csv"

LOG_FILE = "logs/pipeline.log"
