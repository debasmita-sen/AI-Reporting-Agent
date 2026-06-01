import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="AI BI Reporting Dashboard", layout="wide")

st.title("AI Business Intelligence Reporting Dashboard")

df = pd.read_csv("File.csv")

df["Revenue"] = df["Quantity"] * df["Unit_Price"]

total_revenue = df["Revenue"].sum()
total_orders = len(df)
top_product = df.groupby("Product")["Revenue"].sum().idxmax()
top_salesperson = df.groupby("Salesperson")["Revenue"].sum().idxmax()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
col2.metric("Total Orders", total_orders)
col3.metric("Top Product", top_product)
col4.metric("Top Salesperson", top_salesperson)

st.subheader("Cleaned Sales Data")
st.dataframe(df, use_container_width=True)

st.subheader("Revenue by Product")
product_chart = df.groupby("Product", as_index=False)["Revenue"].sum()
fig1 = px.bar(product_chart, x="Product", y="Revenue", title="Revenue by Product")
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Revenue by Salesperson")
salesperson_chart = df.groupby("Salesperson", as_index=False)["Revenue"].sum()
fig2 = px.bar(salesperson_chart, x="Salesperson", y="Revenue", title="Revenue by Salesperson")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Revenue by Category")
category_chart = df.groupby("Category", as_index=False)["Revenue"].sum()
fig3 = px.pie(category_chart, names="Category", values="Revenue", title="Revenue by Category")
st.plotly_chart(fig3, use_container_width=True)