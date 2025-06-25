## 🚀 Automated System for Product Labeling and Traceability

This project uses a **YOLOv5 object detection model** to detect key labels on product packaging such as:
- Device ID  
- Batch ID  
- Manufacturing Date  
- RoHS Compliance  
- Serial Number

### 📦 Project Structure
```
├── data/
│   └── custom.yaml
├── scripts/
│   └── label_verification.py
│   └── label_inspection_script.py
├── yolov5/
│   ├── train.py
│   ├── detect.py
├── README.md
```

### 🧠 Model Info

- **Model**: YOLOv5 (custom-trained)
- **Classes**: 5 (listed above)
- **Dataset**: Custom annotated QR labels

### 🛠 How It Works

1. YOLO detects bounding boxes around labels.
2. The `label_verification.py` script:
   - Checks if **all 5 labels** are present.
   - Flags missing or duplicated labels.
3. Based on verification:
   - Prints a **green LED** (✔ Accept) or **red LED** (❌ Reject) signal.

