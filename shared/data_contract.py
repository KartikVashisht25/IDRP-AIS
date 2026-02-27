# shared/data_contract.py

FEATURE_SCHEMA = {
    "ear": float,
    "blink_rate": float,
    "eye_closure_duration": float,
    "head_pitch": float,
    "head_yaw": float,
    "head_roll": float,
    "timestamp": str
}

def validate_feature_vector(feature_dict):
    for key in FEATURE_SCHEMA:
        if key not in feature_dict:
            raise ValueError(f"Missing feature: {key}")
    return True    
