import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score

st.set_page_config(
    page_title="Critical Thinking Churn Analysis",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def generate_data(n=5000, seed=42):
    np.random.seed(seed)
    df = pd.DataFrame({
        "customer_id": range(1, n + 1),
        "tenure_months": np.random.randint(1, 36, n),
        "monthly_usage_hours": np.random.gamma(2, 15, n).round(1),
        "support_tickets_last_90d": np.random.poisson(1.2, n),
        "plan_type": np.random.choice(["Basic", "Pro", "Enterprise"], n, p=[0.5, 0.35, 0.15]),
        "received_price_increase": np.random.choice([0, 1], n, p=[0.4, 0.6]),
        "experienced_ui_change": np.random.choice([0, 1], n, p=[0.3, 0.7]),
    })
    base = 0.04
    usage_effect = np.where(df["monthly_usage_hours"] < 10, 0.08, 0)
    ui_effect = np.where((df["experienced_ui_change"] == 1) & (df["monthly_usage_hours"] < 15), 0.06, 0)
    price_effect = np.where((df["received_price_increase"] == 1) & (df["monthly_usage_hours"] < 12), 0.03, 0)
    support_effect = np.where(df["support_tickets_last_90d"] >= 3, 0.04, 0)
    tenure_effect = np.where(df["tenure_months"] < 3, 0.03, 0)
    prob = np.clip(base + usage_effect + ui_effect + price_effect + support_effect + tenure_effect, 0, 0.6)
    df["churned"] = (np.random.rand(n) < prob).astype(int)
    missing_idx = np.random.choice(df.index, 150, replace=False)
    df.loc[missing_idx, "support_tickets_last_90d"] = np.nan
    return df

def simple_risk_score(row):
    score = 0
    if row["monthly_usage_hours"] < 10:
        score += 2
    elif row["monthly_usage_hours"] < 15 and row["experienced_ui_change"] == 1:
        score += 1
    if pd.notna(row["support_tickets_last_90d"]) and row["support_tickets_last_90d"] >= 3:
        score += 1
    if row["received_price_increase"] == 1 and row["monthly_usage_hours"] < 12:
        score += 1
    return score

st.sidebar.header("Data Source")
data_source = st.sidebar.radio(
    "Choose how to load data",
    ["Use synthetic demo data", "Upload CSV file", "Connect to database"]
)

df = None

if data_source == "Upload CSV file":
    uploaded = st.sidebar.file_uploader("Upload your churn CSV", type=["csv"])
    if uploaded is not None:
        df = pd.read_csv(uploaded)
        st.sidebar.success(f"Loaded {len(df):,} rows from CSV")
    else:
        st.sidebar.info("Please upload a CSV file")

elif data_source == "Connect to database":
    st.sidebar.markdown("**Database connection**")
    st.sidebar.caption("Credentials are used only in this session and are not stored.")
    db_type = st.sidebar.selectbox("Database type", ["PostgreSQL", "MySQL", "SQLite"])
    if db_type == "SQLite":
        sqlite_path = st.sidebar.text_input("SQLite file path", "churn.db")
        table_name = st.sidebar.text_input("Table name", "customers")
        if st.sidebar.button("Load from SQLite"):
            try:
                import sqlite3
                conn = sqlite3.connect(sqlite_path)
                df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
                conn.close()
                st.sidebar.success(f"Loaded {len(df):,} rows")
            except Exception as e:
                st.sidebar.error(str(e))
    else:
        host = st.sidebar.text_input("Host", "localhost")
        port = st.sidebar.text_input("Port", "5432" if db_type == "PostgreSQL" else "3306")
        database = st.sidebar.text_input("Database name")
        user = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        table_name = st.sidebar.text_input("Table name", "customers")
        if st.sidebar.button("Connect and load data"):
            try:
                from sqlalchemy import create_engine
                if db_type == "PostgreSQL":
                    url = f"postgresql://{user}:{password}@{host}:{port}/{database}"
                else:
                    url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
                engine = create_engine(url)
                df = pd.read_sql(f"SELECT * FROM {table_name}", engine)
                st.sidebar.success(f"Loaded {len(df):,} rows")
            except Exception as e:
                st.sidebar.error(str(e))

if df is None:
    if data_source != "Use synthetic demo data":
        st.info("Using synthetic demo data until you load your own.")
    df = generate_data()

st.title("Critical Thinking Applied to Customer Churn")
st.markdown("""
I built this app to show how I approach a high-pressure data science request.  
Users can load their own data via CSV upload or direct database connection.
""")

with st.sidebar:
    st.markdown("---")
    st.header("About")
    st.caption("Supports synthetic data, CSV, or database")

st.header("1. Problem Reframing")
col1, col2 = st.columns(2)
with col1:
    st.info("Stated: Build a model quickly. Price is the main driver.")
with col2:
    st.success("Reframed: Why did churn rise and which drivers are actionable?")

st.header("2. Data Preview")
if "churned" in df.columns:
    st.metric("Overall churn rate", f"{df['churned'].mean():.1%}")
st.dataframe(df.head(8), use_container_width=True)

st.header("3. Risk Score & Model")
st.markdown("The app calculates a transparent risk score and Logistic Regression baseline when the required columns are present.")

if all(c in df.columns for c in ["monthly_usage_hours", "experienced_ui_change", "support_tickets_last_90d", "received_price_increase"]):
    df["risk_score"] = df.apply(simple_risk_score, axis=1)
    if "churned" in df.columns:
        summary = df.groupby("risk_score")["churned"].mean().reset_index()
        summary.columns = ["Risk Score", "Churn Rate"]
        summary["Churn Rate"] = summary["Churn Rate"].apply(lambda x: f"{x:.1%}")
        st.dataframe(summary, hide_index=True)

st.header("4. Recommendation")
st.markdown("""
- Investigate usage and recent product changes first.  
- Use a transparent score for targeting.  
- Validate with a small experiment.
""")

st.caption("End users can supply their own data from CSV or database.")
