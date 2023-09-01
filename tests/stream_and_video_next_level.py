import time
import datetime
import threading

from gpiozero import MotionSensor
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput, FileOutput
from stream_test_lib import *

# Setup 
pir = MotionSensor(4)
picam2 = Picamera2()
#stream_config = picam2.create_video_configuration(lores={"size": (640, 480)})
video_config = picam2.create_video_configuration(main={"size": (1280, 720)},
                                                 lores={"size": (640, 480)})
picam2.configure(video_config)
#picture_config = picam2.create_video_configuration(hires={"size": (1920, 1080)})

def get_file_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

def owl_stream():
    #stream
    print("starting stream")

    #picam2.configure(stream_config)
    picam2.start_recording(encoder_stream, FileOutput(output_stream), name="lores")

    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        picam2.stop_recording()
    print("oops, stream stopped")


encoder_vid = H264Encoder(10000000)
encoder_stream = JpegEncoder(10000000)

stream_thread = threading.Thread(target=owl_stream)
stream_thread.start()

counter = 0

# Infinite loop
while True:
    pir.wait_for_motion()
    print("Motion Detected")
    #picam2.configure(video_config)


    # Record a video for a set amount of time
    file_name = get_file_name()
    output_vid = FfmpegOutput('videos/'+file_name+'.mp4')
    #picam2.start_recording(encoder_vid, output_vid)
    picam2.start_encoder(encoder_vid, output_vid, name="main")
    time.sleep(5)
    #picam2.stop_recording()
    picam2.stop_encoder(encoder_vid)
    #picam2.configure(stream_config) # is this needed
    
    print("Recording Stopped")
    counter += 1
    pir.wait_for_no_motion()
    print("Motion Stopped")
    
    
    #stream end
    
    #For testing, break the loop after 2 loops
    

