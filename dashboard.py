import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Retail Analytics Dashboard",
    layout="wide"
)

# -------------------------------------------------
# Custom CSS Styling
# -------------------------------------------------
st.markdown("""
<style>

[data-testid="stSidebar"] {
    background-color: #1f2937;
}

[data-testid="stSidebar"] label {
    color: white;
    font-weight: bold;
}

.main-title {
    font-size:36px;
    font-weight:bold;
    text-align:center;
    color:#1f4e79;
}

.kpi-card {
    background-color:#f0f2f6;
    padding:20px;
    border-radius:10px;
    text-align:center;
    box-shadow:0px 3px 8px rgba(0,0,0,0.15);
}

.kpi-value {
    font-size:28px;
    font-weight:bold;
    color:#0f4c81;
}

.kpi-title {
    font-size:16px;
    color:#444;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Title
# -------------------------------------------------
st.markdown('<p class="main-title">Retail Sales Analytics Dashboard</p>', unsafe_allow_html=True)

# -------------------------------------------------
# Load Data
# -------------------------------------------------
df = pd.read_csv("data/transformed_retail.csv")

# -------------------------------------------------
# Sidebar Filters
# -------------------------------------------------
st.sidebar.title("Filters")

country = st.sidebar.multiselect(
    "Country",
    df["Country"].unique(),
    default=df["Country"].unique()
)

month = st.sidebar.multiselect(
    "Month",
    sorted(df["Month"].unique()),
    default=sorted(df["Month"].unique())
)

filtered_df = df[
    (df["Country"].isin(country)) &
    (df["Month"].isin(month))
]

# -------------------------------------------------
# KPI Metrics
# -------------------------------------------------
total_sales = filtered_df["TotalAmount"].sum()
total_orders = filtered_df["Invoice"].nunique()
total_customers = filtered_df["Customer ID"].nunique()
total_products = filtered_df["StockCode"].nunique()

k1, k2, k3, k4 = st.columns(4)

k1.markdown(f"""
<div class="kpi-card">
<p class="kpi-title">Total Sales</p>
<p class="kpi-value">${total_sales:,.0f}</p>
</div>
""", unsafe_allow_html=True)

k2.markdown(f"""
<div class="kpi-card">
<p class="kpi-title">Total Orders</p>
<p class="kpi-value">{total_orders}</p>
</div>
""", unsafe_allow_html=True)

k3.markdown(f"""
<div class="kpi-card">
<p class="kpi-title">Total Customers</p>
<p class="kpi-value">{total_customers}</p>
</div>
""", unsafe_allow_html=True)

k4.markdown(f"""
<div class="kpi-card">
<p class="kpi-title">Products Sold</p>
<p class="kpi-value">{total_products}</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# -------------------------------------------------
# Chart Row 1
# -------------------------------------------------
col1, col2 = st.columns(2)

# Monthly Sales Trend
with col1:

    monthly_sales = (
        filtered_df.groupby("Month")["TotalAmount"]
        .sum()
        .reset_index()
    )

    fig1 = px.line(
        monthly_sales,
        x="Month",
        y="TotalAmount",
        markers=True,
        title="Monthly Sales Trend",
        color_discrete_sequence=["#1f77b4"]
    )

    st.plotly_chart(fig1, use_container_width=True)

# Country Sales
with col2:

    country_sales = (
        filtered_df.groupby("Country")["TotalAmount"]
        .sum()
        .reset_index()
        .sort_values(by="TotalAmount", ascending=False)
        .head(10)
    )

    fig2 = px.bar(
        country_sales,
        x="TotalAmount",
        y="Country",
        orientation="h",
        title="Top Countries by Sales",
        color_discrete_sequence=["#2ca02c"]
    )

    st.plotly_chart(fig2, use_container_width=True)

# -------------------------------------------------
# Chart Row 2
# -------------------------------------------------
col3, col4 = st.columns(2)

# Top Products
with col3:

    top_products = (
        filtered_df.groupby("Description")["Quantity"]
        .sum()
        .reset_index()
        .sort_values(by="Quantity", ascending=False)
        .head(10)
    )

    fig3 = px.bar(
        top_products,
        x="Quantity",
        y="Description",
        orientation="h",
        title="Top Selling Products",
        color_discrete_sequence=["#ff7f0e"]
    )

    st.plotly_chart(fig3, use_container_width=True)

# Sales Distribution
with col4:

    fig4 = px.histogram(
        filtered_df,
        x="TotalAmount",
        nbins=40,
        title="Sales Distribution",
        color_discrete_sequence=["#9467bd"]
    )

    st.plotly_chart(fig4, use_container_width=True)

# -------------------------------------------------
# Dataset Preview
# -------------------------------------------------
st.subheader("Dataset Preview")

st.dataframe(filtered_df.head(30))