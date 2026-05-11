# 🚗 Intelligent Driver Risk Prediction & Adaptive Intervention System (IDRP-AIS)

## 📌 Overview

The **Intelligent Driver Risk Prediction & Adaptive Intervention System (IDRP-AIS)** is an AI-powered real-time driver monitoring system designed to detect fatigue, drowsiness, and driver risk levels using Computer Vision and Machine Learning.

The system continuously analyzes facial behavior such as eye closure, blink rate, and head movement to predict risk and trigger adaptive alerts for improved road safety.

---

## 🎯 Key Features

* 🎥 Real-time camera-based monitoring (OpenCV)
* 👁️ Facial landmark detection using MediaPipe
* 📊 Eye Aspect Ratio (EAR) for fatigue detection
* 🔁 Blink rate & eye closure duration tracking
* 🤖 Machine Learning-based risk prediction (Random Forest)
* 🧠 Hybrid Decision Engine (ML + rule-based logic)
* 🚨 Real-time alert system (sound + console alerts)
* 🗄️ SQLite database logging
* 📊 Live console dashboard
* 🎯 On-screen UI overlay (live metrics display)

---

## 🧠 System Architecture

Driver → Camera → Feature Extraction → ML Prediction → Decision Engine → Alert System → Database

---

## ⚙️ Technologies Used

| Category         | Technology        |
| ---------------- | ----------------- |
| Language         | Python            |
| Computer Vision  | OpenCV, MediaPipe |
| Machine Learning | Scikit-learn      |
| Data Handling    | NumPy, Pandas     |
| Database         | SQLite            |
| Version Control  | Git, GitHub       |

---

## 📂 Project Structure

IDRP(AIS)/
│
├── module1_vision/
│   ├── camera_stream.py
│   ├── landmark_detector.py
│   ├── ear_calculator.py
│   ├── fatigue_detector.py
│   └── feature_extractor.py
│
├── module2_ml/
│   ├── predictor.py
│   ├── train_module.py
│   └── model/
│
├── module3_system/
│   ├── decision_engine.py
│   ├── alert_system.py
│   ├── dashboard.py
│   └── database.py
│
├── shared/
├── main.py
├── requirements.txt
└── README.md

---

## 🚀 How It Works

1. Captures live video using webcam
2. Detects facial landmarks using MediaPipe
3. Computes EAR (Eye Aspect Ratio)
4. Tracks blink rate & eye closure duration
5. Sends features to ML model
6. Predicts driver risk level
7. Applies decision logic
8. Triggers alerts
9. Logs data into database

---

## 📊 Sample Output

EAR: 0.23
Blink Rate: 55.5
Eye Closure Duration: 0.0
Risk: SAFE
Alert: NORMAL

---

## ⚠️ Current Limitations

* No head pose detection yet
* Model trained on mock/synthetic data
* No web-based dashboard
* Limited temporal modeling

---

## 🔥 Future Enhancements

### 🧠 AI Improvements

* LSTM-based fatigue detection
* Real dataset training
* Personalized driver behavior

### 👁️ Vision Upgrades

* Head pose estimation
* Eye gaze tracking
* Yawning detection

### 🎯 UI Upgrades

* Streamlit dashboard
* Real-time graphs
* Mobile app integration

### 🚗 IoT Integration

* GPS-based alerts
* Cloud storage (Firebase/AWS)
* Vehicle integration

---

## 🧪 Installation & Setup

### 1. Clone Repository

git clone https://github.com/KartikVashisht25/IDRP-AIS.git
cd IDRP-AIS

---

### 2. Create Virtual Environment

python -m venv venv310
venv310\Scripts\activate

---

### 3. Install Dependencies

pip install -r requirements.txt

---

### 4. Run Project

python main.py

---

## 🧠 Project Highlights

* Real-time AI system
* Modular architecture
* Hybrid intelligence (ML + rules)
* End-to-end pipeline
* Industry-relevant use case

---

## 👨‍💻 Author

Kartik Vashisht
BCA Student | AI Developer

---

## 📌 Note

This project is developed as both:

* Academic Major Project
* Resume & Portfolio Project

---

## ⭐ If you like this project, give it a star!