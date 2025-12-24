from flask import Flask, Response
from prometheus_client import (
    Counter,
    Gauge,
    generate_latest,
    CONTENT_TYPE_LATEST,
)
import time
import threading

app = Flask(__name__)

# Metrics
REQUESTS = Counter("app_requests_total", "Total HTTP requests")
MEMORY_OBJECTS = Gauge("app_memory_objects", "Simulated memory leak objects")

leak = []

def memory_leak_simulator():
    while True:
        leak.append("x" * 1024)  # simulate leak
        MEMORY_OBJECTS.set(len(leak))
        time.sleep(5)

@app.route("/")
def home():
    REQUESTS.inc()
    return "pre-app running\n"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    t = threading.Thread(target=memory_leak_simulator, daemon=True)
    t.start()
    app.run(host="0.0.0.0", port=8000)

