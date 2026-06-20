"""
extract.py

This module extracts sales data from a CSV file.
"""

import os
import pandas as pd


def extract_data(file_path: str) -> pd.DataFrame:
    """
    Extract data from a CSV file.

    Parameters
    ----------
    file_path : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded DataFrame.
    """

    try:
        # Check if file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        # Read CSV
        df = pd.read_csv(file_path)

        # Display basic information
        print("\n" + "=" * 50)
        print("DATA EXTRACTION SUCCESSFUL")
        print("=" * 50)

        print(f"\nDataset Shape: {df.shape}")

        print("\nColumn Names:")
        for column in df.columns:
            print(f"- {column}")

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nExtraction Completed Successfully.\n")

        return df

    except FileNotFoundError as e:
        print(f"\nERROR: {e}")
        raise

    except pd.errors.EmptyDataError:
        print("\nERROR: CSV file is empty.")
        raise

    except pd.errors.ParserError:
        print("\nERROR: Unable to parse CSV file.")
        raise

    except Exception as e:
        print(f"\nUnexpected Error: {e}")
        raise


# Testing
if __name__ == "__main__":

    FILE_PATH = "data/raw/sales.csv"

    data = extract_data(FILE_PATH)
