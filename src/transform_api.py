"""
transform_api.py

Transform product data from Fake Store API.
"""

import pandas as pd


def transform_products(df: pd.DataFrame) -> pd.DataFrame:

    print("\n" + "=" * 50)
    print("PRODUCT DATA TRANSFORMATION")
    print("=" * 50)

    # Select useful columns

    df = df[
        [
            "id",
            "title",
            "price",
            "category"
        ]
    ]

    # Rename columns

    df.columns = [
        "product_id",
        "product_name",
        "price",
        "category"
    ]

    # Remove duplicates

    df = df.drop_duplicates()

    # Handle missing values

    df = df.dropna()

    print("\nTransformed Shape:")
    print(df.shape)

    print("\nFirst 5 Rows:")
    print(df.head())

    return df
