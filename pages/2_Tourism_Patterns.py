import streamlit as st
import pandas as pd
from snowflake.snowpark.context import get_active_session

st.set_page_config(page_title="Monument Tourism Trends", layout="wide")

st.title("🕌 Monument Tourism Trends (2019–2021)")

# Connect to Snowflake
session = get_active_session()
df = session.table("TOURISM").to_pandas()

# Clean column names
df.columns = df.columns.str.strip()

# Show available columns for debugging if needed
# st.write("Available Columns:", df.columns.tolist())

# Columns expected
monument_col = "Name of the Monument"
years = ['2019-20', '2020-21']

# Select monument
monument = st.selectbox("🏛️ Select a Monument", sorted(df[monument_col].unique()))

# Filter data
monument_df = df[df[monument_col] == monument]

# Extract values
domestic = [int(monument_df[f'Domestic-{year}'].values[0]) for year in years]
foreign = [int(monument_df[f'Foreign-{year}'].values[0]) for year in years]
total = [d + f for d, f in zip(domestic, foreign)]

# -------------------------
# Summary Metrics
# -------------------------
st.subheader(f"📊 Visitor Summary: {monument}")
col1, col2, col3 = st.columns(3)
col1.metric("Total Visitors (2019-20)", f"{total[0]:,}")
col2.metric("Total Visitors (2020-21)", f"{total[1]:,}")
change = ((total[1] - total[0]) / total[0]) * 100 if total[0] > 0 else 0
col3.metric("Change (%)", f"{change:+.2f}%")


# -------------------------
# Combined Bar Chart
# -------------------------
st.subheader(f"📈 Domestic vs Foreign Visitors to {monument}")

combined_df = pd.DataFrame({
    'Year': years * 2,
    'Type': ['Domestic'] * 2 + ['Foreign'] * 2,
    'Visitors': domestic + foreign
})
pivot_df = combined_df.pivot(index='Year', columns='Type', values='Visitors')
st.bar_chart(pivot_df)

# -------------------------
# Top Monuments by Total Visitors (2020-21)
# -------------------------
st.subheader("🏆 Top 10 Monuments by Total Visitors (2020-21)")
df['Total-2020-21'] = df['Domestic-2020-21'] + df['Foreign-2020-21']
top10 = df[[monument_col, 'Total-2020-21']].sort_values(by='Total-2020-21', ascending=False).head(10)
st.dataframe(top10.reset_index(drop=True), use_container_width=True)

# -------------------------
# Download Button
# -------------------------
@st.cache_data
def convert_df_to_csv(data):
    return data.to_csv(index=False).encode('utf-8')

csv = convert_df_to_csv(df)
st.download_button(
    label="⬇️ Download Full Dataset as CSV",
    data=csv,
    file_name='monument_tourism.csv',
    mime='text/csv'
)
