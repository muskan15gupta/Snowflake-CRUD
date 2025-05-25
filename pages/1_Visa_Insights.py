import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

st.set_page_config(page_title="Visa Insights", layout="wide")

st.title("🛂 Visa Insights by Nationality")

# Connect to Snowflake and load table
session = get_active_session()
df = session.table("VISA").to_pandas()

# Group by country
visa_summary = df.groupby('COUNTRY')[
    ['TOURIST VISA', 'EMPLOYMENT VISA', 'BUSINESS VISA', 'CONFERENCE VISA']
].sum().reset_index()

# -------------------------
# Summary Metrics
# -------------------------
st.subheader("📊 Key Metrics")
total_visas = df[['TOURIST VISA', 'EMPLOYMENT VISA', 'BUSINESS VISA', 'CONFERENCE VISA']].sum().sum()
st.columns(3)[0].metric("Total Visas Issued", f"{int(total_visas):,}")
st.columns(3)[1].metric("Unique Countries", visa_summary['COUNTRY'].nunique())
st.columns(3)[2].metric("Visa Types", "4")

# -------------------------
# Visa Type Selector Chart
# -------------------------
st.subheader("🌍 Top 10 Countries by Selected Visa Type")

visa_type = st.selectbox("Choose Visa Type", ['TOURIST VISA', 'EMPLOYMENT VISA', 'BUSINESS VISA', 'CONFERENCE VISA'])
top_countries = visa_summary.sort_values(by=visa_type, ascending=False).head(10)

st.bar_chart(top_countries.set_index('COUNTRY')[visa_type])

# -------------------------
# Visa Type Distribution (Bar Chart)
# -------------------------
st.subheader("📊 Visa Type Distribution (All Countries)")

visa_totals = df[['TOURIST VISA', 'EMPLOYMENT VISA', 'BUSINESS VISA', 'CONFERENCE VISA']].sum().reset_index()
visa_totals.columns = ['Visa Type', 'Count']
st.bar_chart(visa_totals.set_index('Visa Type'))

# -------------------------
# Country Filter
# -------------------------
st.subheader("🔍 View Visa Details by Country")
selected_country = st.selectbox("Filter by Country", visa_summary['COUNTRY'].unique())
filtered_df = visa_summary[visa_summary['COUNTRY'] == selected_country]
st.table(filtered_df.set_index('COUNTRY'))

# -------------------------
# Full Visa Summary Table
# -------------------------
st.subheader("🧾 Full Visa Summary Table")
st.dataframe(visa_summary.sort_values(by='TOURIST VISA', ascending=False).reset_index(drop=True), use_container_width=True)

# -------------------------
# Download Summary as CSV
# -------------------------
@st.cache_data
def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

csv_data = convert_df_to_csv(visa_summary)
st.download_button(
    label="⬇️ Download Visa Summary as CSV",
    data=csv_data,
    file_name='visa_summary.csv',
    mime='text/csv'
)
