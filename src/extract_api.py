"""
extract_api.py

Extract product data from Fake Store API.
"""

import pandas as pd
import requests


def extract_products_api() -> pd.DataFrame:

    url = "https://fakestoreapi.com/products"

    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

    df = pd.DataFrame(data)

    print("\n" + "=" * 50)
    print("API EXTRACTION SUCCESSFUL")
    print("=" * 50)

    print(f"\nDataset Shape: {df.shape}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())

    return df


if __name__ == "__main__":

    df = extract_products_api()

    print(df.head())
