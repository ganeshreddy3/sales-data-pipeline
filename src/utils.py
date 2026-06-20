"""
utils.py

Utility functions for the Sales Data Pipeline.
"""

import os
import pandas as pd


def save_dataframe(
    df: pd.DataFrame,
    output_path: str
) -> None:
    """
    Save DataFrame to CSV.

    Parameters
    ----------
    df : pd.DataFrame

    output_path : str
    """

    # Create folder if it doesn't exist

    directory = os.path.dirname(
        output_path
    )

    os.makedirs(
        directory,
        exist_ok=True
    )

    # Save CSV

    df.to_csv(
        output_path,
        index=False
    )

    print("\n" + "=" * 50)
    print("DATA SAVED SUCCESSFULLY")
    print("=" * 50)

    print(
        f"\nOutput File:\n{output_path}"
    )

    print(
        f"\nRows Saved: {len(df)}"
    )

    print(
        f"Columns Saved: {len(df.columns)}"
    )
