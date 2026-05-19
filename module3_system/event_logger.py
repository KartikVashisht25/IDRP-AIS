import csv
import os
from datetime import datetime

from module3_system.database import (
    initialize_database,
    insert_event
)

LOG_FILE = "driver_logs.csv"


def initialize_log():

    initialize_database()

    if not os.path.exists(LOG_FILE):

        with open(LOG_FILE, mode="w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                "Timestamp",
                "Risk",
                "EAR",
                "BlinkRate",
                "Yawning",
                "HeadDirection",
                "GazeDirection",
                "DistractionDuration",
            ])


def log_event(
    risk,
    ear,
    blink,
    yawning,
    head_direction,
    gaze_direction,
    distraction_duration
):

    important_event = False

    if risk != "SAFE":
        important_event = True

    if yawning:
        important_event = True

    if head_direction != "CENTER":
        important_event = True

    if gaze_direction != "CENTER":
        important_event = True

    if distraction_duration > 3:
        important_event = True

    if not important_event:
        return

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    # CSV Logging
    with open(LOG_FILE, mode="a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([

            timestamp,

            risk,
            round(ear, 3),
            round(blink, 2),

            yawning,
            head_direction,
            gaze_direction,

            round(distraction_duration, 2)
        ])

    # Database Logging
    insert_event(

        timestamp=timestamp,

        risk=risk,

        ear=round(ear, 3),

        blink_rate=round(blink, 2),

        yawning=yawning,

        head_direction=head_direction,

        gaze_direction=gaze_direction,

        distraction_duration=round(
            distraction_duration,
            2
        )
    )