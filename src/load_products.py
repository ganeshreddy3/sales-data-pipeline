"""
load_products.py

Load product data into PostgreSQL.
"""

import pandas as pd

from src.database import (
    get_database_engine
)


def load_products(
    df: pd.DataFrame
) -> None:

    print("\n" + "=" * 50)
    print("LOADING PRODUCTS TO DATABASE")
    print("=" * 50)

    engine = get_database_engine()

    df.to_sql(
        name="products",
        con=engine,
        if_exists="replace",
        index=False
    )

    print(
        "\nProducts loaded successfully."
    )

    print(
        f"\nRows inserted: {len(df)}"
    )
