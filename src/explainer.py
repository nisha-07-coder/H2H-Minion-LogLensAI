def explain_anomalies(anomalies):
    explanations = []

    for a in anomalies:
        if a["type"] == "Brute Force Attack":
            msg = f"⚠️ Multiple failed login attempts detected from IP {a['ip']}. This may indicate a brute-force attack. Recommended: Block the IP or monitor login attempts."

        elif a["type"] == "Port Scan":
            msg = f"⚠️ IP {a['ip']} is trying multiple ports. This indicates a possible port scanning activity. Recommended: Restrict access or investigate further."

        else:
            msg = f"⚠️ Suspicious activity detected from IP {a['ip']}."

        explanations.append(msg)

    return explanations
