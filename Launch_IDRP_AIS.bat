@echo off

cd /d "%~dp0"

call venv310\Scripts\activate

start http://localhost:8501

streamlit run live_dashboard.py

pause