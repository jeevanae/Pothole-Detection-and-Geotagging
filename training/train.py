from ultralytics import YOLO

def main():
    model = YOLO("yolov8n.pt")

    model.train(
        data="dataset/data.yaml",  # 👈 FIX HERE
        epochs=30,
        imgsz=640,
        batch=16,
        device=0,
        workers=4
    )

if __name__ == "__main__":
    main()
