import streamlit as st
import cv2
import mediapipe as mp
import time
from module1_vision.feature_extractor import extract_features
from module2_ml.lstm_predictor import predict_lstm
from module3_system.decision_engine import evaluate_risk
from module1_vision.head_pose_estimator import estimate_head_pose
from module1_vision.gaze_tracker import get_gaze_direction
from module1_vision.yawn_detector import calculate_mar
from module3_system.event_logger import(
    initialize_log,
    log_event
)
from module3_system.telegram_alert import send_telegram_alert
from module3_system.alert_system import (
     trigger_alert,
     stop_alert
)
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
st.set_page_config(layout="wide")
st.sidebar.title("🚗 IDRP-AIS")
st.sidebar.markdown("---")

st.sidebar.success("🟢 System Active")
fps_placeholder = st.sidebar.empty()

st.sidebar.markdown("## 📊 MONITORING MODULES")

st.sidebar.write("✅ EAR Tracking")
st.sidebar.write("✅ Blink Detection")
st.sidebar.write("✅ LSTM Fatigue AI")
st.sidebar.write("✅ Risk Prediction")
st.sidebar.write("✅ Alert System")
st.sidebar.write("✅ Head Pose Estimation")
st.sidebar.write("✅ Gaze Tracking")
st.sidebar.write("✅ Yawn Detection")
st.sidebar.write("✅ Distraction Detection")

st.sidebar.markdown("---")

st.sidebar.info("""
👨‍💻 Intelligent Driver Risk Prediction &
Adaptive Intervention System
""")
# st.title("🚗 IDRP-AIS Live Monitoring Dashboard")

st.markdown("""
# 🚗 IDRP-AIS Live Monitoring Dashboard

### Intelligent Driver Risk Prediction & Adaptive Intervention System
""")


# Webcam
CAMERA_INDEX = 1
camera = cv2.VideoCapture(CAMERA_INDEX)

camera.set(cv2.CAP_PROP_FRAME_WIDTH, 200)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 200)
camera.set(cv2.CAP_PROP_BUFFERSIZE, 1)

# Graph data

frame_count = 0
graph_update_counter = 0
prev_time = time.time()
# Streamlit placeholders
frame_placeholder = st.empty()
status_placeholder = st.empty()
yawn_placeholder = st.empty()
fatigue_placeholder = st.empty()
distraction_placeholder = st.empty()
distraction_start_time = None
DISTRACTION_THRESHOLD = 2  # seconds
initialize_log()
last_telegram_alert = 0
telegram_cooldown=15
previous_risk = "SAFE"
yawn_active = False
session_start_time = time.time()
total_yawns = 0
total_high_risk = 0
total_distractions = 0
ear_values = []
session_placeholder = st.sidebar.empty()
face_missing_start = None
while True:
    frame_count += 1

    success, frame = camera.read()
    frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    if frame_count % 2 != 0:
        continue

    if not success:
        st.error("Camera not detected")
        break
    # frame = cv2.resize(frame, (480, 360))

    if not success:
        st.error("Camera not detected")
        break

    # Extract features
    current_time = time.time()
    fps = 1 / (current_time - prev_time)
    prev_time = current_time
    fps_placeholder.metric("⚡ FPS", int(fps))
    try:

            features = extract_features(frame)

    except Exception as e:

        st.error(f"ERROR: {e}")

        continue


    # If face NOT detected
    if features is None:

        frame_rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        frame_placeholder.image(
            frame_rgb,
            channels="RGB",
            width=600
        )

        if face_missing_start is None:

            face_missing_start = time.time()

        missing_duration = (
            time.time() - face_missing_start
        )

        if missing_duration > 2:

            status_placeholder.warning(
                "❕ Face Not Detected"
            )

        continue


    face_missing_start = None


    # Prediction
    prediction = predict_lstm(features)

    # If sequence not ready yet
    if prediction is None:

        continue
    
    #If face NOT detected
