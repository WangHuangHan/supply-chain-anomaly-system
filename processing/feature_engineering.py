# processing/feature_engineering.py

import pandas as pd
import numpy as np


def add_features(df):
    """
    Perform feature engineering for MRP anomaly detection.
    """

    # 依 SKU 分組
    df = df.sort_values(["sku", "date"])

    # ===== Demand Features =====

    # 與前一天差異
    df["demand_diff"] = df.groupby("sku")["actual_demand"].diff()

    # 7天 rolling 平均
    df["demand_rolling_mean"] = (
        df.groupby("sku")["actual_demand"]
        .rolling(window=7)
        .mean()
        .reset_index(level=0, drop=True)
    )

    # Z-score（標準化偏離）
    df["demand_zscore"] = (
        df["actual_demand"] - df["demand_rolling_mean"]
    ) / df.groupby("sku")["actual_demand"].rolling(7).std().reset_index(level=0, drop=True)

    # ===== Inventory Features =====

    df["inventory_diff"] = df.groupby("sku")["inventory_level"].diff()

    df["inventory_rolling_mean"] = (
        df.groupby("sku")["inventory_level"]
        .rolling(window=7)
        .mean()
        .reset_index(level=0, drop=True)
    )

    # ===== Lead Time Features =====

    df["lead_time_diff"] = df.groupby("sku")["lead_time"].diff()

    df["lead_time_rolling_mean"] = (
        df.groupby("sku")["lead_time"]
        .rolling(window=7)
        .mean()
        .reset_index(level=0, drop=True)
    )

    # 移除前幾天因 rolling 產生的 NaN
    df = df.dropna()

    return df


if __name__ == "__main__":
    df = pd.read_csv("data/raw/mrp_data.csv")
    df["date"] = pd.to_datetime(df["date"])

    df = add_features(df)

    df.to_csv("data/processed/featured_mrp_data.csv", index=False)

    print("Feature engineering completed.")