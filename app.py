import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from datetime import datetime

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Currency Dashboard",
    layout="wide"
)

st.title("💱 Real-Time Currency Intelligence System")
st.markdown("Live exchange rates with Refresh feature ⟳")

# -----------------------------
# SESSION STATE (Refresh Control)
# -----------------------------
if "refresh" not in st.session_state:
    st.session_state.refresh = True

# زرار الريفريش
col1, col2 = st.columns([1, 5])

with col1:
    if st.button("⟳ Refresh Data"):
        st.session_state.refresh = True
        st.cache_data.clear()
        st.rerun()

# -----------------------------
# API Loader
# -----------------------------
@st.cache_data(ttl=3600)
def load_latest_rates():
    url = "https://v6.exchangerate-api.com/v6/dff927e21aa1a64f10901337/latest/USD"
    res = requests.get(url, timeout=10)
    return res.json()

# لو refresh true نعمل تحميل جديد
data = load_latest_rates()

# reset refresh flag
st.session_state.refresh = False

# -----------------------------
# Error Handling
# -----------------------------
if "rates" not in data:
    st.error("❌ Failed to load data from API")
    st.json(data)
    st.stop()

rates = data["rates"]
base = data.get("base_code", "USD")

df = pd.DataFrame(list(rates.items()), columns=["Currency", "Rate"])

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("⚙️ Settings")

selected_currencies = st.sidebar.multiselect(
    "Select currencies",
    df["Currency"].tolist(),
    default=["EUR", "GBP", "SAR", "AED", "JPY", "EGP"]
)

if selected_currencies:
    df = df[df["Currency"].isin(selected_currencies)]

# -----------------------------
# Converter
# -----------------------------
st.sidebar.subheader("🔄 Converter")

target_currency = st.sidebar.selectbox(
    "Convert USD to:",
    df["Currency"].tolist()
)

amount = st.sidebar.number_input("Amount in USD", value=1.0, min_value=0.0)

st.subheader("🔄 Currency Converter")

rate = df[df["Currency"] == target_currency]["Rate"].values[0]
converted = amount * rate

c1, c2, c3 = st.columns(3)

c1.metric("From", f"{amount} USD")
c2.metric("To", target_currency)
c3.metric("Result", f"{converted:.2f}")

# -----------------------------
# Table
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