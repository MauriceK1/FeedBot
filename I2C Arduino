#define trigPin 10
#define echoPin 13 
#include <Wire.h>

float duration, distance;


#define SLAVE_ADDRESS 0x04
int number;
int state = 0;


void setup() {
  Serial.begin (9600);

  Wire.begin(SLAVE_ADDRESS);
  Wire.onRequest(sendData);

  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
}

void loop() {
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2);
 
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  duration = pulseIn(echoPin, HIGH);
  distance = (duration / 2) * 0.0344;
  
  if (distance >= 400){
    Serial.print("Distance = ");
    Serial.println("Out of range");
  }
  else {
    Serial.print("Distance = ");
    Serial.print(distance);
    Serial.println(" cm");
    delay(100); 
  }
  delay(1000);
}

void sendData(){
  int y = round(distance);
  Wire.write(y);
}