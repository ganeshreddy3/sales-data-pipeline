"""
transform.py

This module cleans and transforms the sales dataset.
"""

import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform sales data.

    Parameters
    ----------
    df : pd.DataFrame
        Raw sales data.

    Returns
    -------
    pd.DataFrame
        Cleaned sales data.
    """

    print("\n" + "=" * 50)
    print("DATA TRANSFORMATION")
    print("=" * 50)

    # Remove duplicate rows
    duplicate_count = df.duplicated().sum()
    df = df.drop_duplicates()

    print(f"\nDuplicates Removed: {duplicate_count}")

    # Remove rows with missing values
    missing_before = df.isnull().sum().sum()

    df = df.dropna()

    missing_after = df.isnull().sum().sum()

    print(
        f"Missing Values Removed: "
        f"{missing_before - missing_after}"
    )

    # Convert numeric columns

    df["Price"] = pd.to_numeric(
        df["Price"],
        errors="coerce"
    )

    df["Quantity"] = pd.to_numeric(
        df["Quantity"],
        errors="coerce"
    )

    # Remove rows where Price or Quantity
    # could not be converted

    df = df.dropna(
        subset=["Price", "Quantity"]
    )

    # Convert Date column

    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    # Remove invalid dates

    df = df.dropna(
        subset=["Date"]
    )

    # Standardize text columns

    text_columns = [
        "CustomerID",
        "Product",
        "Category"
    ]

    for col in text_columns:

        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .str.title()
        )

    # Remove invalid prices

    df = df[
        df["Price"] > 0
    ]

    # Remove invalid quantities

    df = df[
        df["Quantity"] > 0
    ]

    # Create TotalAmount column

    df["TotalAmount"] = (
        df["Price"] *
        df["Quantity"]
    )

    # Reset index

    df.reset_index(
        drop=True,
        inplace=True
    )

    print("\nTransformation Completed Successfully.")

    print(f"\nFinal Dataset Shape: {df.shape}")

    print("\nData Types:")

    print(df.dtypes)

    print("\nFirst Five Rows:")

    print(df.head())

    return df
