
# VehicleSense: Adaptive Sensor-Video Learning for Vehicle Type Identification and Overload Detection

VehicleSense is a real-time multimodal learning framework for automatic vehicle classification (AVC) and overload detection. It fuses visual data (ImageSense) and inertial sensor data (SensorSense) using a late fusion strategy with a trainable meta-classifier.


## Run Locally

Clone the project

1. Download the project folder.

2. Extract the contents.

3. Make sure Python 3.8+ is installed on your system.

4. Open a terminal or command prompt in the project directory and follow the steps:

### Step 1: Extract frames from video
```bash
    python extract_frames.py --input input_video.mp4 --output ./frames/
```


### Step 2: Run CNN model (ImageSense)
```bash
    python cnn_model.py --data ./frames/ --output cnn_predictions.csv
```

### Step 3: Run sensor model (SensorSense)
```bash
    python rf_model.py --input sensor_data.csv --output rf_predictions.csv
```

### Step 4: Run fusion model
```bash
    python fusion_model.py --cnn cnn_predictions.csv --rf rf_predictions.csv --output final_results.csv

```



## Installation

Install required Python libraries:

```bash
  pip install -r requirements.txt
```
You need:

- OpenCV
- NumPy
- scikit-learn
- PyTorch or TensorFlow (for CNN)
- Pandas, SciPy

---

### 🚀 **Deployment**
VehicleSense can be deployed on roadside edge devices such as Raspberry Pi, Jetson Nano, or embedded CPUs for real-time use.

You can connect a camera for video input and mount tri-axial accelerometers for vibration sensing.

The models are light enough to run in real-time on moderate hardware.


---

### 📊 **Features**
- YOLOv8 + ResNet-18 image classification
- Accelerometer-based Random Forest classifier
- Adaptive late fusion via neural meta-classifier
- Real-time overload detection using tilt and suspension energy

---

### 📘 **Usage/Examples**
- Your video is named `input_video.mp4`
- Your sensor data is in `sensor_data.csv`


---

### 🧱 **Tech**
- Python 3.8+
- OpenCV
- PyTorch / TensorFlow
- scikit-learn
- SSIM, FFT, SMOTE
- Sensor data (accelerometer CSVs)

---

### 📍 **Roadmap**
- [x] Frame extraction using SSIM
- [x] CNN classification using YOLO and ResNet
- [x] RF classification using vibration features
- [x] Late fusion with meta-classifier
- [ ] Add GUI for easier use
- [ ] Export as mobile app or dashboard

---

### ❤️ **Acknowledgements**
Thanks to all contributors and institutions involved in data collection at Gorakhpur, Varanasi, and East Champaran.

---
