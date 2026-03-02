# business_logic/action_engine.py

def determine_action(risk_level):
    if risk_level == "HIGH":
        return "Send Alert + Create Incident"
    elif risk_level == "MEDIUM":
        return "Notify SCM Dashboard"
    else:
        return "Log Only"