# 🚀 LogLens AI

### From Raw Logs to Smart Decisions

---

## 👥 Team

**Team Name:** Minion++

* Nikath Jahan
* Nisha S

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

Instead of just translating logs, we build a system that **acts like a network analyst**.

LogLens AI:

* Understands logs
* Connects related events
* Explains what is happening
* Suggests what action to take

---

## 🧠 What Makes Our Solution Different

### 🔗 Event-Based Thinking

We do not treat logs individually.
We group multiple logs into meaningful **incidents**.

---

### 🧩 Pattern Detection

We identify patterns such as:

* Repeated login failures
* Port scanning
* Sudden traffic spikes

---

### 🧠 Human-Like Explanation

Instead of technical output, we generate simple insights:

“Multiple failed login attempts detected. This may indicate a brute-force attack.”

---

### 💡 Action Suggestions

We guide the user with next steps:

“Recommended: Block the IP or restrict SSH access.”

---

## ⚙️ How It Works

Raw Logs
↓
Log Parsing (extract important fields)
↓
Pattern Detection & Analysis
↓
Incident Formation (group related logs)
↓
Insight Generation
↓
User-Friendly Output

---

## 🔍 Example

### Input Logs:

Login failed
Login failed
Login failed
Port scan detected

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
* Rule-based logic (pattern detection
* AI for explanation 
* Streamlit (simple UI)

---

## 📂 Project Structure

H2H-Minion-LogLensAI/

* data/ → sample logs
* src/ → parser, analysis, logic
* ui/ → Streamlit app
* docs/ → diagrams
* README.md

---

## 🚧 Current Status

Day 1 — Problem understanding and project design

---

## 🔮 Future Scope

* Real-time log monitoring
* Chat-based interaction (“Explain this log”)
* Integration with security tools
* Advanced attack detection

---
