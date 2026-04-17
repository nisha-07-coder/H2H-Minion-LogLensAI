# Function to classify a single log
def classify_log(log):
    if log["action"] == "DENY":
        if log["port"] == 22:
            return "CRITICAL"   # SSH attack
        return "WARNING"
    
    elif log["action"] == "ALLOW":
        return "INFO"
    
    return "UNKNOWN"


# Function to classify all logs
def classify_logs(logs):
    classified = []
    
    for log in logs:
        log["category"] = classify_log(log)
        classified.append(log)
    
    return classified