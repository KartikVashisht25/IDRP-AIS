<div align="center">

<h1>🚗 IDRP-AIS</h1>
<h3>Intelligent Driver Risk Prediction & Adaptive Intervention System</h3>

<p><em>Real-time AI-powered driver monitoring that detects fatigue, distraction, and attention loss — before they cause accidents.</em></p>
</div>

---

## Overview

Driver fatigue and distraction are among the leading causes of road accidents worldwide. **IDRP-AIS** addresses this by continuously analyzing a driver's facial behavior through a live camera feed, using computer vision and machine learning to detect dangerous states in real time — and intervening before a crisis occurs.

The system doesn't just monitor. It **acts**: triggering adaptive alerts, sending Telegram emergency notifications, logging events for analytics, and rendering a live risk dashboard — all within milliseconds.

---

## What It Detects

| Behavior | Detection Method |
|---|---|
| 😴 Eye closure / drowsiness | Eye Aspect Ratio (EAR) |
| 🥱 Yawning | Mouth Aspect Ratio (MAR) |
| 👁️ Excessive blinking | Blink rate tracking |
| 👀 Unsafe gaze direction | Gaze vector estimation |
| 🧠 Head pose deviation | Pitch / Yaw / Roll estimation |
| 🚨 Overall driver risk level | AI + rule-based decision engine |

---

## System Architecture

```
Camera Feed
    │
    ▼
Face Landmark Detection  (MediaPipe)
    │
    ▼
Feature Extraction  (EAR · MAR · Gaze · Head Pose · Blink Rate)
    │
    ▼
AI Risk Prediction  (LSTM + Rule-Based Decision Engine)
    │
    ▼
   ┌──────────────────────────────────────┐
   │          Adaptive Intervention        │
   ├─────────────┬────────────┬───────────┤
   │  🔊 Alert   │ 📲 Telegram│ 📊 Dashboard│
   │   Sound     │   Alert    │  Warning  │
   └─────────────┴────────────┴───────────┘
    │
    ▼
🗄️ Database Logging  (SQLite + CSV)
```

---

## Core Features

### 🎥 Real-Time Vision Pipeline
Processes a live webcam stream frame-by-frame using MediaPipe's face mesh, extracting 468 facial landmarks per frame to power all downstream detections.

### 👁️ Fatigue & Blink Detection
Calculates the **Eye Aspect Ratio (EAR)** continuously. When eyes remain closed beyond a configurable threshold, or blink frequency spikes abnormally, the system flags fatigue.

### 🥱 Yawn Detection
The **Mouth Aspect Ratio (MAR)** tracks mouth openness over time. Repeated yawning — a key early indicator of driver fatigue — triggers escalating alert levels.

### 👀 Gaze & Head Pose Tracking
6-DoF head pose estimation (pitch, yaw, roll) combined with iris-based gaze tracking detects when a driver looks away from the road — left, right, up, or down — and for how long.

### 🚨 Adaptive Alert System
Alerts scale with risk level:
- **Low risk** → passive dashboard indicator
- **Medium risk** → audio alert
- **High risk** → audio alert + Telegram emergency notification

### 📊 Live Streamlit Dashboard
A fully interactive dashboard displays all metrics in real time:
EAR · MAR · Blink Rate · Gaze Direction · Head Direction · Pitch/Yaw/Roll · Risk Level · Session Statistics · Fatigue & Distraction Alerts

### 🗄️ Event Logging & Analytics
Every detected event is persisted to an SQLite database and exported as CSV — enabling post-session analysis, driver reports, and long-term trend monitoring.

---

## Project Structure

