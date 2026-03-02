# models/statistical_detector.py

import pandas as pd
import numpy as np


def detect_statistical_anomalies(df,
                                 demand_z_threshold=2.5,
                                 inventory_drop_threshold=-50,
                                 lead_time_spike_threshold=2):
    """
    Statistical baseline anomaly detection.
    """

    df = df.copy()

    # ===== Demand Anomaly =====
    df["demand_anomaly"] = np.abs(df["demand_zscore"]) > demand_z_threshold

    # ===== Inventory Sudden Drop =====
    df["inventory_anomaly"] = df["inventory_diff"] < inventory_drop_threshold

    # ===== Lead Time Spike =====
    df["lead_time_anomaly"] = df["lead_time_diff"] > lead_time_spike_threshold

    # ===== Combine Overall Internal Anomaly =====
    df["internal_anomaly"] = (
        df["demand_anomaly"] |
        df["inventory_anomaly"] |
        df["lead_time_anomaly"]
    )

    return df


if __name__ == "__main__":
    df = pd.read_csv("data/processed/featured_mrp_data.csv")
    df["date"] = pd.to_datetime(df["date"])

    df = detect_statistical_anomalies(df)

    df.to_csv("data/processed/statistical_results.csv", index=False)

    print("Statistical anomaly detection completed.")