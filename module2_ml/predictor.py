import joblib
import numpy as np
from shared.data_contract import validate_feature_vector
from module3_system.decision_engine import evaluate_risk
from module3_system.database import initialize_databse, log_prediction
from datetime import datetime


#RISK LABEL MAPPING
RISK_LABELS = {
    0:"SAFE",
    1:"MODERATE RISK",
    2:"HIGH RISK"
}

# LOAD TRAINED MODEL
MODEL_PATH = "module2_ml/model/risk_model.pkl"
model = joblib.load(MODEL_PATH)

def predict_risk(feature_dict):
    """
    Accepts a feature dictionary
    
    Returns risk class, label and probability scores
    """

    # Validate input structure
    validate_feature_vector(feature_dict)
    # Convert dictionary to ordered feature array
    feature_array = np.array([[
        feature_dict["ear"],
        feature_dict["blink_rate"],
        feature_dict["eye_closure_duration"],
        feature_dict["head_pitch"],
        feature_dict["head_yaw"],
        feature_dict["head_roll"]
    ]])

    # Predict Class
    risk_class = model.predict(feature_array)[0]

    # Predict Probabilities
    probabilities = model.predict_proba(feature_array)[0]

    return {
        "risk_class": int(risk_class),
        "risk_label": RISK_LABELS[risk_class],
        "probabilities":{
            "SAFE": float(probabilities[0]),
            "MODERATE": float(probabilities[1]),
            "HIGH": float(probabilities[2])
        }
    }

if __name__ == "__main__":

    initialize_databse()

    sample_feature = {
        "ear": 0.18,
        "blink_rate": 30,
        "eye_closure_duration": 1.5,
        "head_pitch": 15,
        "head_yaw": 10,
        "head_roll": 5,
        "timestamp": str(datetime.now())
    }

    result = predict_risk(sample_feature)
    decision = evaluate_risk(result)

    log_prediction(sample_feature, result, decision)

    print("\nPrediction Result:")
    print(result)

    print("\nDecision Result:")
    print(decision)

    print("\nLog saved to databse!")

    
        