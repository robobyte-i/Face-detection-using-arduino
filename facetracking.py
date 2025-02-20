import cv2
from cvzone.FaceDetectionModule import FaceDetector
import serial
import numpy as np

# Initialize serial communication (adjust 'COM4' to the correct port)
arduino = serial.Serial('COM4', 9600)  # Use the correct port for your system

cap = cv2.VideoCapture(0)
ws, hs = 1280, 720
cap.set(3, ws)
cap.set(4, hs)

if not cap.isOpened():
    print("Camera couldn't Access!!!")
    exit()

detector = FaceDetector()
servoPos = [90, 90]  # Initial servo position

while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img, draw=False)

    if bboxs:
        fx, fy = bboxs[0]["center"][0], bboxs[0]["center"][1]
        pos = [fx, fy]
        servoX = np.interp(fx, [0, ws], [0, 255])  # Map to 0-255 range
        servoY = np.interp(fy, [0, hs], [0, 255])  # Map to 0-255 range

        # Send data to Arduino (X and Y position as bytes)
        arduino.write([int(servoX), int(servoY)])

        cv2.circle(img, (fx, fy), 80, (0, 0, 255), 2)
        cv2.putText(img, str(pos), (fx+15, fy-15), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
        cv2.line(img, (0, fy), (ws, fy), (0, 0, 0), 2)  # X line
        cv2.line(img, (fx, hs), (fx, 0), (0, 0, 0), 2)  # Y line
        cv2.circle(img, (fx, fy), 15, (0, 0, 255), cv2.FILLED)
        cv2.putText(img, "TARGET LOCKED", (850, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    else:
        cv2.putText(img, "NO TARGET", (880, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)
        cv2.circle(img, (640, 360), 80, (0, 0, 255), 2)
        cv2.circle(img, (640, 360), 15, (0, 0, 255), cv2.FILLED)
        cv2.line(img, (0, 360), (ws, 360), (0, 0, 0), 2)  # X line
        cv2.line(img, (640, hs), (640, 0), (0, 0, 0), 2)  # Y line

    cv2.putText(img, f'Servo X: {int(servoPos[0])} deg', (50, 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.putText(img, f'Servo Y: {int(servoPos[1])} deg', (50, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
