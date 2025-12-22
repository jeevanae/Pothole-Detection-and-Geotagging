from ultralytics import YOLO

model = YOLO("runs/detect/train3/weights/best.pt")
print(model.names)
