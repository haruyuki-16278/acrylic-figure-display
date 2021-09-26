// ライブラリ読み込み
#include <LiquidCrystal_I2C.h>

// LCDインスタンス生成
LiquidCrystal_I2C lcd(0x27, 16,2);

// グローバル変数宣言
String incoming = "";
String tmp = "";
int i=0, j=0;
byte cnt=255;

byte LED_power[4][3] = {
    {0xD2, 0xB9, 0xDE},
    {0x00, 0x00, 0x8B},
    {0xEE, 0xFF, 0xB4},
    {0x48, 0xD1, 0xEE}
};

byte LED_pins[4][3] = {
    {2, 3, 4},
    {5, 6, 7},
    {10, 8, 9},
    {11, 12, 13}
};


void setup() {
    int i;
    for(i=2; i<=13; i++)
    {
        pinMode(i, OUTPUT);
    }
    lcd.init();
    lcd.backlight();
    lcd.setCursor(0, 0);
    lcd.print("MORE MORE JUMP!");
    Serial.begin(9600);
}

void loop() {
    incoming = "";
    cnt--;
    for(i=0; i<4; i++)
    {
        for(j=0; j<3; j++)
        {
            if(cnt == 255) {
                digitalWrite(LED_pins[i][j], HIGH);
            }
            if(cnt == 255 - LED_power[i][j])
            {
                digitalWrite(LED_pins[i][j], LOW);
            }
        }
    }
    while (Serial.available()) 
    {
        delay(100);
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
        Serial.read();
        lcd.setCursor(0, 1);
        lcd.print(incoming);
        Serial.print("I received: "); // 受信データを送りかえす
		Serial.println(incoming);
    }
}
