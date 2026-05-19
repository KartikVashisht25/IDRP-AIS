import subprocess
import sys
import os
import webbrowser
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

dashboard_path = os.path.join(BASE_DIR, "live_dashboard.py")

# Start Streamlit
subprocess.Popen([
    sys.executable,
    "-m",
    "streamlit",
    "run",
    dashboard_path
])

# Wait few seconds
time.sleep(5)

# Open browser automatically
webbrowser.open("http://localhost:8501")