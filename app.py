import streamlit as st
import pandas as pd

# ==========================================
# 1. PAGE SETUP
# ==========================================
st.set_page_config(page_title="Churn Dashboard", layout="wide")
st.title("🚨 Customer Churn Prediction Dashboard")

# ==========================================
# 2. LOAD DATA (WITH CACHING FOR SPEED)
# ==========================================
@st.cache_data
def load_data():
    return pd.read_csv('churn_risk_data.csv')

try:
    data = load_data()
except FileNotFoundError:
    st.error("Error: 'churn_risk_data.csv' not found. Make sure you ran the Jupyter Notebook to generate this file in the same folder.")
    st.stop()

# ==========================================
# 3. EXECUTIVE KPIs
# ==========================================
st.subheader("📈 Executive Summary")

total_high_risk = len(data[data['Risk_Percentage'] > 80])
avg_risk = data['Risk_Percentage'].mean()

col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Critical Risk Customers (>80%)", value=total_high_risk)
with col2:
    st.metric(label="Average Fleet Risk", value=f"{avg_risk:.1f}%")
with col3:
    st.metric(label="Total Customers Scored", value=len(data))

st.markdown("---")

# ==========================================
# 4. ACTIONABLE DATA TABLE
# ==========================================
st.subheader("🎯 Highest Risk Customers Action List")
st.write("These customers have the highest probability of leaving this month. Prioritize retention efforts here.")

# Show top 20 highest risk
st.dataframe(
    data.head(20),
    width="stretch",
    hide_index=True 
)

st.markdown("---")

# ==========================================
# 5. VISUALIZATIONS (OPTIMIZED FOR PERFORMANCE)
# ==========================================
st.subheader("📊 Visualizing the Danger Zone: Risk vs. Tenure")
st.write("These charts show that newer customers (low tenure on the left) have a much higher risk of leaving.")

# Create two columns for the charts side-by-side
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.markdown("#### Risk Trend (Sample of 500 Customers)")
    # Sampling 500 rows avoids browser lag and displays a clean scatter plot
    sample_data = data.sample(n=min(500, len(data)), random_state=42)
    st.scatter_chart(
        data=sample_data, 
        x='tenure', 
        y='Risk_Percentage',
        color='#FF4B4B'
    )

with chart_col2:
    st.markdown("#### Average Risk by Tenure Group (Months)")
    # Group by tenure and calculate mean Risk_Percentage (reduces data points to 73, rendering instantly)
    avg_risk_by_tenure = data.groupby('tenure')['Risk_Percentage'].mean().reset_index()
    st.bar_chart(
        data=avg_risk_by_tenure, 
        x='tenure', 
        y='Risk_Percentage'
    )