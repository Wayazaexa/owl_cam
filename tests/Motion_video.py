import time
import datetime
#import subprocess
from gpiozero import MotionSensor
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

def get_file_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

# Setup
pir = MotionSensor(4)
picam2 = Picamera2()
video_config = picam2.create_video_configuration()
picam2.configure(video_config)

encoder = H264Encoder(10000000)
counter = 0

# Infinite loop
while True:
    pir.wait_for_motion()
    print("Motion Detected")
    file_name = get_file_name()
    # Change the output with new motion detected event
    output = FfmpegOutput('videos/'+file_name+'.mp4')

    # Record a video for a set amount of time
    picam2.start_recording(encoder, output)
    time.sleep(5)
    picam2.stop_recording()
    
    print("Recording Stopped")
    counter += 1
    pir.wait_for_no_motion()
    print("Motion Stopped")
    
    # For testing, break the loop after 2 loops
    #if counter == 2:
        #break
