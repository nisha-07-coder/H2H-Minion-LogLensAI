# 🚀 LogLens AI

### From Raw Logs to Smart Decisions

---

## ❗ Problem

Network logs are generated continuously in systems, but they are difficult to understand.

Example:
SRC=192.168.1.10 PORT=22 ACTION=DENY

Such logs are:

* Hard to interpret
* Time-consuming to analyze
* Difficult for beginners and even tiring for experts

This leads to delayed detection of security threats and slower incident response.

---

## 💡 Our Idea

Instead of building just a log translator, we designed a system that **acts like a network analyst**.

LogLens AI:

* Understands logs
* Connects related events
* Explains what is happening
* Suggests what action to take

---

## 🧠 Core Capabilities (Aligned with Problem Statement)

### 🔍 Log Parsing

Extracts structured information such as source IP, destination, port, and action from raw logs (Syslog, SNMP, VPC Flow Logs).

---

### 🚨 Anomaly Detection

Identifies unusual patterns such as:

* Repeated login failures
* Port scanning activity
* Sudden traffic spikes

---

### ⚠️ Log Categorization

Each event is classified as:

* 🔴 **Critical** — attacks or security threats
* 🟡 **Warning** — suspicious or unusual behavior
* 🟢 **Informational** — normal activity

---

### 🧠 Natural Language Output

Converts technical logs into simple, human-readable insights:

> “Multiple failed SSH login attempts detected. This may indicate a brute-force attack.”

---

### ⏱️ Time-to-Clarity Metric

Traditional analysis:

* Requires reading multiple logs manually
* Takes minutes to understand an issue

With LogLens AI:

* Logs are instantly translated into insights
* Time reduced from minutes → seconds

Example:

* Without tool: ~2–3 minutes
* With LogLens AI: < 10 seconds

---

## 🔥 What Makes Our Solution Different

### 🔗 Event-Based Thinking

Logs are grouped into meaningful **incidents** instead of being analyzed individually.

---

### 🧩 Pattern Detection & Correlation

Multiple logs are connected to detect coordinated behavior.

---

### 💡 Actionable Recommendations

System suggests next steps:

> “Recommended: Block the IP or restrict SSH access.”

---

## ⚙️ How It Works  

Raw Logs  
   ↓  
Log Parsing  
   ↓  
Structured Data  
   ↓  
Pattern Detection & Analysis  
   ↓  
Incident Formation  
   ↓  
Classification (Critical / Warning / Info)  
   ↓  
Insight Generation  
   ↓  
User-Friendly Output (Dashboard)  

---

## 🔍 Example

### Input Logs:

-Login failed
-Login failed
-Login failed
-Port scan detected


### Output:

“Suspicious activity detected. Repeated login failures followed by a port scan may indicate a potential attack.”

---

## 🎯 Goal

To reduce the **time between seeing a log and understanding what to do**

From minutes → to seconds

---

## 🛠️ Tech Stack

* Python
* Regex (log parsing)
* Pandas (data handling)
* Rule-based logic (pattern detection)
* AI for explanation
* Streamlit (UI)

---

## 📂 Project Structure  

```
H2H-Minion-LogLensAI/

├── data/
│   └── sample_logs.txt
│
├── src/
│   ├── parser.py
│   ├── classifier.py
│   ├── anomaly.py
│   ├── incident.py
│   └── translator.py
│
├── ui/
│   └── app.py
│
├── docs/
│   └── architecture.png
│
├── requirements.txt
└── README.md
```
## 🚧 Current Status

Day 1 — Problem understanding and system design

---

## 🔮 Future Scope

* Real-time log monitoring
* Chat-based interaction (“Explain this log”)
* Integration with security tools
* Advanced attack detection

---
## 👥 Team

**Team Name:** Minion++

* Nikath Jahan
* Nisha S

---

