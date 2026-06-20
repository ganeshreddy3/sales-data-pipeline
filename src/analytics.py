"""
analytics.py

Business analytics.
"""

import pandas as pd

from src.database import (
    get_database_engine
)


def total_orders():

    engine = get_database_engine()

    query = """
    SELECT COUNT(*)
    FROM sales
    """

    result = pd.read_sql(
        query,
        engine
    )

    print("\nTotal Orders")

    print(result)


def total_revenue():

    engine = get_database_engine()

    query = """
    SELECT SUM(totalamount)
    FROM sales
    """

    result = pd.read_sql(
        query,
        engine
    )

    print("\nTotal Revenue")

    print(result)


def product_sales():

    engine = get_database_engine()

    query = """
    SELECT
    product,
    SUM(quantity)
    AS quantity
    FROM sales
    GROUP BY product
    ORDER BY quantity DESC
    """

    result = pd.read_sql(
        query,
        engine
    )

    print("\nProduct Sales")

    print(result)


def category_revenue():

    engine = get_database_engine()

    query = """
    SELECT
    category,
    SUM(totalamount)
    AS revenue
    FROM sales
    GROUP BY category
    ORDER BY revenue DESC
    """

    result = pd.read_sql(
        query,
        engine
    )

    print("\nCategory Revenue")

    print(result)
