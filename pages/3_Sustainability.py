import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

st.title("🌿 Tourism Sustainability Insights")

session = get_active_session()
df = session.table("TOURISM").to_pandas()

# Strip spaces in column names
df.columns = df.columns.str.strip()

df["Total-2019-20"] = df["Domestic-2019-20"] + df["Foreign-2019-20"]

st.subheader("🏛️ Most Visited Monuments (2019-20)")
top_visited = df.sort_values("Total-2019-20", ascending=False).head(10)
st.dataframe(top_visited[["Name of the Monument", "Total-2019-20"]])

st.subheader("📉 Monuments with Highest Drop in Domestic Tourists")
df["Drop % Domestic"] = df["% Growth 2021-21/2019-20-Domestic"]
st.dataframe(df.sort_values("Drop % Domestic").head(10)[["Name of the Monument", "Drop % Domestic"]])

st.subheader("🌱 Low-Traffic Monuments (Untapped Potential)")
low_traffic = df[df["Total-2019-20"] < 20000]
st.dataframe(low_traffic[["Name of the Monument", "Total-2019-20"]])
