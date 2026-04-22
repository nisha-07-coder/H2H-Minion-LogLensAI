# 🚀 LogLens AI  
### 🧠 From Raw Logs to Smart Security Intelligence

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/AI-Powered-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

---

## 📌 Overview

**LogLens AI** is an intelligent cybersecurity platform that transforms raw network logs into:

- 📊 Structured data  
- 🚨 Detected threats  
- 🔗 Correlated incidents  
- 🧠 Human-readable insights  

It acts like a **virtual SOC analyst**, helping security teams understand threats faster and respond smarter.

---

## 🎯 Problem Statement

Modern systems generate huge volumes of logs that are:

- ❌ Complex and unstructured  
- ⏳ Time-consuming to analyze  
- 🧠 Difficult to interpret  

➡️ Result: **Delayed threat detection & slow incident response**

---

## 💡 Solution

LogLens AI simplifies log analysis by:

- 🔍 Parsing raw logs  
- 🚨 Detecting anomalies  
- 🏷️ Classifying severity  
- 🔗 Correlating incidents  
- 🧠 Translating logs into plain English  
- 💡 Providing actionable recommendations  

---

## 🧱 Architecture

```
Raw Logs
   ↓
Log Parsing (Regex)
   ↓
Structured Data (JSON)
   ↓
Classification Engine
   ↓
Anomaly Detection
   ↓
Incident Correlation
   ↓
AI Insight Generator
   ↓
Streamlit Dashboard
```

---

## 🔥 Features

### 🔍 Log Parsing
- Extracts IP, Port, Action, Timestamp  
- Converts raw logs → structured format  

---

### 🚨 Anomaly Detection
Detects:
- Brute Force Attacks  
- Port Scanning  
- Suspicious Patterns  

---

### 🔗 Incident Correlation
Combines multiple events into **attack stories**

> Example:  
> Failed logins + multi-port access → **Coordinated attack**

---

### 🧠 AI Log Translator
Transforms logs into human language:

> “Multiple failed login attempts detected → Possible brute-force attack.”

---

### 💡 Recommendations Engine
- Block malicious IP  
- Restrict ports  
- Monitor suspicious activity  

---

### 📊 Interactive Dashboard
- KPI cards (Logs, Anomalies, Incidents)  
- Threat level indicator 🔥  
- Attack timeline  
- Charts & analytics  
- Chat-based assistant  

---

## ⚙️ Tech Stack

| Layer        | Technology |
|-------------|------------|
| Backend      | Python |
| Data         | Pandas |
| Parsing      | Regex |
| UI           | Streamlit |
| AI Layer     | Rule-based / LLM-ready |
| ML (Optional)| Scikit-learn |

---

## 📂 Project Structure

```
H2H-Minion-LogLensAI/

├── data/
│   └── sample_logs.txt
│
├── src/
│   ├── app.py
│   ├── parser.py
│   ├── classifier.py
│   ├── anomaly.py
│   ├── incident.py
│   ├── explainer.py
│   ├── ip_intelligence.py
│   ├── ip_geo.py
│   └── ai_chat.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

```bash
git clone https://github.com/nisha-07-coder/H2H-Minion--LogLensAI.git
cd H2H-Minion-LogLensAI
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
cd src
streamlit run app.py
```

---

## 📊 Example Output

```json
{
  "source_ip": "192.168.1.10",
  "port": 22,
  "action": "DENY",
  "category": "CRITICAL",
  "ip_type": "Private Network"
}
```

---

## ⏱️ Time-to-Clarity

| Scenario            | Time |
|--------------------|------|
| Manual Analysis     | 2–3 min |
| Using LogLens AI    | < 10 sec |

---

## 🔐 Use Cases

- 🛡️ Security Operations Center (SOC)  
- ⚡ Incident Response  
- 🔍 Threat Detection  
- 📊 SIEM Enhancement  
- 🎓 Cybersecurity Learning  

---

## 🧠 Innovation Factor

✔ Solves real-world cybersecurity problem  
✔ Reduces analysis time drastically  
✔ Converts technical logs → human insights  
✔ Combines rule-based + AI thinking  
✔ Not just a dashboard — a **decision system**

---

## 🔮 Future Enhancements

- ⚡ Real-time log streaming  
- 💬 Advanced AI chat (LLM integration)  
- 🌍 IP geolocation visualization  
- 🤖 ML-based anomaly detection  
- 🔗 Integration with tools like Splunk  

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to fork and submit pull requests.

---

## 📜 License

MIT License

---

## 👥 Team

**Team Name:** Minion++

- Nisha S  
- Nikath Jahan  

---

## ⭐ Show Your Support

If you like this project:

⭐ Star the repo  
