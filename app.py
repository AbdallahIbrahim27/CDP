import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from datetime import datetime

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Currency Data Pipeline Dashboard",
    layout="wide"
)

st.title("💱 Currency Data Pipeline Dashboard")
st.markdown("Live exchange rates with selectable currencies")

# -----------------------------
# Safe API Loader
# -----------------------------
@st.cache_data(ttl=3600)
def load_latest_rates():
    try:
        url = "https://open.er-api.com/v6/latest/USD"
        res = requests.get(url, timeout=10)
        return res.json()
    except Exception as e:
        return {"error": str(e)}

data = load_latest_rates()

# -----------------------------
# Error Handling (IMPORTANT FIX)
# -----------------------------
if "rates" not in data:
    st.error("❌ Failed to load currency data from API")
    st.json(data)
    st.stop()

rates = data["rates"]
base = data.get("base_code", "USD")

df = pd.DataFrame(list(rates.items()), columns=["Currency", "Rate"])

# -----------------------------
# Sidebar - Currency Filter
# -----------------------------
st.sidebar.header("⚙️ Settings")

selected_currencies = st.sidebar.multiselect(
    "Select currencies to display",
    df["Currency"].tolist(),
    default=["EUR", "GBP", "SAR", "AED", "KWD", "OMR","JOD","EGP"]
)

# Apply filter safely
if selected_currencies:
    df = df[df["Currency"].isin(selected_currencies)]

# -----------------------------
# Sidebar - Converter
# -----------------------------
st.sidebar.subheader("🔄 Converter")

target_currency = st.sidebar.selectbox(
    "Convert USD to:",
    df["Currency"].tolist()
)

amount = st.sidebar.number_input("Amount in USD", value=1.0, min_value=0.0)

# -----------------------------
# Converter Result
# -----------------------------
st.subheader("🔄 Currency Converter")

rate = df[df["Currency"] == target_currency]["Rate"].values[0]
converted = amount * rate

col1, col2, col3 = st.columns(3)

col1.metric("From", f"{amount} USD")
col2.metric("To", target_currency)
col3.metric("Result", f"{converted:.2f}")

# -----------------------------
# Data Table
# -----------------------------
st.subheader("📊 Exchange Rates")

st.dataframe(df.sort_values("Rate", ascending=False), use_container_width=True)

# -----------------------------
# Chart
# -----------------------------
st.subheader("📈 Currency Comparison")

fig = px.bar(
    df.sort_values("Rate", ascending=False),
    x="Currency",
    y="Rate",
    title="Selected Currency Rates vs USD"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Footer
# -----------------------------
st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")