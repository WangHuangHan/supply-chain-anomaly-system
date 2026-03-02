import pandas as pd
from business_logic.risk_rules import assign_risk_level
from business_logic.action_engine import determine_action

def detect_anomaly(model, records):
    df = pd.DataFrame([r.dict() for r in records])
    # -------- Statistical --------
    def statistical_anomaly(df):
        df["stat_anomaly"] = (
            (df["demand_zscore"].abs() > 3)
            | (df["inventory_diff"].abs() > 80)
            | (df["lead_time_diff"].abs() > 5)
        )
        return df
    df = statistical_anomaly(df)

    # -------- ML --------
    features = df[['demand_diff', 'demand_zscore', 'inventory_diff', 'inventory_rolling_mean', 'lead_time_diff', 'lead_time_rolling_mean']]
    predictions = model.predict(features)
    df['ml_anomaly'] = predictions == -1

    # -------- Comparison --------
    def compare_anomalies(df):
        df["anomaly_overlap"] = (
            df["ml_anomaly"] & df["stat_anomaly"]
        )
        df["ml_only"] = (
            df["ml_anomaly"] & ~df["stat_anomaly"]
        )
        df["stat_only"] = (
            df["stat_anomaly"] & ~df["ml_anomaly"]
        )
        return df
    df = compare_anomalies(df)

    # -------- Business Logic --------
    df["risk_level"] = df.apply(assign_risk_level, axis=1)
    df["action"] = df["risk_level"].apply(determine_action)

    return df.to_dict(orient="records")