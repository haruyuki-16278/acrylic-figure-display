# パッケージインポート
import serial
import RPi.GPIO as GPIO
from time import sleep

# 定数宣言
ARDUINO_RSTPIN = 4
SERIAL_PORT = '/dev/serial0'

# 初期化
### GPIO設定
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(ARDUINO_RSTPIN, GPIO.OUT)
# GPIO.setwarnings(False)
### シリアル通信(UART)設定
ser = serial.Serial(SERIAL_PORT)
ser.baudrate = 9600

# 関数宣言
### Arduinoにリセットをかける関数
def reset_arduino() -> None:
    GPIO.output(ARDUINO_RSTPIN, True)
    sleep(0.01)
    GPIO.output(ARDUINO_RSTPIN, False)
    sleep(0.01)
    GPIO.output(ARDUINO_RSTPIN, True)

### Arduinoにシリアル通信で文字を送る関数(LCDに表示される)
def send_string(text:str='') -> None:
    while(len(text) < 16):
        text = text+' '
    ser.write(text.encode('utf-8'))

send_string(text='python test')
# GPIO.cleanup()
