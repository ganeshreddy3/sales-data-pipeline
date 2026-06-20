import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

# Database Connection

DATABASE_URL = (
    "postgresql://"
    "postgres:"
    "postgres@"
    "localhost:"
    "5432/"
    "sales_db"
)

engine = create_engine(DATABASE_URL)

# Read Data

df = pd.read_sql(
    "SELECT * FROM sales",
    engine
)

# Normalize column names

df.columns = df.columns.str.lower()

# Streamlit Config

st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)

st.title("📊 Sales Data Dashboard")

# KPIs

total_orders = len(df)

total_revenue = df["totalamount"].sum()

average_order = total_revenue / total_orders

total_quantity = df["quantity"].sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Orders",
    total_orders
)

col2.metric(
    "Total Revenue",
    f"₹{total_revenue:,.0f}"
)

col3.metric(
    "Average Order",
    f"₹{average_order:,.0f}"
)

col4.metric(
    "Items Sold",
    total_quantity
)

st.divider()

# Revenue by Category

st.subheader(
    "Revenue by Category"
)

category = (
    df.groupby(
        "category"
    )["totalamount"]
    .sum()
)

st.bar_chart(category)

# Product Sales

st.subheader(
    "Product Sales"
)

product = (
    df.groupby(
        "product"
    )["quantity"]
    .sum()
)

st.bar_chart(product)

st.divider()

st.subheader("Sales Data")

st.dataframe(df)
