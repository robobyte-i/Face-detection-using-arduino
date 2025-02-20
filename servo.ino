#include <Servo.h>

Servo servoX; // Servo for X-axis
Servo servoY; // Servo for Y-axis

int servoPinX = 9;  // Servo X on pin 9
int servoPinY = 10; // Servo Y on pin 10

void setup() {
  Serial.begin(9600);  
  servoX.attach(servoPinX);
  servoY.attach(servoPinY);
}

void loop() {
  if (Serial.available() >= 2) {  
    int servoXPos = Serial.read();  
    int servoYPos = Serial.read();  

    // Map values (0-255) to servo angles (0-180 degrees)
    servoXPos = map(servoXPos, 0, 255, 0, 180);
    servoYPos = map(servoYPos, 0, 255, 0, 180);

    // Move servos
    servoX.write(servoXPos);
    servoY.write(servoYPos);
  }
}
