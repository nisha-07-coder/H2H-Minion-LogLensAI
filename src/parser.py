import re
import os
from classifier import classify_logs
from anomaly import detect_anomalies
from datetime import datetime

# Parse a single log
def parse_log(log):
    pattern = r"SRC=(\S+)\s+PORT=(\d+)\s+ACTION=(\S+)"
    
    match = re.search(pattern, log)
    
    if match:
        return {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "source_ip": match.group(1),
            "port": int(match.group(2)),
            "action": match.group(3)
        }
    return None


# Parse file
def parse_file(file_path):
    parsed_logs = []

    if not os.path.exists(file_path):
        print("⚠️ File not found:", file_path)
        return []

    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parsed = parse_log(line)
                if parsed:
                    parsed_logs.append(parsed)

    except Exception as e:
        print("Error reading file:", e)
        return []

    return parsed_logs

# Main
if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_dir, "data", "sample_logs.txt")

    logs = parse_file(file_path)

    # Classification
    logs = classify_logs(logs)

    # Anomaly detection
    anomalies = detect_anomalies(logs)

    print("Classified Logs:\n")
    for log in logs:
        print(log)

    print("\nDetected Anomalies:\n")
    for a in anomalies:
        print(a)
