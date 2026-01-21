import csv
import json
import time
import os

CSV_FILE = "pothole_log.csv"
JSON_FILE = "potholes.json"

def convert():
    data = []

    if not os.path.exists(CSV_FILE):
        return

    with open(CSV_FILE, newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            lat = row.get("latitude")
            lon = row.get("longitude")

            # 🔑 Skip entries without valid GPS
            if lat in (None, "", "NA") or lon in (None, "", "NA"):
                continue

            try:
                data.append({
                    "lat": float(lat),
                    "lon": float(lon),
                    "class": row["class_name"],
                    "confidence": float(row["confidence"]),
                    "timestamp": row["timestamp"]
                })
            except ValueError:
                continue  # skip malformed rows safely

    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    print(" CSV - JSON service running...")
    while True:
        convert()
        time.sleep(2)
