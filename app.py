import streamlit as st
import pandas as pd
import  joblib
import plotly.express as px
import plotly.graph_objects as go

from sklearn.base import BaseEstimator, TransformerMixin


# Feature Enginnering

class FeatureEngineer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):

        X = X.copy()
        X["week_start"] = pd.to_datetime(X["week_start"])
        # Date Features
        X["year"] = X["week_start"].dt.year
        X["month"] = X["week_start"].dt.month
        X["quarter"] = X["week_start"].dt.quarter
        X["week_no"] = X["week_start"].dt.isocalendar().week.astype(int)
        X["marketing_visit_ratio"] = ( X["marketing_spend"] / (X["store_visits"] + 1))
        X["googlescore_visit_ratio"] = ( X["google_trend_score"] / (X["store_visits"] + 1))

        return X

st.set_page_config(
    page_title="Sales Prediction ",
    page_icon="📈",
    layout="wide"
)


st.markdown("""
<style>
.block-container{
    padding-top:2rem;
}

h1{
    text-align:center;
}

.stButton>button{
    width:100%;
    height:50px;
    font-size:18px;
}
</style>
""", unsafe_allow_html=True)

model = joblib.load("lr_new.pkl")

st.title("Retail Sales Forecasting System")

st.markdown(
    """
    ### Welcome to the Sales Prediction Dashboard

    Predict weekly retail sales using:
    - Weather Conditions
    - Google Trend Score
    - Marketing Spend
    - Store Visits
    - Holiday Impact

    Enter the required inputs from the sidebar and click **Predict Sales** to get the forecast.
    """
)

st.sidebar.header("Sales Input Parameters")

week_start = st.sidebar.date_input(
    "Week Start Date"
)

region = st.sidebar.selectbox(
    "Region",
    ["North", "South", "East", "West"]
)
avg_temp = st.sidebar.number_input(
    "Average Temperature",
    min_value=-10.0,
    max_value=50.0,
    value=25.0,
    step=0.1
)
google_trend_score = st.sidebar.number_input(
    "Google Trend Score",
    min_value=0.0,
    max_value=100.0,
    value=50.0,
    step=1.0
)
marketing_spend = st.sidebar.number_input(
    "Marketing Spend",
    min_value=0.0,
    value=50.0,
    step=1.0
)
store_visits = st.sidebar.number_input(
    "Store Visits",
    min_value=0.0,
    value=150.0,
    step=1.0
)

holiday_flag = st.sidebar.selectbox(
    "Holiday Week",
    [0, 1],
    format_func=lambda x: "Yes" if x == 1 else "No"
)


input_df = pd.DataFrame({
    "week_start": [week_start],
    "region": [region],
    "avg_temp": [avg_temp],
    "google_trend_score": [google_trend_score],
    "marketing_spend": [marketing_spend],
    "store_visits": [store_visits],
    "holiday_flag": [holiday_flag]
})

st.dataframe(input_df,use_container_width=True)

if st.button("Predict Sales"):

    weekly_sales = model.predict(input_df)[0]

    monthly_sales = round(weekly_sales * 4.33,4)
    quarterly_sales = round(weekly_sales * 13,4)
    annual_sales = round(weekly_sales * 52,4)

    st.subheader("Sales Forecast")
    st.subheader("Weekly Sales Forecast")

    max_sales = weekly_sales * 1.5

    fig_gauge = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=weekly_sales,
            number={
                "prefix": "₹ ",
                "valueformat": ",.2f"
            },
            title={
                "text": "Predicted Weekly Sales"
            },
            gauge={
                "axis": {
                    "range": [0, max_sales]
                }
            }
        )
    )

    st.plotly_chart(fig_gauge, use_container_width=True)
    col1,col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Weekly Sales",
            f"₹ {weekly_sales:,.2f}"
        )

    with col2:
        st.metric(
            "Monthly Sales",
            f"₹ {monthly_sales:,.2f}"
        )

    with col3:
        st.metric(
            "Quarterly Sales",
            f"₹ {quarterly_sales:,.2f}"
        )

    with col4:
        st.metric(
            "Annual Sales",
            f"₹ {annual_sales:,.2f}"
        )

    st.success("Sales forecast generated successfully!")
    
