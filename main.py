import cv2
import time

from module1_vision.camera_stream import start_camera
from module1_vision.feature_extractor import extract_features

#from module2_ml.predictor import predict_risk
from module3_system.decision_engine import evaluate_risk
from module3_system.alert_system import trigger_alert
from module3_system.database import log_prediction, initialize_database
from module3_system.dashboard import show_dashboard

from module2_ml.lstm_predictor import predict_lstm

print("🚀 System Starting...")

def run():
    initialize_database()

    # ⏱ System control variables
    start_time = time.time()
    last_alert_time = 0
    risk_counter = 0

    for frame in start_camera():

        features = extract_features(frame)

        if features is None:
            continue

        # ✅ ML Prediction
        #prediction = predict_risk(features)

        prediction = predict_lstm(features)

        # ⛔ If not enough sequence yet
        if prediction is None:
            continue

        # ✅ Decision Engine
        decision = evaluate_risk(prediction, features)

        current_time = time.time()

        # ⏱ Ignore first 5 seconds (stabilization phase)
        if current_time - start_time < 5:
            continue

        # 🧠 Risk confirmation logic
        if decision["alert_level"] == "HIGH RISK":
            risk_counter += 1
        else:
            risk_counter = 0

        # 🚨 Trigger alert (with cooldown)
        #print("DEBUG ALERT:", decision["alert_level"], "RiskCounter:", risk_counter)
        # 🔥 FORCE TEST SOUND
        #trigger_alert({"alert_level": "HIGH RISK"})
        if risk_counter > 3:  # 4 consecutive HIGH RISK → trigger alert
            if current_time - last_alert_time > 2:
                trigger_alert(decision)
                last_alert_time = current_time

        # 🗄️ Log data
        log_prediction(features, prediction, decision)

        # 📊 Dashboard output
        show_dashboard(features, prediction, decision)

        # 🎯 UI Overlay
        cv2.putText(frame, f"EAR: {features['ear']}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        cv2.putText(frame, f"Blink: {features['blink_rate']}", (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

        cv2.putText(frame, f"Risk: {decision['alert_level']}", (20, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow("Driver Monitoring", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    run()