```
IDRP-AIS/
│
├── Assets/                    # Alert audio files
│   ├── alert.mp3
│   └── alert1.wav
│
├── data/
│   └── idrp_ais.db            # SQLite event database
│
├── module1_vision/            # Computer vision pipeline
│   ├── camera_stream.py
│   ├── ear_calculator.py
│   ├── fatigue_detector.py
│   ├── feature_extractor.py
│   ├── gaze_tracker.py
│   ├── head_pose_estimator.py
│   ├── landmark_detector.py
│   └── yawn_detector.py
│
├── module2_ml/                # Machine learning & prediction
│   ├── lstm_data_preparation.py
│   ├── lstm_model.py
│   ├── lstm_predictor.py
│   ├── predictor.py
│   ├── train_lstm.py
│   └── train_module.py
│
├── module3_system/            # Alerts, dashboard, logging
│   ├── alert_system.py
│   ├── dashboard.py
│   ├── database.py
│   ├── decision_engine.py
│   ├── event_logger.py
│   └── telegram_alert.py
│
├── analytics_dashboard.py     # Historical analytics view
├── live_dashboard.py          # Real-time Streamlit dashboard
├── main.py                    # Core monitoring loop
├── start_app.py               # Application entry point
└── requirements.txt
```

---

## Technology Stack

| Category | Tools |
|---|---|
| Language | Python 3.10 |
| Computer Vision | OpenCV, MediaPipe |
| Machine Learning | TensorFlow, Keras, Scikit-learn |
| Dashboard | Streamlit, Plotly |
| Data Handling | NumPy, Pandas |
| Database | SQLite3 |
| Alerts | Pygame, Telegram Bot API |
| Version Control | Git, GitHub |

---

## Getting Started

### Prerequisites
- Python 3.10
- Webcam
- (Optional) Telegram Bot token for emergency alerts

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/KartikVashisht25/IDRP-AIS.git
cd IDRP-AIS

# 2. Create and activate a virtual environment
python -m venv venv310
venv310\Scripts\activate        # Windows
# source venv310/bin/activate   # macOS / Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the live dashboard
streamlit run live_dashboard.py
```

> To configure Telegram alerts, add your bot token and chat ID to the relevant config section in `module3_system/telegram_alert.py`.

---

## Alert Trigger Conditions

The decision engine fires alerts when any of the following thresholds are exceeded:

- Eyes closed continuously beyond the configured duration
- Yawn frequency surpasses the fatigue progression threshold
- Gaze directed away from road for more than the distraction window
- Head pose deviation (left/right/up/down) sustained beyond safe limits
- Composite risk score crosses the HIGH RISK boundary

All thresholds are configurable to adapt to different drivers and environments.

---

## Risk Level Classification

| Level | Condition | Response |
|---|---|---|
| ✅ SAFE | All metrics within normal range | Dashboard monitoring only |
| ⚠️ MEDIUM RISK | One or more metrics approaching threshold | Audio alert triggered |
| 🚨 HIGH RISK | Multiple metrics in danger zone | Audio + Telegram alert |

---

## Roadmap

- [ ] Driver identity recognition (per-driver baseline calibration)
- [ ] Voice-based alert system
- [ ] Cloud dashboard & fleet monitoring integration
- [ ] Mobile companion app
- [ ] Automated PDF session reports
- [ ] Full LSTM training pipeline with labeled dataset
- [ ] Advanced post-session analytics dashboard

---

## Why IDRP-AIS?

Most driver monitoring systems on the market are either expensive hardware integrations or simple single-metric detectors. IDRP-AIS is a **multi-signal, AI-driven system** that:

- Combines **6+ behavioral signals** into a unified risk score
- Operates entirely on a **standard webcam** — no specialized hardware needed
- Provides **adaptive intervention** that escalates with risk, rather than binary on/off alerts
- Maintains a **full audit trail** for post-incident analysis

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## Developed By

**Kartik Vashisht**  
AI Developer · Computer Vision · ML Systems  
[GitHub](https://github.com/KartikVashisht25)

---

<div align="center">
  <p>If IDRP-AIS is useful to you, consider giving it a ⭐ on GitHub — it helps others find the project.</p>
</div>
