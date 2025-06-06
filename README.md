# 🧳 Impactful Journeys: Responsible Tourism Tracker

A data-driven dashboard to uncover cultural patterns, encourage sustainable tourism, and promote responsible travel across India using official datasets and Snowflake.

---

## 📘 Table of Contents

- [🔧 Requirements](#-requirements)  
- [📦 Install Dependencies](#-install-dependencies)  
- [📁 Project Structure](#-project-structure)  
- [📂 Step-by-Step Instructions](#-step-by-step-instructions)  
  - [Run with Local CSVs](#1-run-with-local-csvs)  
  - [Run with Snowflake](#2-run-with-snowflake-optional)  
- [🧭 Navigating the Dashboard](#-navigating-the-dashboard)  
- [🚀 Deployment on Streamlit Cloud](#-deployment-on-streamlit-cloud)  
- [💡 Notes](#-notes)

---

## 🔧 Requirements

Make sure you have:

- Python 3.8+
- pip
- Snowflake account (for cloud data source)
- Streamlit

---

## 📦 Install Dependencies

```bash
pip install streamlit pandas plotly snowflake-connector-python matplotlib
```

---

## 📁 Project Structure

```
project/
├── streamlit_app.py               # Main homepage of the app
├── pages/
│   ├── 1_Visa_Insights.py         # Tourist nationality analysis using VISA dataset
│   ├── 2_Tourism_Patterns.py      # Year-wise monument visitor patterns
│   └── 3_Sustainability.py        # Sustainability insights & overcrowding
├── data/
│   ├── VISA.csv                   # Tourist nationality dataset
│   └── Tourism.csv                # Monument-wise tourism dataset
├── images/                        # (Optional) Screenshots for submission
└── README.md
```

---

## 📂 Step-by-Step Instructions

### ✅ 1. Run with Local CSVs

**Step 1: Clone the repository**
```bash
git clone https://github.com/yourusername/responsible-tourism-tracker.git
cd responsible-tourism-tracker
```

**Step 2: Place the Datasets**

Put the following files inside the `/data` folder:

- `VISA.csv`
- `Tourism.csv`

Ensure the file names match exactly.

**Step 3: Run the Streamlit App**

```bash
streamlit run streamlit_app.py
```

Open your browser: [http://localhost:8501](http://localhost:8501)

---

### ☁️ 2. Run with Snowflake (Optional)

To use **Snowflake** as your data source instead of CSVs:

**Step 1: Set up your Snowflake environment**

- Make sure your Snowflake account has access to the database and table(s) for:
  - Visa-related data (e.g., `VISA_DATA`)
  - Monument tourism data (e.g., `TOURISM_STATS`)

**Step 2: Create a connection file (`snowflake_config.py`)**

```python
# snowflake_config.py
import snowflake.connector

def get_connection():
    conn = snowflake.connector.connect(
        user='YOUR_USERNAME',
        password='YOUR_PASSWORD',
        account='YOUR_ACCOUNT_ID',
        warehouse='YOUR_WAREHOUSE',
        database='YOUR_DATABASE',
        schema='YOUR_SCHEMA'
    )
    return conn
```

**Step 3: Modify data-loading code in your pages**

For example, replace:

```python
df = pd.read_csv('data/VISA.csv')
```

With:

```python
from snowflake_config import get_connection
import pandas as pd

conn = get_connection()
query = "SELECT * FROM VISA_DATA"
df = pd.read_sql(query, conn)
```

Repeat similar changes for `Tourism.csv` queries in other pages.

---

## 🧭 Navigating the Dashboard

The app contains three interactive pages (via sidebar):

1. **Visa Insights**
   - Explore country-wise tourist interests via bar charts.
2. **Tourism Patterns**
   - Select a monument to see year-wise domestic & foreign visitor stats.
3. **Sustainability**
   - Visualize over-tourism, seasonal visitor surges, and eco-tourism proposals.

---

## 🚀 Deployment on Streamlit Cloud

To deploy your app online:

1. Push your code to GitHub
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub and deploy the repo
4. For Snowflake:
   - Store secrets (like username/password) via `streamlit secrets`
   - Update the connector to pull credentials from `st.secrets`

Example:

```toml
# .streamlit/secrets.toml
snowflake_user = "your_user"
snowflake_password = "your_password"
snowflake_account = "your_account"
```

Then use in code:

```python
import streamlit as st
import snowflake.connector

conn = snowflake.connector.connect(
    user=st.secrets["snowflake_user"],
    password=st.secrets["snowflake_password"],
    account=st.secrets["snowflake_account"],
    ...
)
```

---

## 💡 Notes

- If hosting with Streamlit Cloud, ensure all files needed (`.py`, `.csv`, `.toml`) are in the repo.
- Plotly and Matplotlib rendering may require additional config in cloud deployment.
- Snowflake free trial users may hit usage limits—optimize queries or limit result size if needed.

---

## ✅ You're Ready!

Feel free to customize or expand this project for your tourism innovation initiatives.
