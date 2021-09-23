# パッケージインポート
import serial
import RPi.GPIO as GPIO
from time import sleep

# 定数宣言
SERIAL_PORT = '/dev/serial0'

### シリアル通信(UART)設定
ser = serial.Serial(SERIAL_PORT)
ser.baudrate = 9600

# 関数宣言
### Arduinoにリセットをかける関数
def reset_arduino() -> None:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    sleep(0.01)
    GPIO.cleanup()

### Arduinoにシリアル通信で文字を送る関数(LCDに表示される)
def send_string(text:str='') -> None:
    while(len(text) < 16):
        text = text+' '
    ser.write(text.encode('utf-8'))

send_string(text='python test')
sleep(10)
reset_arduino()