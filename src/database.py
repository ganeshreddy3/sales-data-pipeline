"""
database.py

Database connection module.
"""

from sqlalchemy import create_engine

from config.config import (
    DB_USERNAME,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME
)


def get_database_engine():

    database_url = (
        f"postgresql://"
        f"{DB_USERNAME}:"
        f"{DB_PASSWORD}@"
        f"{DB_HOST}:"
        f"{DB_PORT}/"
        f"{DB_NAME}"
    )

    engine = create_engine(
        database_url
    )

    return engine
