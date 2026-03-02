# dashboard/plots.py
import plotly.express as px
import pandas as pd

def plot_time_series(df, sku, source_options=['anomaly_ml_only','anomaly_stat_only','anomaly_overlap']):
    """
    draw demand_diff, inventory_diff, lead_time_diff these 3 lines + anomaly marker
    """
    df_sku = df[df['sku'] == sku].copy()
    df_sku = df_sku.sort_values('date')

    # melt 3 lines of time series
    df_lines = df_sku.melt(
        id_vars=['date'],
        value_vars=['demand_diff','inventory_diff','lead_time_diff'],
        var_name='metric',
        value_name='value'
    )

    fig = px.line(
        df_lines,
        x='date',
        y='value',
        color='metric',
        title=f'SKU: {sku} Time Series'
    )

    # add anomaly markers
    for source in source_options:
        anomalies = df_sku[df_sku[source] == True]
        fig.add_scatter(
            x=anomalies['date'],
            y=anomalies['demand_diff'], 
            mode='markers',
            name=f"{source} demand_diff anomaly",
            marker=dict(color='red', size=10)
        )
        fig.add_scatter(
            x=anomalies['date'],
            y=anomalies['inventory_diff'],
            mode='markers',
            name=f"{source} inventory_diff anomaly",
            marker=dict(color='orange', size=10)
        )
        fig.add_scatter(
            x=anomalies['date'],
            y=anomalies['lead_time_diff'],
            mode='markers',
            name=f"{source} lead_time_diff anomaly",
            marker=dict(color='yellow', size=10)
        )

    return fig