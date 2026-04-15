# 💱 Real-Time Currency Intelligence System

## 🚀 Overview

The **Real-Time Currency Intelligence System** is a data engineering
project that provides a live dashboard for global foreign exchange (FX)
rates.

It is built using a complete **data pipeline architecture** that fetches
real-time currency data, processes it, and visualizes it through an
interactive **Streamlit dashboard**.

### 🧠 This project demonstrates skills in:

-   Data Engineering (ETL Pipeline Design)
-   Real-time API Integration
-   Data Analysis with Pandas
-   Interactive Dashboards with Streamlit
-   Data Visualization with Plotly

------------------------------------------------------------------------

## 📊 Features

-   🌍 Real-time currency exchange rates (USD base)\
-   🔄 Manual refresh button ⟳ for live updates\
-   💱 Currency converter (USD → selected currency)\
-   🎯 Multi-currency filtering (user selection)\
-   📊 Interactive data table\
-   📈 Dynamic bar chart visualization\
-   ⚡ Cached API requests for performance optimization\
-   🛡️ Error handling for API failures

------------------------------------------------------------------------

## 🏗️ Project Architecture

``` bash
Currency-Intelligence-System/
│
├── app.py                  # Streamlit dashboard
├── requirements.txt        # Dependencies
├── src/
│   ├── fetch_data.py       # Data extraction (API layer)
│   ├── pipeline.py         # ETL processing logic
│   └── utils.py            # Helper functions
│
└── data/                   # Cached datasets (optional)
```

------------------------------------------------------------------------

## ⚙️ Tech Stack

-   **Python 3.10+**
-   **Streamlit** -- Web dashboard\
-   **Pandas** -- Data processing\
-   **Requests** -- API communication\
-   **Plotly** -- Data visualization

------------------------------------------------------------------------

## 🔌 Data Source

This project uses a free and reliable FX API:

🌐 https://open.er-api.com

------------------------------------------------------------------------

## 🚀 How to Run Locally

### 1️⃣ Clone the repository

``` bash
git clone https://github.com/AbdallahIbrahim27/currency-data-pipelinee.git
cd currency-data-pipelinee
```

### 2️⃣ Install dependencies

``` bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## 🔄 Live Refresh Feature

The system includes a **manual refresh button ⟳** that:

-   Clears cached API data\
-   Fetches the latest FX rates instantly\
-   Updates the dashboard in real-time

------------------------------------------------------------------------

## 📈 Use Cases

-   Financial data analysis\
-   Forex monitoring tools\
-   Data engineering portfolio projects\
-   Real-time API dashboards\
-   ETL pipeline demonstrations

------------------------------------------------------------------------

## 💡 Future Improvements

-   📊 Historical currency trends (7D / 30D / 1Y)\
-   🌍 Currency strength index (relative scoring)\
-   ⚡ Auto-refresh live streaming mode\
-   🧠 AI-based FX prediction module\
-   📦 FastAPI backend architecture\
-   🐳 Docker containerization\
-   ☁️ Cloud deployment (Streamlit Cloud / Render)

------------------------------------------------------------------------

## 👨‍💻 Author

**Abdallah Ibrahim**

-   GitHub: https://github.com/AbdallahIbrahim27

------------------------------------------------------------------------

## ⭐ Support

If you like this project:

-   ⭐ Star the repository\
-   🍴 Fork it\
-   🚀 Share it with others
