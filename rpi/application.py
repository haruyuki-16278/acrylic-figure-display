# パッケージインポート
import os
import serial
import RPi.GPIO as GPIO
from time import sleep, time
import simpleaudio as sa
import subprocess as sp

# 定数宣言
SERIAL_PORT = '/dev/serial0'
ARDUINO_RSTPIN = 4
LEFT_BTN = 21
CENTER_BTN = 20
RIGHT_BTN = 16
CHIME_FILE = '/home/pi/acrylic-figure-display/rpi/chime.wav'

# 変数宣言
unit_number = 1
music_number = 0
loop_enable = False
musics: dict

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
    ser.write(text.encode('shift-jis'))

### 曲リストを取得する関数
def get_musics_list() -> dict:
    units = sorted(os.listdir('/home/pi/musics'))
    musics = {}
    for unit in units:
        musics[unit] = sorted(os.listdir('/home/pi/musics/'+unit))
    return musics

### ファイル/ディレクトリ名からナンバリングと拡張子を外す関数
def remove_num_and_ext(string: str) -> str:
    return string.split(' ')[1].split('.')[0].replace('_', ' ')

### simpleaudioでファイルを再生する
def play_file(file_path: str = '') -> sa.PlayObject:
    wav_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wav_obj.play()
    return play_obj

### ユニット番号と曲番号をグローバルから取得して再生する
def play_music() -> sa.PlayObject:
    file_name = musics[list(musics.keys())[unit_number]][music_number]
    file_path = '/home/pi/musics/'+list(musics.keys())[unit_number]+'/'+file_name
    send_string(remove_num_and_ext(file_name))
    return play_file(file_path)

### 曲番号を次に進める
def next_music():
    global music_number
    global unit_number
    if music_number + 1 < len(musics[list(musics.keys())[unit_number]]):
        music_number += 1
    elif unit_number + 1 < len(list(musics.keys())):
        unit_number += 1
        music_number = 0
    else:
        unit_number = 0
        music_number = 0

### 曲番号を前に戻す
def prev_music():
    global music_number
    global unit_number
    if not music_number - 1 < 0:
        music_number = music_number - 1
    elif not unit_number - 1 < 0:
        unit_number = unit_number - 1
        music_number = len(musics[list(musics.keys())[unit_number]]) - 1
    else:
        unit_number = len(musics.keys()) - 1
        music_number = len(musics[list(musics.keys())[unit_number]]) - 1

# メインプログラム
try:
    now_playing = play_file(CHIME_FILE)
    reset_arduino()
    musics = get_musics_list()
    now_playing.wait_done()
    send_string('Not playing')
    sleep(3)
    while(True):
        if not GPIO.input(LEFT_BTN):
            while(not GPIO.input(LEFT_BTN)):
                sleep(0.01)
            if now_playing.is_playing():
                now_playing.stop()
            send_string('prev')
            prev_music()
            sleep(2)
            now_playing = play_music()
        if not GPIO.input(CENTER_BTN):
            tmp_time = time()
            while(not GPIO.input(CENTER_BTN)):
                sleep(0.01)
                if(time() - tmp_time > 10):
                    send_string('shutdown')
                    sp.run(('/sbin/shutdown'))
            loop_enable = True
            if now_playing.is_playing():
                now_playing.stop()
                send_string('Not playing')
                loop_enable = False
                continue
            send_string('play music')
            sleep(2)
            now_playing = play_music()
        if not GPIO.input(RIGHT_BTN):
            while(not GPIO.input(RIGHT_BTN)):
                sleep(0.01)
            if now_playing.is_playing():
                now_playing.stop()
            send_string('next')
            next_music()
            sleep(2)
            now_playing = play_music()
        if loop_enable and not now_playing.is_playing():
            next_music()
            now_playing = play_music()

finally:
    GPIO.cleanup()