# Module3_system/Database.py
import sqlite3

from datetime import datetime

DB_PATH = "data/idrp_ais.db"

def initialize_databse():
    """
    Create databse and table if not exists
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS driver_logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            ear REAL,
            blink_rate INTEGER,
            eye_closure_duration REAL,
            head_pitch REAL,
            head_yaw REAL,
            head_roll REAL,
            risk_class INTEGER,
            risk_label TEXT,
            alert_level TEXT
        )
    """)
    
    conn.commit()
    conn.close()

def log_prediction(feature_dict, prediction_result, decision_result):
    """
    Insert new log entry into database
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO  driver_logs(
            timestamp,
            ear,
            blink_rate,
            eye_closure_duration,
            head_pitch,
            head_yaw,
            head_roll,
            risk_class,
            risk_label,
            alert_level
        )VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,(
        feature_dict["timestamp"],
        feature_dict["ear"],
        feature_dict["blink_rate"],
        feature_dict["eye_closure_duration"],
        feature_dict["head_pitch"],
        feature_dict["head_yaw"],
        feature_dict["head_roll"],
        prediction_result["risk_class"],
        prediction_result["risk_label"],
        decision_result["alert_level"],
    ))

    conn.commit()
    conn.close()

def fetch_all_logs():
    """
    Retrieve all logs
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM driver_logs")
    rows = cursor.fetchall()

    conn.close()
    return rows    
