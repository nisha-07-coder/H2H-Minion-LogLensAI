import streamlit as st
import pandas as pd
import os
import time
from collections import Counter

from parser import parse_file
from classifier import classify_logs
from anomaly import detect_anomalies
from incident import correlate_incidents
from translator import translate_anomalies
from ip_intelligence import enrich_logs
from ai_chat import generate_response

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="LogLens AI", layout="wide")

# ------------------ LIGHT UI CSS ------------------
st.markdown("""
<style>
body {
    background-color: #f5f7fb;
}
.block-container {
    padding-top: 2rem;
}
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
}
.detect-card {
    background: white;
    padding: 15px;
    border-radius: 12px;
    margin: 10px 0;
}
.chat-user {
    text-align:right;
    background:#2563eb;
    color:white;
    padding:10px;
    border-radius:10px;
}
.chat-ai {
    text-align:left;
    background:#ffffff;
    padding:10px;
    border-radius:10px;
    border:1px solid #e5e7eb;
}
.header-box {
    background: linear-gradient(90deg, #0ea5e9, #6366f1);
    padding: 25px;
    border-radius: 15px;
    color: white;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

# ------------------ SIDEBAR ------------------
st.sidebar.title("⚙️ Controls")
run_live = st.sidebar.checkbox("🔴 Simulate Real-Time Logs")

# ------------------ HEADER ------------------
st.markdown("""
<div class="header-box">
<h1>🚀 LogLens AI</h1>
<p>AI-Powered Network Threat Intelligence Dashboard</p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ------------------ LOAD DATA (FIXED) ------------------
current_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(current_dir, ".."))
file_path = os.path.join(base_dir, "data", "sample_logs.txt")

# ✅ IMPORTANT FIX: initialize logs safely
logs = parse_file(file_path)

# ------------------ PROCESS ------------------
if logs is None:
    logs = []

logs = enrich_logs(logs)
logs = classify_logs(logs)

anomalies = detect_anomalies(logs)
incidents = correlate_incidents(anomalies)
insights = translate_anomalies(anomalies)

df = pd.DataFrame(logs)

# ✅ Prevent crash if empty
if df.empty:
    df = pd.DataFrame(columns=["port", "action", "category", "ip_type", "source_ip"])

# ------------------ THREAT SCORE ------------------
score = 0
for a in anomalies:
    if a["type"] == "Brute Force Attack":
        score += 40
    elif a["type"] == "Port Scan":
        score += 30

score += len(incidents) * 50
threat_score = min(100, score)

col1, col2 = st.columns([2,1])

with col1:
    st.markdown("### 🔥 Threat Level")
    st.progress(threat_score / 100)

    if threat_score > 70:
        st.error(f"🚨 HIGH RISK ({threat_score}%)")
    elif threat_score > 40:
        st.warning(f"⚠️ MEDIUM RISK ({threat_score}%)")
    else:
        st.success(f"✅ LOW RISK ({threat_score}%)")

with col2:
    if threat_score > 70:
        st.markdown("## 🔴 UNDER ATTACK")
    else:
        st.markdown("## 🟢 SYSTEM STABLE")

st.divider()

# ------------------ KPI ------------------
def card(title, value):
    st.markdown(f"""
    <div class="card">
        <h4>{title}</h4>
        <h1>{value}</h1>
    </div>
    """, unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    card("📄 Logs", len(logs))
with c2:
    card("🚨 Anomalies", len(anomalies))
with c3:
    card("🔥 Incidents", len(incidents))

st.divider()

# ------------------ TOP IP ------------------
ips = [log.get("source_ip") for log in logs if "source_ip" in log]
if ips:
    top_ip = Counter(ips).most_common(1)[0][0]
    st.warning(f"⚠️ Most Active / Suspicious IP: {top_ip}")

# ------------------ ANALYTICS ------------------
st.markdown("## 📊 Analytics")

col1, col2 = st.columns(2)

with col1:
    if "port" in df.columns:
        st.bar_chart(df["port"].value_counts())
    if "action" in df.columns:
        st.bar_chart(df["action"].value_counts())

with col2:
    if "category" in df.columns:
        st.bar_chart(df["category"].value_counts())

st.divider()

# ------------------ CHAT ------------------
st.markdown("### 💬 Ask LogLens AI")

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(f'<div class="chat-user">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-ai">{msg}</div>', unsafe_allow_html=True)

user_input = st.text_input("Ask about logs...")

if st.button("Send"):
    if user_input:
        st.session_state.messages.append(("user", user_input))

        response = generate_response(user_input, logs, anomalies, incidents)

        st.session_state.messages.append(("assistant", response))

# ------------------ FOOTER ------------------
st.markdown("---\n🔐 LogLens AI")
