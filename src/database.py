"""
database.py

Database connection module.
"""

from sqlalchemy import create_engine


def get_database_engine():

    username = "postgres"

    password = "postgres"

    host = "localhost"

    port = "5432"

    database = "sales_db"

    database_url = (
        f"postgresql://"
        f"{username}:"
        f"{password}@"
        f"{host}:"
        f"{port}/"
        f"{database}"
    )

    engine = create_engine(
        database_url
    )

    return engine
