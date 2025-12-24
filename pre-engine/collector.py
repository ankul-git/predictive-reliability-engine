import os
import requests
import time

PROM_URL = os.getenv("PROM_URL", "http://localhost:9090")
QUERY = "app_memory_objects"

print("🔮 Predictive Reliability Engine started")

def fetch_metric():
    r = requests.get(
        f"{PROM_URL}/api/v1/query",
        params={"query": QUERY},
        timeout=5
    )
    r.raise_for_status()
    return float(r.json()["data"]["result"][0]["value"][1])

while True:
    try:
        value = fetch_metric()
        print(f"[INFO] app_memory_objects = {value}")
    except Exception as e:
        print(f"[ERROR] {e}")
    time.sleep(10)

