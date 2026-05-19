import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
from module3_system.database import (
    initialize_database
)
st.set_page_config(layout="wide")
initialize_database()

DB_NAME = "data/idrp_ais.db"

st.set_page_config(layout="wide")

st.title("📊 IDRP-AIS Analytics Dashboard")

connection = sqlite3.connect(DB_NAME)

query = "SELECT * FROM driver_events"

df = pd.read_sql_query(query, connection)

connection.close()

if len(df) == 0:

    st.warning("No event data found.")

    st.stop()

# Metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Events",
    len(df)
)

col2.metric(
    "High Risk Events",
    len(df[df["risk"] == "HIGH RISK"])
)

col3.metric(
    "Yawning Events",
    len(df[df["yawning"] == 1])
)

col4.metric(
    "Distraction Events",
    len(df[df["distraction_duration"] > 2])
)

st.markdown("---")

# Risk Distribution
risk_chart = px.pie(
    df,
    names="risk",
    title="⚠️ Risk Distribution"
)

st.plotly_chart(
    risk_chart,
    use_container_width=True
)

# EAR Trend
ear_chart = px.line(
    df,
    x="timestamp",
    y="ear",
    title="👁️ EAR Trend Over Time"
)

st.plotly_chart(
    ear_chart,
    use_container_width=True
)

# Blink Rate Trend
blink_chart = px.line(
    df,
    x="timestamp",
    y="blink_rate",
    title="👀 Blink Rate Trend"
)

st.plotly_chart(
    blink_chart,
    use_container_width=True
)

# Head Direction Analysis
head_chart = px.histogram(
    df,
    x="head_direction",
    title="🧠 Head Movement Analysis"
)

st.plotly_chart(
    head_chart,
    use_container_width=True
)

# Gaze Analysis
gaze_chart = px.histogram(
    df,
    x="gaze_direction",
    title="👁️ Gaze Direction Analysis"
)

st.plotly_chart(
    gaze_chart,
    use_container_width=True
)

# Raw Data
st.markdown("## 📄 Event Logs")

st.dataframe(
    df,
    use_container_width=True
)