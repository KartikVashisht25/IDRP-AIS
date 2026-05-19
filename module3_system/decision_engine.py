def evaluate_risk(prediction, features):

    if prediction > 0.7:

        risk = "HIGH RISK"

    elif prediction > 0.4:

        risk = "MEDIUM RISK"

    else:

        risk = "SAFE"

    return {
        "alert_level": risk
    }