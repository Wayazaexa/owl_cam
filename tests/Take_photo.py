import time
import datetime

from picamera2 import Picamera2, Preview
from picamera2.outputs import FfmpegOutput

def get_file_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")


file_name_photo = get_file_name()
picam = Picamera2()

picam.start()
time.sleep(2)
picam.capture_file('Photos/'+file_name_photo+'.jpg')
picam.close()