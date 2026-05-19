import sqlite3


DB_NAME = "data/idrp_ais.db"


def initialize_database():

    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS driver_events (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            timestamp TEXT,

            risk TEXT,

            ear REAL,

            blink_rate REAL,

            yawning INTEGER,

            head_direction TEXT,

            gaze_direction TEXT,

            distraction_duration REAL
        )
    """)

    connection.commit()

    connection.close()


def insert_event(
    timestamp,
    risk,
    ear,
    blink_rate,
    yawning,
    head_direction,
    gaze_direction,
    distraction_duration
):

    connection = sqlite3.connect(DB_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO driver_events (

            timestamp,
            risk,
            ear,
            blink_rate,
            yawning,
            head_direction,
            gaze_direction,
            distraction_duration

        )

        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        timestamp,
        risk,
        ear,
        blink_rate,
        yawning,
        head_direction,
        gaze_direction,
        distraction_duration
    ))

    connection.commit()

    connection.close()