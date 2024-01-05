#include<Arduino.h>

static const int but_pin = 0;
static const int led_pin = 16;

//globals 

static int buton_state = HIGH;
static int last_button_state = HIGH;
static unsigned long last_debounce_time = 0;
static unsigned long debounce_delay = 50;

void setup()
{
  //configure serial
  Serial.begin(115200);//baud RAD_TO_DEG
  while(!Serial);
  pinMode(led_pin,OUTPUT);
  pinMode(but_pin,INPUT_PULLUP);
}

void loop()
{
  int reading = digitalRead(but_pin);

if(reading != last_button_state)
{
  last_debounce_time = millis();
}

if((millis() - last_debounce_time) > debounce_delay)
{
  if(reading != buton_state)
  {
    buton_state = reading;
    if(buton_state == LOW)
    {
      Serial.println("Hello hari,sucessful execution");
    }
  }
}
last_button_state = reading;
}
/*
const int but_pin = 0;     
const int led_pin = 13;      
const unsigned long interval = 1000;  
unsigned long lastPressTime = 0;     
int pressCount = 0;                  

void setup() {
  Serial.begin(115200);
  while(!Serial);
  pinMode(but_pin, INPUT_PULLUP);
  pinMode(led_pin, OUTPUT);
  
}

void loop() {
  int buttonState = digitalRead(but_pin);
  
 
  if (buttonState == LOW) {
    digitalWrite(led_pin, HIGH);  
    lastPressTime = millis();    
    pressCount++;                
    delay(300);                  
  }
  
  
  if (millis() - lastPressTime >= interval) {
    digitalWrite(led_pin, LOW);   
    if (pressCount > 0) {
      Serial.print("Button pressed ");
      Serial.print(pressCount);
      Serial.println(" times");
    }
    pressCount = 0;              
  }
}*/








