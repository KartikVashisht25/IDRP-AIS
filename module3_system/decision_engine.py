#MODULE3_SYSTEM/decision_engine.py

def evaluate_risk(prediction_result):
    """
    Takes prediction dictionary from ML module
    Returns decision level and action type
    """

    risk_class = prediction_result["risk_class"]
    probabilities = prediction_result["probabilities"]

    decision = {
        "alert_level": None,
        "action": None
    }

    #SAFE
    if risk_class == 0:
        decision["alert_level"] = "NONE"
        decision["action"] = "No Action Required."

    #MODERATE
    elif risk_class == 1:
        decision["alert_level"] = "WARNING"
        decision["action"] = "Play Soft Alert Sound."

    #HIGH
    elif risk_class == 2:
        decision["alert_level"] = "CRITICAL"
        decision["action"] = "Trigger Loud Alarm And Dashboard Alert."

    return decision            