# If face NOT detected
# If face NOT detected

    # Decison Engine
    decision = evaluate_risk(prediction, features)

    ear = features["ear"]
    blink = features["blink_rate"]
    risk = decision["alert_level"]
        # Store EAR history
    ear_values.append(ear)

    # Session Summary
    session_duration = round(
        (time.time() - session_start_time) / 60,
        2
    )

    average_ear = round(
        sum(ear_values) / len(ear_values),
        3
    ) if ear_values else 0

    with session_placeholder.container():

        st.markdown("---")

        st.subheader("📊 Session Summary")

        st.write(
            f"⏱️ Duration: {session_duration} min"
        )

        st.write(
            f"🥱 Yawns: {total_yawns}"
        )

        st.write(
            f"🚨 High Risk: {total_high_risk}"
        )

        st.write(
            f"⚠️ Distractions: {total_distractions}"
        )

        st.write(
            f"👁️ Avg EAR: {average_ear}"
        )

    # Convert frame
    frame_rgb = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # Face mesh Detection
    results = face_mesh.process(frame_rgb)

    # Default values
    pitch = 0
    yaw = 0
    roll = 0
    mar = 0
    head_direction = "CENTER"
    gaze_direction = "CENTER"

    # Draw landmarks
    if results.multi_face_landmarks:

        for face_landmarks in results.multi_face_landmarks:

            mar = calculate_mar(face_landmarks)

            pitch, yaw, roll = estimate_head_pose(
                face_landmarks,
                frame.shape
            )

            if pitch > 8:

                head_direction = "UP"

            elif pitch < -8:

                head_direction = "DOWN"

            elif yaw > 10:

                head_direction = "RIGHT"

            elif yaw < -10:

                head_direction = "LEFT"

            else:

                head_direction = "CENTER"

            if mar > 0.28:

                yawn_placeholder.warning("""
                🥱 Yawning Detected
                Driver Fatigue Increasing
                """)

            else:

                yawn_placeholder.empty()

            gaze_direction = get_gaze_direction(
                face_landmarks
            )

            mp_drawing.draw_landmarks(
                image=frame_rgb,
                landmark_list=face_landmarks,
                connections=mp_face_mesh.FACEMESH_TESSELATION,
                landmark_drawing_spec=None,
                connection_drawing_spec=mp_drawing.DrawingSpec(
                    color=(0, 255, 0),
                    thickness=1,
                    circle_radius=1
                )
            )

    # Display camera
    frame_placeholder.image(
        frame_rgb,
        channels="RGB",
        width=600
    )

    # Metrics
    with status_placeholder.container():

        col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

        col1.metric(
            "👁️ Eye Aspect Ratio",
            round(ear, 3)
        )

        col2.metric(
            "👀 Blink Rate",
            round(blink, 2)
        )

        col3.metric(
            "⚠️ Driver Risk",
            risk
        )

        col4.metric("⬆️ Pitch", round(pitch, 2))
        col5.metric("➡️ Yaw", round(yaw, 2))
        col6.metric("🔄 Roll", round(roll, 2))
        col7.metric("👁️ Gaze", gaze_direction)
        col8.metric("🕰️ Head Direction", head_direction)
        col9.metric("🥱 MAR", round(mar, 3))

    # Distraction Detection
    driver_distracted = False

    if gaze_direction in ["LEFT", "RIGHT"]:

        driver_distracted = True

    if abs(yaw) > 15 or abs(pitch) > 15:

        driver_distracted = True

    if driver_distracted:

        total_distractions += 1

        if distraction_start_time is None:

            distraction_start_time = time.time()

        distraction_duration = (
            time.time() - distraction_start_time
        )

        distraction_placeholder.warning(
            f"⚠️ Driver Distracted ({round(distraction_duration,1)}s)"
        )
        if distraction_duration > DISTRACTION_THRESHOLD:
            distraction_placeholder.error("""
            🚨Driver Lost Attention!
               Driver is not focused on road.
                Immediate intervention required.
            """)
            trigger_alert(
                "DRIVER DISTRACTION ALERT"
            )
    else:

        distraction_start_time = None
        distraction_duration = 0

        distraction_placeholder.empty()

    # Yawn detection
    is_yawning = False

    if mar > 0.28:

        if not yawn_active:

            is_yawning = True

            yawn_active = True

    else:
        yawn_active = False

    if is_yawning:

        total_yawns += 1

    # Fatigue alerts
    if risk == "HIGH RISK":

        total_high_risk += 1

        if previous_risk != "HIGH RISK":

            trigger_alert(
                "HIGH RISK DRIVER FATIGUE DETECTED"
            )

        fatigue_placeholder.error("""
        🚨 HIGH RISK DRIVER FATIGUE DETECTED
        """)

        previous_risk = "HIGH RISK"

    elif risk == "MEDIUM RISK":

        fatigue_placeholder.warning("""
        ⚠️ Driver showing fatigue symptoms.
        """)

        previous_risk = "MEDIUM RISK"

    else:

        stop_alert()

        fatigue_placeholder.success("""
        ✅ Driver Status Normal!
        Driver condition currently stable.
        """)

        previous_risk = "SAFE"


        distraction_placeholder.warning(
    f"⚠️ Driver Distracted ({round(distraction_duration,1)}s)"
)