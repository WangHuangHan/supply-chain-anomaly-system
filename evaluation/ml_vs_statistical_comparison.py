# evaluation/ml_vs_statistical_comparison.py

import pandas as pd

def compare_ml_vs_statistical(df):
    """
    Compare Isolation Forest anomalies with Statistical baseline anomalies.
    """
    df = df.copy()
    
    # ML anomaly
    ml_anomaly = df["ml_anomaly"]
    
    # Statistical anomaly
    stat_anomaly = df["internal_anomaly"]
    
    # Overlap
    df["anomaly_overlap"] = ml_anomaly & stat_anomaly
    
    # Only ML
    df["anomaly_ml_only"] = ml_anomaly & (~stat_anomaly)
    
    # Only Statistical
    df["anomaly_stat_only"] = stat_anomaly & (~ml_anomaly)
    
    # Summary counts
    summary = {
        "total_records": len(df),
        "ml_anomalies": ml_anomaly.sum(),
        "stat_anomalies": stat_anomaly.sum(),
        "overlap": df["anomaly_overlap"].sum(),
        "ml_only": df["anomaly_ml_only"].sum(),
        "stat_only": df["anomaly_stat_only"].sum()
    }
    
    return df, summary


if __name__ == "__main__":
    # 讀取前面兩層結果
    df_ml = pd.read_csv("data/processed/ml_results.csv")
    df_stat = pd.read_csv("data/processed/statistical_results.csv")

    # 合併
    df = pd.merge(df_ml, df_stat[["date","sku","internal_anomaly"]],
                  on=["date","sku"], how="left")

    df, summary = compare_ml_vs_statistical(df)

    # 儲存結果
    df.to_csv("data/processed/ml_vs_statistical.csv", index=False)

    print("Comparison completed. Summary:")
    for k, v in summary.items():
        print(f"{k}: {v}")