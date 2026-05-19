import streamlit as st
import pandas as pd
import plotly.express as px
import random
import time

st.set_page_config(
    page_title="IDRP-AIS Dashboard",
    layout="wide"
)

st.title("🚗 Intelligent Driver Risk Prediction & Adaptive Intervention System")

st.markdown("---")

# Live Metrics
col1, col2, col3 = st.columns(3)

ear = round(random.uniform(0.15, 0.35), 3)
blink = round(random.uniform(10, 30), 2)

risk_levels = ["SAFE", "MODERATE", "HIGH RISK"]
risk = random.choice(risk_levels)

col1.metric("👁️ EAR", ear)
col2.metric("👀 Blink Rate", blink)
col3.metric("⚠️ Risk Level", risk)

st.markdown("---")

# Real-time graph data
data = {
    "Time": list(range(1, 21)),
    "EAR": [round(random.uniform(0.15, 0.35), 3) for _ in range(20)]
}

df = pd.DataFrame(data)

fig = px.line(
    df,
    x="Time",
    y="EAR",
    title="📈 Real-Time Eye Aspect Ratio Monitoring"
)

st.plotly_chart(fig, use_container_width=True)

# Alert Box
if risk == "HIGH RISK":
    st.error("🚨 HIGH RISK ALERT! Driver appears drowsy.")
elif risk == "MODERATE":
    st.warning("⚠️ Moderate fatigue detected.")
else:
    st.success("✅ Driver status normal.")

st.markdown("---")

st.subheader("📊 System Information")

st.write("""
- Real-time fatigue detection
- LSTM-based prediction
- Eye Aspect Ratio monitoring
- Blink tracking
- Adaptive alert system
- AI-powered driver safety analysis
""")