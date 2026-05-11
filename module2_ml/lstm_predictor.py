import numpy as np
from tensorflow.keras.models import load_model

# Load trained model
model = load_model("module2_ml/model/lstm_model.h5")

# Store recent frames
sequence_buffer = []
SEQUENCE_LENGTH = 10


def predict_lstm(features):

    global sequence_buffer

    # Convert features dict to list
    feature_list = [
        features["ear"],
        features["blink_rate"],
        features["eye_closure_duration"],
        features["head_pitch"],
        features["head_yaw"],
        features["head_roll"]
    ]

    sequence_buffer.append(feature_list)

    # Keep only last 10 frames
    if len(sequence_buffer) > SEQUENCE_LENGTH:
        sequence_buffer.pop(0)

    # Not enough data yet
    if len(sequence_buffer) < SEQUENCE_LENGTH:
        return None

    # Convert to numpy
    sequence = np.array(sequence_buffer)
    sequence = np.expand_dims(sequence, axis=0)

    # Prediction
    prediction = model.predict(sequence)

    predicted_class = np.argmax(prediction)

    labels = ["SAFE", "DROWSY", "HIGH RISK"]

    return {
        "risk_class": int(predicted_class),
        "risk_label": labels[predicted_class]
    }