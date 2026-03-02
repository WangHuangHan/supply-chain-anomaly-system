# dashboard/utils.py
import pandas as pd

def load_data(file_path="data/processed/ml_vs_statistical.csv"):
    df = pd.read_csv(file_path)
    df['date'] = pd.to_datetime(df['date'])
    return df

def calculate_anomaly_percentage(df):
    """
    回傳每個 SKU anomaly 百分比，給 summary cards / trend 使用
    """
    total = len(df)
    ml_count = df['anomaly_ml_only'].sum()
    stat_count = df['anomaly_stat_only'].sum()
    overlap_count = df['anomaly_overlap'].sum()
    return {
        'ml_percentage': ml_count / total * 100,
        'stat_percentage': stat_count / total * 100,
        'overlap_percentage': overlap_count / total * 100
    }