import json
import time
import random
import requests
from datetime import datetime

# ELASTIC CONFIG
ELASTIC_URL = "http://192.168.0.242:9200/logs_realtime/_doc"

AUTH = ('elastic', 'fcBS6I6O4_nFFfDBoEko')   # Change if needed
VERIFY_SSL = False  # Only if you’re using self-signed SSL

# Example fields for network/system logs
log_levels = ["INFO", "WARN", "ERROR", "CRITICAL"]
actions = ["login_attempt", "file_access", "port_scan", "dns_query", "firewall_block"]

def generate_log():
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "level": random.choice(log_levels),
        "action": random.choice(actions),
        "source_ip": f"192.168.0.{random.randint(1,255)}",
        "destination_ip": f"10.0.0.{random.randint(1,255)}",
        "port": random.randint(20, 1024),
        "protocol": random.choice(["TCP", "UDP"]),
        "message": "Simulated log event for monitoring system"
    }
    return log

def send_log(log):
    try:
        response = requests.post(ELASTIC_URL, auth=AUTH, verify=VERIFY_SSL, json=log)
        if response.status_code in [200, 201]:
            print(f"[✅ Sent] {log['action']} from {log['source_ip']}")
        else:
            print(f"[❌ Error {response.status_code}] {response.text}")
    except Exception as e:
        print(f"⚠️ Connection error: {e}")

if __name__ == "__main__":
    print("🚀 Sending logs to Elasticsearch in real time...")
    while True:
        log = generate_log()
        send_log(log)
        time.sleep(2)  # Adjust frequency (every 2 sec)

