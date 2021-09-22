#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16,2);
String incoming = "";
String tmp = "";

void setup() {
    lcd.init();
    lcd.backlight();
    lcd.setCursor(0, 0);
    lcd.print("MORE MORE JUMP!");
    Serial.begin(9600);
    pinMode(13, OUTPUT);
    pinMode(2, OUTPUT);
}

void loop() {
    incoming = "";
    while (Serial.available()) 
    {
        digitalWrite(13, HIGH);
        delay(100);
        digitalWrite(13, LOW);
        tmp = (char)Serial.read();
        if (tmp != -1)
        {
            incoming += tmp;
        }
        else
        {
            break;
        }
    }
    if (incoming != "") 
    {
        digitalWrite(2, HIGH);
        Serial.read();
        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print(incoming);
        Serial.print("I received: "); // 受信データを送りかえす
		Serial.println(incoming);
        digitalWrite(2, LOW);
    }
}