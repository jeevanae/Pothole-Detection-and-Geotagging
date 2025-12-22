import cv2
from ultralytics import YOLO
from datetime import datetime
import csv
import os

model = YOLO("runs/detect/train3/weights/best.pt")
cap = cv2.VideoCapture(0)

# Create CSV file if not exists
csv_file = "pothole_log.csv"
file_exists = os.path.isfile(csv_file)

with open(csv_file, mode="a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["time", "class", "confidence"])

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, conf=0.4)

        for box in results[0].boxes:
            cls_id = int(box.cls[0])
            cls_name = model.names[cls_id]
            conf = float(box.conf[0])

            if "pothole" in cls_name.lower():
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                writer.writerow([now, cls_name, conf])
                print("Pothole logged:", now, cls_name, conf)

        annotated = results[0].plot()
        cv2.imshow("Detection", annotated)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
