from datetime import datetime

from module1_vision.landmark_detector import get_landmarks
from module1_vision.ear_calculator import calculate_ear
from module1_vision.fatigue_detector import FatigueDetector

fatigue_detector = FatigueDetector()

def extract_features(frame):
    landmarks = get_landmarks(frame)

    if landmarks is None:
        return None

    ear = calculate_ear(landmarks, frame.shape)

    fatigue_data = fatigue_detector.update(ear)

    features = {
        "ear": round(ear, 3),
        "blink_rate": fatigue_data["blink_rate"],
        "eye_closure_duration": fatigue_data["eye_closure_duration"],
        "head_pitch": 0,
        "head_yaw": 0,
        "head_roll": 0,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    return features