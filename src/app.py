import streamlit as st
import pandas as pd
import os

from parser import parse_file
from classifier import classify_logs
from anomaly import detect_anomalies
from incident import correlate_incidents
from translator import translate_anomalies
from ip_intelligence import enrich_logs

# ------------------ PAGE CONFIG ------------------
st.set_page_config(page_title="LogLens AI", layout="wide")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
body {
    background-color: #0e1117;
}
.block-container {
    padding-top: 2rem;
}
.metric-box {
    background: #1c1f26;
    padding: 20px;
    border-radius: 10px;
    text-align: center;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------
st.title("🚀 LogLens AI")
st.caption("AI-Powered Network Log Intelligence Dashboard")

st.divider()

# ------------------ LOAD DATA ------------------
base_dir = os.path.dirname(os.path.dirname(__file__))
file_path = os.path.join(base_dir, "data", "sample_logs.txt")

logs = parse_file(file_path)

# ------------------ PROCESS ------------------
logs = enrich_logs(logs)
logs = classify_logs(logs)

anomalies = detect_anomalies(logs)
incidents = correlate_incidents(anomalies)
insights = translate_anomalies(anomalies)

df = pd.DataFrame(logs)

# ------------------ METRICS (CARDS STYLE) ------------------
st.markdown("## 📊 Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-box">
        <h3>📄 Logs</h3>
        <h1>{len(logs)}</h1>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-box">
        <h3>🚨 Anomalies</h3>
        <h1>{len(anomalies)}</h1>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-box">
        <h3>🔥 Incidents</h3>
        <h1>{len(incidents)}</h1>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ------------------ LOG TABLE ------------------
st.markdown("## 📄 Log Data")
st.dataframe(df, use_container_width=True)

st.divider()

# ------------------ TWO COLUMN LAYOUT ------------------
col1, col2 = st.columns(2)

# -------- ANOMALIES --------
with col1:
    st.markdown("## 🚨 Anomalies")
    if anomalies:
        for a in anomalies:
            st.error(f"**{a['type']}**\n\nIP: {a['ip']}\n\n{a['detail']}")
    else:
        st.success("No anomalies detected")

# -------- INCIDENTS --------
with col2:
    st.markdown("## 🔗 Incidents")
    if incidents:
        for i in incidents:
            st.warning(f"**{i['incident']}**\n\nIP: {i['ip']}\n\n{i['detail']}")
    else:
        st.success("No incidents detected")

st.divider()

# ------------------ INSIGHTS ------------------
st.markdown("## 🧠 AI Insights")

for ins in insights:
    st.success(f"""
💡 {ins['message']}

👉 **Recommendation:** {ins['recommendation']}
""")

st.divider()

# ------------------ ANALYTICS ------------------
st.markdown("## 📊 Analytics")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Traffic by Port")
    st.bar_chart(df["port"].value_counts())

    st.markdown("### Traffic by Action")
    st.bar_chart(df["action"].value_counts())

with col2:
    st.markdown("### Severity")
    st.bar_chart(df["category"].value_counts())

    if "ip_type" in df.columns:
        st.markdown("### IP Type")
        st.bar_chart(df["ip_type"].value_counts())

st.divider()

# ------------------ CHAT ------------------
st.markdown("## 💬 Chat Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, msg in st.session_state.messages:
    if role == "user":
        st.markdown(f"🧑 **You:** {msg}")
    else:
        st.markdown(f"🤖 **AI:** {msg}")

user_input = st.text_input("Ask about logs...")

if st.button("Send"):
    if user_input:
        st.session_state.messages.append(("user", user_input))

        if "ip" in user_input.lower():
            ips = set([log["source_ip"] for log in logs])
            response = f"Detected IPs: {', '.join(ips)}"

        elif "anomaly" in user_input.lower():
            response = str(anomalies)

        elif "incident" in user_input.lower():
            response = str(incidents)

        else:
            response = "Ask about logs, anomalies, or incidents."

        st.session_state.messages.append(("assistant", response))

st.divider()

# ------------------ FOOTER ------------------
st.markdown("""
---
🔐 **LogLens AI** 
""")