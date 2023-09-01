import time
import datetime
from gpiozero import Button
from signal import pause
from picamera2 import Picamera2, Preview
from picamera2.outputs import FfmpegOutput

button = Button(27)
picam = Picamera2()

def get_file_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

picam.start()
for _ in range(150):
    if button.is_pressed:
        file_name_photo = get_file_name()
        picam.capture_file('Photos/'+file_name_photo+'.jpg')
    else:
        time.sleep(0.1)
    
picam.close()
        
