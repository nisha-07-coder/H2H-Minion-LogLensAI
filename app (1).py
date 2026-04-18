import streamlit as st
import os
from src.parser import parse_file
from src.classifier import classify_logs
from src.anomaly import detect_anomalies

st.title("🚀 LogLens AI")
st.subheader("From Raw Logs to Smart Decisions")

# File path
base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "Data", "sample_logs.txt")

# Process logs
logs = parse_file(file_path)
logs = classify_logs(logs)
anomalies = detect_anomalies(logs)

# Display logs
st.write("### 📄 Classified Logs")
for log in logs:
    st.json(log)

# Display anomalies
st.write("### 🚨 Detected Anomalies")
for a in anomalies:
    st.json(a)