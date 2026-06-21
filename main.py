"""
main.py

Sales Data Pipeline
"""

from src.extract import extract_data
from src.transform import transform_data
from src.utils import save_dataframe
from src.load import load_data
from src.logger import logger

from config.config import (
    INPUT_FILE,
    OUTPUT_FILE
)


def main():

    logger.info(
        "Pipeline Started"
    )

    df = extract_data(
        INPUT_FILE
    )

    clean_df = transform_data(
        df
    )

    save_dataframe(
        clean_df,
        OUTPUT_FILE
    )

    load_data(
        clean_df
    )

    logger.info(
        "Pipeline Completed"
    )

    print("\n" + "=" * 50)
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 50)


if __name__ == "__main__":
    main()
