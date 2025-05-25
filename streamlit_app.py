import streamlit as st

# Page configuration
st.set_page_config(page_title="India Tourism Analytics", layout="wide")

# Title
st.title("🇮🇳 India Tourism Analytics Dashboard")

# Introductory text
st.markdown("""
Welcome to the *India Tourism Dashboard*.  
Navigate through the sidebar to explore:

1. 🛂 Visa trends by nationality  
2. 🏛 Monument-wise tourism patterns  
3. 🌱 Sustainability and seasonality impacts  
""")

# Display image with updated parameter
st.image(
    "https://d18x2uyjeekruj.cloudfront.net/wp-content/uploads/2023/01/tourism.jpg",
    use_container_width=True
)