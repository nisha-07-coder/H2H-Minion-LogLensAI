def detect_anomalies(logs):
    anomalies = []
    ip_activity = {}

    # Track activity per IP
    for log in logs:
        ip = log["source_ip"]

        if ip not in ip_activity:
            ip_activity[ip] = {
                "deny_count": 0,
                "ports": set()
            }

        if log["action"] == "DENY":
            ip_activity[ip]["deny_count"] += 1

        ip_activity[ip]["ports"].add(log["port"])

    # Analyze patterns
    for ip, data in ip_activity.items():
        if data["deny_count"] >= 3:
            anomalies.append({
                "ip": ip,
                "type": "Brute Force Attack",
                "detail": "Multiple failed login attempts"
            })

        if len(data["ports"]) >= 3:
            anomalies.append({
                "ip": ip,
                "type": "Port Scan",
                "detail": "Multiple ports accessed"
            })

    return anomalies