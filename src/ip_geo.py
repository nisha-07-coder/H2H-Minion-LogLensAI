import requests

def get_ip_location(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()

        return {
            "country": data.get("country", "Unknown"),
            "city": data.get("city", "Unknown"),
            "lat": data.get("lat", 0),
            "lon": data.get("lon", 0)
        }
    except:
        return {
            "country": "Unknown",
            "city": "Unknown",
            "lat": 0,
            "lon": 0
        }


def enrich_with_location(logs):
    for log in logs:
        ip = log["source_ip"]

        # Skip private IPs
        if ip.startswith("192.") or ip.startswith("10.") or ip.startswith("172."):
            log["location"] = "Private Network"
        else:
            loc = get_ip_location(ip)
            log["location"] = f"{loc['city']}, {loc['country']}"
            log["lat"] = loc["lat"]
            log["lon"] = loc["lon"]

    return logs