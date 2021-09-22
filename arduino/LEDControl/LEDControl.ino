int i=0, j=0;
byte cnt=255;

byte LED_power[4][3] = {
    {0xD2, 0xB9, 0xDE},
    {0x00, 0x00, 0x8B},
    {0xEE, 0xFF, 0xB4},
    {0x48, 0xD1, 0xEE}
};

byte LED_pins[4][3] = {
    {5, 9, 13},
    {4, 8, 12},
    {3, 7, 11},
    {2, 6, 10}
};

void setup() {
    int i;
    for(i=2; i<=13; i++)
    {
        pinMode(i, OUTPUT);
    }
}

void loop() {
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
}
