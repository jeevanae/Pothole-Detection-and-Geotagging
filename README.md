# Pothole-Detection-and-Geotagging
AI-based pothole detection and GPS geo-tagging system using YOLOv8 and real-time camera input.

# 🚧 Intelligent Pothole Detection and Geo-Tagging System

## 📌 Overview
This project is an AI-based system designed to **detect potholes and road surface defects** using a deep learning model and **geo-tag their locations using GPS data**.  
A trained YOLOv8 object detection model processes a live camera feed to identify potholes in real time. Each detected pothole is logged along with its **confidence score and geographic coordinates**, enabling further analysis and mapping.

The system aims to provide a **low-cost, scalable solution** for road condition monitoring and smart transportation applications.

---

## 🎯 Objectives
- Detect potholes and related road defects using computer vision
- Perform real-time inference on live camera input
- Geo-tag detected potholes using GPS coordinates
- Log detections into a structured CSV file
- Enable future visualization on Google Maps
- Prepare the system for deployment on a single-board computer

---

## 🧠 How It Works
1. A camera captures live video frames
2. A YOLOv8 model detects potholes and road defects
3. Only pothole-related classes are filtered
4. GPS coordinates are acquired in real time
5. Each valid detection is logged with:
   - Timestamp  
   - Defect class  
   - Confidence score  
   - Latitude & longitude  

Duplicate entries are controlled using time-based filtering.

---

## 🛠️ Technologies Used

### Software
- Python 3
- Ultralytics YOLOv8
- OpenCV
- PySerial
- pynmea2

### Hardware (Current & Planned)
- USB Camera
- u-blox NEO-6M GPS Module
- USB-to-TTL Adapter (CP2102)
- *(Planned)* Radxa / Raspberry Pi SBC

---

## 📂 Dataset
- Dataset sourced from Roboflow
- Exported in YOLOv8 format
- Includes multiple road surface defect classes such as:
  - pothole
  - pothole_water
  - crack
  - damage
  - hump

---

## 📊 Output
Detections are logged in CSV format:



Example:
19-12-2025 14:03:21, pothole, 0.74, 10.527641, 76.214443


---

## 🚀 Current Status
- ✔ Model trained and validated
- ✔ Live detection working
- ✔ Class-wise filtering implemented
- ✔ CSV logging functional
- ✔ GPS integration tested on laptop
- 🔄 Hardware-level testing in progress
- 🔄 SBC deployment planned

---

## 🔮 Future Enhancements
- Google Maps visualization of pothole locations
- Severity estimation based on bounding box size
- Deployment on Radxa / Raspberry Pi
- Cloud database integration
- Dashboard for road maintenance authorities

---

## 📌 Disclaimer
This project is developed as an **academic mini project** for educational purposes.  
Detection accuracy depends on camera quality, lighting conditions, and GPS signal availability.

## Repository Structure
- `training/` : Model training scripts
- `inference/` : Real-time pothole detection and GPS geo-tagging
- `requirements.txt` : Python dependencies


