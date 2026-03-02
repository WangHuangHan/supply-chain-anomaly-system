# models/isolation_forest_detector.py

import joblib
import os
import pandas as pd
from sklearn.ensemble import IsolationForest

FEATURE_COLUMNS = [
    "demand_diff",
    "demand_zscore",
    "inventory_diff",
    "inventory_rolling_mean",
    "lead_time_diff",
    "lead_time_rolling_mean"
]

def train_and_save_model(df, model_path="models/isolation_forest.pkl",random_state=42, contamination=0.1):
    """
    Use Isolation Forest to detect anomalies in MRP features and save the model for future use.
    """
    df = df.copy()

    # 取得特徵欄位
    X = df[FEATURE_COLUMNS]

    # 建立 Isolation Forest 模型
    model = IsolationForest(
        n_estimators=100,
        max_samples="auto",
        contamination=contamination,
        random_state=random_state
    )

    # 訓練模型
    model.fit(X)

    # 確保資料夾存在並儲存
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"模型已儲存至: {model_path}")
    return model



if __name__ == "__main__":
    # 1.讀取處理後的 MRP 數據
    df = pd.read_csv("data/processed/featured_mrp_data.csv")
    df["date"] = pd.to_datetime(df["date"])
    
    # 2.訓練模型並儲存
    model = train_and_save_model(df)
    
    # 3.預測 anomaly (-1 = anomaly, 1 = normal)
    X = df[FEATURE_COLUMNS]
    df["ml_anomaly"] = model.predict(X) == -1

    # 4.儲存結果
    df.to_csv("data/processed/ml_results.csv", index=False)
    print("Isolation Forest anomaly detection completed.")