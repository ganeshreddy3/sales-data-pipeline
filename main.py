"""
main.py

Sales Data Pipeline
"""

from src.extract import extract_data
from src.transform import transform_data
from src.utils import save_dataframe
from src.load import load_data


def main():

    input_file = "data/raw/sales.csv"

    output_file = "data/processed/clean_sales.csv"

    # Extract
    df = extract_data(input_file)

    # Transform
    clean_df = transform_data(df)

    # Save cleaned CSV
    save_dataframe(
        clean_df,
        output_file
    )

    # Load into PostgreSQL
    load_data(
        clean_df
    )

    print("\n" + "=" * 50)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    main()
