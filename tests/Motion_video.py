import time

from gpiozero import MotionSensor
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput

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
    # Change the output with new motion detected event
    output = FfmpegOutput('test'+str(counter)+'.mp4')

    # Record a video for a set amount of time
    picam2.start_recording(encoder, output)
    time.sleep(5)
    picam2.stop_recording()
    
    print("Recording Stopped")
    counter += 1
    pir.wait_for_no_motion()
    print("Motion Stopped")

