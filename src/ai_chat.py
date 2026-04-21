from collections import Counter

def generate_response(user_input, logs, anomalies, incidents):
    user_input = user_input.lower()

    # -------- SUMMARY --------
    if "summary" in user_input:
        return f"""
📊 Summary:
- Total Logs: {len(logs)}
- Anomalies: {len(anomalies)}
- Incidents: {len(incidents)}
"""

    # -------- IP DETAILS --------
    elif "ip" in user_input:
        ips = [log["source_ip"] for log in logs]
        ip_counts = Counter(ips)

        result = "🌐 IP Activity:\n"
        for ip, count in ip_counts.items():
            result += f"- {ip}: {count} requests\n"

        return result

    # -------- ANOMALIES --------
    elif "anomaly" in user_input:
        if not anomalies:
            return "✅ No anomalies detected."

        result = "🚨 Detected Anomalies:\n"
        for a in anomalies:
            result += f"- {a['type']} from {a['ip']}\n"

        return result

    # -------- INCIDENTS --------
    elif "incident" in user_input:
        if not incidents:
            return "✅ No incidents detected."

        result = "🔥 Incidents:\n"
        for i in incidents:
            result += f"- {i['incident']} from {i['ip']}\n"

        return result

    # -------- ATTACK ANALYSIS --------
    elif "attack" in user_input:
        if anomalies:
            return "⚠️ Suspicious activity detected. Possible brute-force or port scanning."
        else:
            return "✅ No attack patterns detected."

    # -------- DEFAULT --------
    else:
        return "💬 Try asking: summary, anomalies, incidents, IP activity, attacks"