# 🚀 LogLens AI  
### 🧠 From Raw Logs to Smart Security Intelligence

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/AI-Powered-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

---
## ❗ Problem Statement  
Modern systems generate massive volumes of raw logs (Syslog, SNMP traps, VPC Flow Logs). These logs are:

- Unstructured and complex  
- Hard to analyze manually  
- Time-consuming during incidents  

👉 This leads to delayed threat detection and slow incident response in SOC environments.

---

#  💡 Proposed Solution  
LogLens AI solves this problem by building an intelligent log analysis pipeline that:

- Parses raw logs into structured data  
- Detects anomalies and suspicious behavior  
- Classifies log severity  
- Correlates incidents  
- Converts logs into human-readable insights  

👉 Acts as a virtual SOC analyst for faster decision-making.

---

# 🧰 Tech Stack  

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Data Processing:** Pandas  
- **Parsing:** Regex  
- **AI Layer:** Rule-based + chatbot logic  
- **Visualization:** Streamlit Charts  
- **Language:** Python 3.11  

---

#  ⚙️ Features  

- 🔍 Raw log parsing (Syslog-style logs)  
- 🚨 Anomaly detection (Brute force, port scanning)  
- 🏷️ Log classification (Critical / Warning / Info)  
- 🔗 Incident correlation  
- 🧠 SOC AI chatbot assistant  
- 📊 Interactive dashboard  
- 🔥 Threat scoring system  
- 📈 Live log simulation  

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


## ⚙️ Setup & Installation

1. Clone the repository:

```bash
git clone https://github.com/nisha-07-coder/H2H-Minion--LogLensAI.git
cd H2H-Minion-LogLensAI
```

---

2. Create a virtual environment:

### 🔹 For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

### 🔹 For Mac/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```
---

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

4. Run the application:

```bash
cd src
streamlit run app.py
```

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
## Screenshots
<img width="1440" height="900" alt="Screenshot 2026-04-23 at 8 24 48 PM" src="https://github.com/user-attachments/assets/66b73a64-62f0-43cf-8e75-39d7b4db16aa" />
<img width="1440" height="900" alt="Screenshot 2026-04-23 at 8 24 55 PM" src="https://github.com/user-attachments/assets/540ec1e0-43e0-4e23-85a2-ebb6a65953d6" />
<img width="1440" height="900" alt="Screenshot 2026-04-23 at 8 25 09 PM" src="https://github.com/user-attachments/assets/a6aa62e7-8536-46f2-9061-fb05e49a6b17" />
<img width="1440" height="900" alt="Screenshot 2026-04-23 at 8 25 03 PM" src="https://github.com/user-attachments/assets/cdb64337-fad0-4316-9424-fc6e829970e4" />
<img width="1440" height="900" alt="Screenshot 2026-04-23 at 8 29 48 PM" src="https://github.com/user-attachments/assets/6aeeed56-5c4f-414e-a978-f9fe6ad4800c" />
<img width="1440" height="900" alt="Screenshot 2026-04-23 at 8 25 13 PM" src="https://github.com/user-attachments/assets/e64ed42a-4392-4115-94e2-d621768969c8" />
<img width="1440" height="900" alt="Screenshot 2026-04-23 at 8 25 20 PM" src="https://github.com/user-attachments/assets/5f322d12-0182-43c2-a73c-ec6a6550821e" />

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

## 🌐 Deployed Link
The project is deployed using Streamlit Community Cloud.

👉 Live Application:
https://h2h-minion-loglensai.streamlit.app/

## 📜 License

MIT License

---

## 👥 Team

**Team Name:** Minion++

- Nisha S  
- Nikath Jahan  

---
