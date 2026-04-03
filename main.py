import cv2

from module1_vision.camera_stream import start_camera
from module1_vision.feature_extractor import extract_features

from module2_ml.predictor import predict_risk
from module3_system.decision_engine import evaluate_risk
from module3_system.alert_system import trigger_alert
from module3_system.database import log_prediction, initialize_database
from module3_system.dashboard import show_dashboard


def run():
    initialize_database()

    for frame in start_camera():

        features = extract_features(frame)

        if features is None:
            continue

        prediction = predict_risk(features)
        decision = evaluate_risk(prediction, features)

        trigger_alert(decision)
        log_prediction(features, prediction, decision)
        show_dashboard(features, prediction, decision)

        # UI Overlay
        cv2.putText(frame, f"EAR: {features['ear']}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)

        cv2.putText(frame, f"Blink: {features['blink_rate']}", (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,0), 2)

        cv2.putText(frame, f"Risk: {decision['alert_level']}", (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

        cv2.imshow("Driver Monitoring", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()