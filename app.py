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

# ---------------------------
# Synthetic data generation
# ---------------------------
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

    # Introduce some missing values
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

# ---------------------------
# App layout
# ---------------------------
st.title("Critical Thinking Applied to Customer Churn")
st.markdown("""
I built this app to show how I approach a high-pressure data science request.  
Instead of immediately building a complex model, I applied critical thinking to reframe the problem, evaluate the data rigorously, and deliver a transparent, actionable solution.
""")

with st.sidebar:
    st.header("About this project")
    st.markdown("""
    **Scenario**  
    Leadership saw churn rise from ~4% to 7% and asked for a quick prediction model, believing a recent price increase was the main cause.

    **My approach**  
    - Reframe the problem  
    - Interrogate the data  
    - Test multiple hypotheses  
    - Prefer a transparent score over a black-box model  
    - Communicate uncertainty clearly
    """)
    st.caption("Portfolio project – synthetic data")

df = generate_data()

# Section 1: Problem Reframing
st.header("1. Problem Reframing")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Stated request")
    st.info("“Build a churn prediction model quickly so we can identify at-risk customers and intervene. We think the price increase is the main driver.”")
with col2:
    st.subheader("How I reframed it")
    st.success("“Why did churn increase, which drivers are strongest and actionable, and what should we do next under time pressure?”")

st.markdown("Reframing prevented me from locking into one hypothesis and one solution too early.")

# Section 2: Data Evaluation
st.header("2. Data Evaluation")
st.markdown("Before modeling, I examined base rates and key segments.")

overall = df["churned"].mean()
st.metric("Overall churn rate", f"{overall:.1%}")

def segment_rate(mask):
    return df.loc[mask, "churned"].mean()

segments = {
    "Price increase = Yes": segment_rate(df["received_price_increase"] == 1),
    "Price increase = No": segment_rate(df["received_price_increase"] == 0),
    "Usage < 10 hrs": segment_rate(df["monthly_usage_hours"] < 10),
    "Usage ≥ 10 hrs": segment_rate(df["monthly_usage_hours"] >= 10),
    "UI change + low usage": segment_rate((df["experienced_ui_change"] == 1) & (df["monthly_usage_hours"] < 15)),
    "High support tickets (≥3)": segment_rate(df["support_tickets_last_90d"] >= 3),
    "New customers (<3 months)": segment_rate(df["tenure_months"] < 3),
}

seg_df = pd.DataFrame({
    "Segment": list(segments.keys()),
    "Churn Rate": [f"{v:.1%}" for v in segments.values()]
})
st.dataframe(seg_df, use_container_width=True, hide_index=True)

st.markdown("""
**Key observation:**  
Low usage (especially combined with the recent UI change) shows a much larger lift than the price-increase flag.  
Price is a contributing factor for a subset of customers, not the dominant driver.
""")

# Section 3: Transparent Risk Score
st.header("3. Transparent Risk Score")
st.markdown("I created a simple, explainable score based on the strongest signals instead of jumping to a complex model.")

df["risk_score"] = df.apply(simple_risk_score, axis=1)
score_summary = df.groupby("risk_score")["churned"].agg(["mean", "count"]).reset_index()
score_summary.columns = ["Risk Score", "Actual Churn Rate", "Customers"]
score_summary["Actual Churn Rate"] = score_summary["Actual Churn Rate"].apply(lambda x: f"{x:.1%}")

st.dataframe(score_summary, use_container_width=True, hide_index=True)

st.markdown("""
**Score logic (transparent):**
- +2 if monthly usage < 10 hours  
- +1 if UI change and usage < 15 hours  
- +1 if support tickets ≥ 3  
- +1 if price increase and usage < 12 hours  

Higher scores clearly correspond to higher observed churn.
""")

# Section 4: Logistic Regression
st.header("4. Logistic Regression Baseline")
st.markdown("I also trained an interpretable Logistic Regression model as a baseline. It confirmed the same drivers.")

features = ["monthly_usage_hours", "experienced_ui_change", "received_price_increase",
            "support_tickets_last_90d", "tenure_months"]
model_df = df.dropna(subset=features + ["churned"])

X = model_df[features]
y = model_df["churned"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42, stratify=y)

pipe = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced", random_state=42))
])
pipe.fit(X_train, y_train)

auc = roc_auc_score(y_test, pipe.predict_proba(X_test)[:, 1])
st.metric("Hold-out ROC-AUC", f"{auc:.3f}")

coef = pd.Series(pipe.named_steps["clf"].coef_[0], index=features).sort_values(key=abs, ascending=False)
coef_df = pd.DataFrame({"Feature": coef.index, "Coefficient": coef.values.round(3)})
st.dataframe(coef_df, use_container_width=True, hide_index=True)

st.markdown("Negative coefficient on usage hours means lower usage increases churn risk — consistent with the segment analysis.")

# Section 5: Recommendation
st.header("5. My Recommendation")
st.markdown("""
Instead of delivering only a prediction model, I recommended:

1. Investigate and address the UI change’s impact on lower-usage customers.  
2. Run a small experiment (usage prompts or improved onboarding) on the high-risk segment.  
3. Use the transparent risk score for near-term targeting.  
4. Treat price as a secondary factor concentrated among already low-engagement customers.  
5. Improve data completeness on support interactions.

This approach is faster to explain, easier to monitor, and more actionable under time pressure.
""")

st.divider()
st.caption("Built as a portfolio project to demonstrate critical thinking, structured analysis, and interpretable modeling in a realistic data science scenario.")
