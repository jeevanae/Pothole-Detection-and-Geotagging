import subprocess
import sys
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

print("[SYSTEM] Started")

processes = []

def run_python(script):
    return subprocess.Popen(
        [sys.executable, os.path.join(BASE_DIR, script)]
    )

def run_http_server():
    return subprocess.Popen(
        [sys.executable, "-m", "http.server", "8000"],
        cwd=BASE_DIR
    )

try:
    # 1️⃣ Start detection + GPS
    processes.append(run_python("detect_and_geotag.py"))
    print("[DETECT] Detection and geotagging started")

    # 2️⃣ Start CSV → JSON updater
    processes.append(run_python("csv_to_json.py"))
    print("[CSV] CSV to JSON conversion started")

    # 3️⃣ Start HTTP server (map hosting)
    processes.append(run_http_server())
    print("[SERVER] HTTP server running at port 8000")

    # 🔒 Keep system alive
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("[SYSTEM] Stopping")
    for p in processes:
        p.terminate()
