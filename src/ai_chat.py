from collections import Counter

def generate_response(query, logs, anomalies, incidents):
    query = query.lower()

    total_logs = len(logs)
    total_anomalies = len(anomalies)
    total_incidents = len(incidents)

    # ------------------ SUMMARY ------------------
    if any(word in query for word in ["summary", "overview", "report"]):
        return f"""
📊 SYSTEM SUMMARY

• Total Logs: {total_logs}
• Anomalies Detected: {total_anomalies}
• Incidents Identified: {total_incidents}

⚡ The system has analyzed network activity and identified potential security threats.
"""

    # ------------------ IP ANALYSIS ------------------
    elif "ip" in query:
        ips = list(set([log["source_ip"] for log in logs]))
        return f"""
🌐 IP ANALYSIS

Detected IP addresses:
{', '.join(ips)}

⚠️ These IPs were involved in network activity and may require monitoring.
"""

    # ------------------ ANOMALIES ------------------
    elif any(word in query for word in ["anomaly", "attack", "threat"]):
        if not anomalies:
            return "✅ No anomalies detected. Network looks safe."

        response = "🚨 THREATS DETECTED:\n\n"
        for a in anomalies:
            response += f"• {a['type']} from IP {a['ip']}\n"

        response += "\n⚠️ These indicate suspicious or malicious behavior."
        return response

    # ------------------ INCIDENTS ------------------
    elif "incident" in query:
        if not incidents:
            return "✅ No incidents detected."

        response = "🔥 INCIDENT ANALYSIS:\n\n"
        for i in incidents:
            response += f"• {i['incident']} involving IP {i['ip']}\n"

        response += "\n⚠️ These are coordinated attack patterns."
        return response

    # ------------------ RECOMMENDATION ------------------
    elif any(word in query for word in ["fix", "solution", "prevent", "recommend"]):
        return """
🛡️ SECURITY RECOMMENDATIONS

• Block suspicious IP addresses
• Enable firewall rules
• Monitor repeated login attempts
• Restrict unnecessary open ports
• Use intrusion detection systems

⚡ These actions can reduce future attacks.
"""

    # ------------------ DEFAULT ------------------
    else:
        return """
🤖 I can help you analyze logs.

Try asking:
• "Give me summary"
• "Show anomalies"
• "Which IP is suspicious?"
• "Any incidents?"
• "How to prevent attacks?"
"""