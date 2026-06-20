"""
load.py

Load cleaned data into PostgreSQL.
"""

import pandas as pd

from src.database import (
    get_database_engine
)


def load_data(
    df: pd.DataFrame,
    table_name: str = "sales"
):

    print("\n" + "=" * 50)
    print("DATA LOADING")
    print("=" * 50)

    engine = get_database_engine()

    df.to_sql(
        name=table_name,
        con=engine,
        if_exists="replace",
        index=False
    )

    print(
        "\nData Loaded Successfully."
    )

    print(
        f"\nTable Name: {table_name}"
    )

    print(
        f"Rows Inserted: {len(df)}"
    )
