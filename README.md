# **Face Tracking with Arduino & OpenCV**  

This project implements **real-time face tracking** using **OpenCV** and **cvzone's FaceDetectionModule**, integrated with an **Arduino-controlled servo system**. The servos adjust their position based on the detected face’s movement, making it ideal for **AI-driven camera tracking** or **robotic vision applications**.  

## **🚀 Features**  
✅ Real-time **Face Detection & Tracking** using OpenCV  
✅ **Automatic Servo Control** based on face position  
✅ **Arduino Integration** with servo motors  
✅ **Smooth Motion Mapping** (0-180°) for accurate tracking  
✅ **Plug & Play Setup** with a webcam and Arduino  

## **🛠 Requirements**  
### 🔹 **Software & Libraries**  
- Python 3.x  
- OpenCV, cvzone, NumPy, PyFirmata  
- Arduino IDE  

### 🔹 **Hardware**  
- Arduino board (Uno, Mega, etc.)  
- Two **servo motors (SG90/MG995)**  
- USB Camera or Webcam  
- Jumper Wires  

## **📜 Installation & Usage**  
1️⃣ **Set Up Arduino** – Connect **servos to PWM pins** and upload Arduino code  
2️⃣ **Install Dependencies** – Install required Python libraries  
3️⃣ **Run the Python Script** – Start face tracking  

## **🎯 How It Works**  
- **Face Detection**: The camera detects a face using OpenCV  
- **Position Calculation**: The center of the face is mapped to servo angles  
- **Servo Control**: The servos adjust to keep the face centered  
- **Idle Mode**: If no face is detected, servos remain in the last position   

## **🛠 Troubleshooting**  
🔴 **Face Not Detected?** Improve lighting & check the camera  
🔴 **Servo Motors Not Moving?** Verify Arduino connections & COM port  

## **📌 Future Enhancements**  
🚀 Multi-Face Tracking  
📡 Wireless Control via **ESP32/Bluetooth**  
🎯 Object Tracking Support  

## **📜 License**  
This project is **open-source** under the MIT License. Feel free to modify and enhance it! 🚀
