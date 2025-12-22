# Inference Module – Pothole Detection & Geo-Tagging

This folder contains the inference pipeline for the **Intelligent Pothole Detection and Geo-Tagging System**.  
It is responsible for detecting road anomalies in real time using a trained YOLOv8 model and logging their GPS locations.

---

## 📌 Purpose
The inference module performs the following tasks:
- Captures live video from a camera
- Detects potholes and related road defects using a trained YOLOv8 model
- Associates each detection with GPS coordinates
- Logs detection details (class, confidence, timestamp, latitude, longitude) into a CSV file

---

## 📂 Files Description

### `detect.py`
- Performs real-time pothole detection using a camera feed
- Displays bounding boxes and class labels
- Does **not** include GPS or logging
- Useful for quick testing and model verification

### `detect_and_geotag.py` ⭐
- **Main inference script**
- Performs pothole detection and GPS geo-tagging
- Logs detection results into a CSV file
- Designed to be extended to embedded platforms (Raspberry Pi / Radxa SBC)

---

## 🧪 Output
The inference process generates a CSV log file containing:
- Timestamp
- Detected class name
- Confidence score
- GPS latitude
- GPS longitude

This data can later be visualized on mapping platforms such as **Google Maps**.

---

## 🚀 Usage

Install dependencies:
```bash
pip install -r requirements.txt
