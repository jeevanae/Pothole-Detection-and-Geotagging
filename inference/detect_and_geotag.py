import cv2
import csv
import os
from datetime import datetime, timedelta
from ultralytics import YOLO

# ===============================
# CONFIG
# ===============================
MODEL_PATH = "runs/detect/train3/weights/best.pt"
CONF_THRESHOLD = 0.3
LOG_INTERVAL_SECONDS = 5
CSV_FILE = "pothole_log.csv"

# Only classes we care about
VALID_CLASSES = ["pothole", "pothole_water", "pothole_water_m"]

# ===============================
# GPS (dummy for now)
# ===============================
def get_gps_location():
    return 10.527641, 76.214443

# ===============================
# SETUP
# ===============================
model = YOLO(MODEL_PATH)
cap = cv2.VideoCapture(0)

last_log_time = datetime.min
file_exists = os.path.isfile(CSV_FILE)

with open(CSV_FILE, mode="a", newline="") as f:
    writer = csv.writer(f)

    if not file_exists:
        writer.writerow([
            "timestamp",
            "class_name",
            "confidence",
            "latitude",
            "longitude"
        ])
        f.flush()

    print("🚀 Pothole detection started")
    print("Logging classes:", VALID_CLASSES)
    print("Press 'q' to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, conf=CONF_THRESHOLD)

        if results[0].boxes is not None:
            for box in results[0].boxes:
                cls_id = int(box.cls[0])
                cls_name = model.names[cls_id]
                conf = float(box.conf[0])

                # 🔑 FILTER ONLY VALID POTHOLE CLASSES
                if cls_name in VALID_CLASSES:
                    now = datetime.now()

                    # Prevent duplicates
                    if (now - last_log_time) >= timedelta(seconds=LOG_INTERVAL_SECONDS):
                        lat, lon = get_gps_location()

                        writer.writerow([
                            now.strftime("%d-%m-%Y %H:%M:%S"),
                            cls_name,
                            round(conf, 3),
                            lat,
                            lon
                        ])
                        f.flush()

                        last_log_time = now

                        print(
                            f"📍 LOGGED | {cls_name} | "
                            f"Conf: {conf:.2f} | "
                            f"Lat: {lat}, Lon: {lon}"
                        )

        annotated = results[0].plot()
        cv2.imshow("Pothole Detection & Geo-tagging", annotated)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
print("✅ Program stopped safely")
