int trigPin = 9;
int echoPin = 10;
int Buzzer = 6;
long duration;
int distance;
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup()
  {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(Buzzer, OUTPUT);
  Serial.begin(9600);
    lcd.begin(16, 2);
  }


void loop() 
  {
  lcd.setCursor(0, 1);
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  
  if (distance > 76.2)
  distance = NULL;
  
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Distance is ");
      lcd.print(distance);
      delay(250);
    
  Serial.print("Distance ");
  Serial.println(distance);
  
    
    if(distance <= 76.2 && distance > 0)
  {     
  tone(Buzzer, 262, 3000);
  }
    else
  noTone(Buzzer);    
  }
