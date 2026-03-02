# dashboard/app.py
import streamlit as st
import pandas as pd
from utils import load_data, calculate_anomaly_percentage
from plots import plot_time_series

st.title("Supply Chain Anomaly Dashboard")

# 讀取資料
df = load_data()

# Sidebar filters
sku_list = df['sku'].unique()
selected_sku = st.sidebar.selectbox("Select SKU", sku_list)
start_date = st.sidebar.date_input("Start date", df['date'].min())
end_date = st.sidebar.date_input("End date", df['date'].max())
source_options = st.sidebar.multiselect(
    "Anomaly Source",
    ['anomaly_ml_only', 'anomaly_stat_only', 'anomaly_overlap'],
    default=['anomaly_ml_only','anomaly_stat_only','anomaly_overlap']
)

# 篩選資料
mask = (
    (df['sku'] == selected_sku) &
    (df['date'] >= pd.to_datetime(start_date)) &
    (df['date'] <= pd.to_datetime(end_date))
)
df_filtered = df.loc[mask].copy()

# Summary cards
st.subheader("Anomaly Summary (%)")
summary = calculate_anomaly_percentage(df_filtered)
#st.write(summary)
st.metric("ML Anomaly %", f"{summary['ml_percentage']:.2f}%")

# Plot time series + anomaly markers
st.subheader("Time Series with Anomaly Highlight")
fig = plot_time_series(df_filtered, selected_sku, source_options)
st.plotly_chart(fig, use_container_width=True)

# Table view
st.subheader("Anomaly Table")
st.dataframe(df_filtered)