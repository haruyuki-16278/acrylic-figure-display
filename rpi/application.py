# パッケージインポート
import serial
import RPi.GPIO as GPIO
from time import sleep
from playsound import playsound as ps

# 定数宣言
SERIAL_PORT = '/dev/serial0'
ARDUINO_RSTPIN = 4
LEFT_BTN = 21
CENTER_BTN = 20
RIGHT_BTN = 16

# 初期化
### GPIO設定
GPIO.setmode(GPIO.BCM)
GPIO.setup(ARDUINO_RSTPIN, GPIO.OUT)
GPIO.setup(LEFT_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(CENTER_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RIGHT_BTN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
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

try:
    reset_arduino()
    while(True):
        if not GPIO.input(LEFT_BTN):
            while(not GPIO.input(LEFT_BTN)):
                sleep(0.01)
            send_string('left')
            print('left')
        if not GPIO.input(CENTER_BTN):
            while(not GPIO.input(CENTER_BTN)):
                sleep(0.01)
            send_string('center')
            print('center')
        if not GPIO.input(RIGHT_BTN):
            while(not GPIO.input(RIGHT_BTN)):
                sleep(0.01)
            send_string('right')
            print('right')

finally:
    GPIO.cleanup()