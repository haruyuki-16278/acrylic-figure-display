// グローバル変数宣言
byte DD = B11111100;
byte 

void setup() {
    // 方向レジスタ操作
    // → に行くほど若い番号のポート
    // ポートDなら 7,6,....,1,0 を Bbbbbbbbb で指定
    // ポートBの上位2ビット(ポート)は水晶発振子があるので気をつける
    DDRD |= B11111100; // D7~0番
    DDRB |= B111111; // D13~8番

    // データレジスタ初期化
    PORTD &= B00000011;
    PORTB &= B000000;
}

void loop() {
  int cnt = 0;
  while(true)
  {
    for (cnt=0; cnt<3; cnt++)
    {
      switch (cnt)
      {
      case 0:
        PORTD |= B00111100;
        PORTD &= B00111111;
        PORTB |= B000000;
        PORTB &= B000000;
        break;
      case 1:
        PORTD |= B11000000;
        PORTD &= B11000011;
        PORTB |= B000011;
        PORTB &= B000011;
        break;
      case 2:
        PORTD |= B00000000;
        PORTD &= B00000011;
        PORTB |= B111100;
        PORTB &= B111100;
        break;
      default:
        break;
      }
      delay(1000);
    }
    cnt = 0;
  }
}
