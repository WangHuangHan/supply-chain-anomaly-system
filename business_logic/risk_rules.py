# business_logic/risk_rules.py

def assign_risk_level(row):
    """
    根據 anomaly 組合 + 業務條件決定風險等級
    """

    if row["anomaly_overlap"]:
        return "HIGH"

    if row["ml_only"] and row["inventory_diff"] < -50:
        return "HIGH"

    if row["stat_only"]:
        return "MEDIUM"

    return "LOW"