# ingestion/sap_loader.py

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def generate_mrp_data(start_date="2024-01-01", days=180, sku_list=None):
    """
    Simulate SAP MRP data.
    """

    if sku_list is None:
        sku_list = ["SKU_A", "SKU_B", "SKU_C"]

    all_data = []

    for sku in sku_list:
        dates = pd.date_range(start=start_date, periods=days)

        # 基本需求波動 + seasonality
        base_demand = 100 + 20 * np.sin(np.linspace(0, 3*np.pi, days))
        noise = np.random.normal(0, 10, days)

        demand = base_demand + noise

        # 加入隨機 spike (異常)
        anomaly_indices = np.random.choice(days, size=5, replace=False)
        demand[anomaly_indices] += np.random.randint(80, 120, size=5)

        inventory = 1000 - np.cumsum(demand * 0.1)
        lead_time = np.random.normal(7, 1, days)

        df = pd.DataFrame({
            "date": dates,
            "sku": sku,
            "forecast_demand": base_demand,
            "actual_demand": demand,
            "inventory_level": inventory,
            "lead_time": lead_time
        })

        all_data.append(df)

    final_df = pd.concat(all_data)
    return final_df


if __name__ == "__main__":
    df = generate_mrp_data()
    df.to_csv("data/raw/mrp_data.csv", index=False)
    print("MRP data generated.")