import subprocess
import webbrowser
import threading
import time
import os
import sys


def open_browser():

    time.sleep(5)

    webbrowser.open(
        "http://localhost:8501"
    )


threading.Thread(
    target=open_browser,
    daemon=True
).start()


base_path = os.path.dirname(
    os.path.abspath(__file__)
)

python_path = os.path.join(
    base_path,
    "venv310",
    "Scripts",
    "python.exe"
)

dashboard_path = os.path.join(
    base_path,
    "live_dashboard.py"
)

subprocess.run([
    python_path,
    "-m",
    "streamlit",
    "run",
    dashboard_path
])