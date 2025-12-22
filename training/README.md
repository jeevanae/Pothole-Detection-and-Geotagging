# Training Module – Pothole Detection Model

This folder contains the training pipeline for the **Intelligent Pothole Detection and Geo-Tagging System**.  
It is responsible for training a deep learning model capable of detecting potholes and road defects from images.

---

## 📌 Objective
The training module aims to:
- Train a YOLOv8-based object detection model
- Learn multiple road anomaly classes such as potholes, cracks, humps, and damaged surfaces
- Generate a trained model suitable for real-time inference and embedded deployment

---

## 🧠 Model Architecture
- **Model**: YOLOv8 (Ultralytics)
- **Task**: Object Detection
- **Framework**: PyTorch
- **Input Size**: 640 × 640
- **Classes**:
  - pothole
  - pothole_water
  - pothole_water_m
  - crack
  - damage
  - hump
  - vehicle
  - and related road anomalies

---

## 📂 Files Description

### `train.py`
- Main training script
- Loads the dataset configuration
- Trains the YOLOv8 model using transfer learning
- Saves the best-performing model weights

---

## 📊 Dataset
- The dataset was sourced from **Roboflow**
- Includes annotated road images with bounding boxes
- Split into training, validation, and test sets

> ⚠️ Due to size constraints, the dataset is **not included** in this repository.

---

## 🚀 Training Instructions

Install dependencies:
```bash
pip install -r requirements.txt

