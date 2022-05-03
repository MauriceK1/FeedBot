
#include <Servo.h> 

Servo base;
Servo armRight;
Servo armLeft;
Servo spoon;
int pos;
int temp;
int led = 3;
int x, y;
double angle = 1;
double len;
bool manual = false;
String str;
String sub;
char type;
int LEFT_ARM = 11, RIGHT_ARM = 5, BASE = 9, SPOON = 6;
double UPPER = 26.0, LOWER = 17.0, FULL = 35.0;
int BASE_MIN = 20, BASE_MAX = 160;
int JOY_LEN = 725;

void setup() {
  Serial.begin(9600);
  base.attach(BASE);
  armRight.attach(RIGHT_ARM);
  armLeft.attach(LEFT_ARM);
  spoon.attach(SPOON);

  // setup the mode toggler
  pinMode(2, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(2), toggle, RISING);
  
  pinMode(led, OUTPUT);

  
}

void loop() {
  if (manual) {
    delay(100);
    x = (analogRead(A0) - 512);
    y = (analogRead(A1) - 512);
    angle = atan2(y, x) * (180 / PI);
    base.write(constrain(abs(angle), BASE_MIN, BASE_MAX));
    
    len = hypot(x, y) * (FULL / JOY_LEN);

    Serial.println(getAngle(len, LOWER, UPPER));
    
    //armRight.write(getAngle(UPPER, LOWER, len));
    //armLeft.write(getAngle(len, LOWER, UPPER));
    
  } else {
    if (Serial.available() > 0) {
        str = Serial.readStringUntil('\n');
        type = str[0];
        
        digitalWrite(led, LOW);
        
        if (type == 's') {
          
        } else if (type == 'p') {
          sub = str.substring(1);
          pos = sub.indexOf(',');
          Serial.println(sub.substring(0, pos).toFloat());
          base.write(sub.substring(0, pos).toFloat());
          temp = pos + 1;
          pos = sub.indexOf(',', pos+1);
          Serial.println(sub.substring(temp, pos));
          armRight.write(sub.substring(temp, pos).toFloat());
          temp = pos + 1;
          pos = sub.indexOf('\n');
          Serial.println(sub.substring(temp, pos));
          armLeft.write(sub.substring(temp, pos).toFloat());
        } else if (type == 'e') {
          Serial.println("error");
          digitalWrite(led, HIGH);
        }
    }
  }
}

void toggle() {
  manual = !manual;
  Serial.print("Manual: ");
  Serial.println(manual);
}

// gets the angle based on the three sides, using the Law of Cosines
double getAngle(double adj1, double adj2, double opp) {
  return 180 - acos( (adj1*adj1 + adj2*adj2 - opp*opp)  / (2*adj1*adj2) ) * (180 / PI) ;
}