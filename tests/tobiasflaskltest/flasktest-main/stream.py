#code for streaming


#were to implement the start_stream() function
#!/usr/bin/python3

# Mostly copied from https://picamera.readthedocs.io/en/release-1.13/recipes2.html
# Run this script, then point a web browser at http:<this-ip-address>:8000
# Note: needs simplejpeg to be installed (pip3 install simplejpeg).

#from stream_test_lib import *

#output_stream = StreamingOutput()
import io
from picamera2 import Picamera2
import time
from picamera2.encoders import MJPEGEncoder
from picamera2.outputs import FileOutput

camera = Picamera2()
camera.configure(camera.create_video_configuration(main={"size": (640, 480)}))
encoder_stream = MJPEGEncoder(10000000)
global buffer, output_stream

# Configure camera settings (e.g., resolution)
#camera.resolution = (640, 480)
#camera.framerate = 30

def start_stream():
    #global output_stream
    #picam2 = Picamera2()
    #picam2.start_recording(JpegEncoder(), FileOutput(output_stream))
    #buffer = io.BytesIO()
    #output_stream = FileOutput(buffer)
    global output_stream
    output_stream = 'stream_jpeg'
    camera.start_recording(encoder_stream, output_stream)


def generate_frames():

    # Create a circular buffer to store video
    #circular_buffer = CircularOutput(camera, io.BufferedIOBase)

    # Start recording
    #camera.start_recording(circular_buffer, format='mjpeg')
    #global output_stream
    #output_stream = 'stream_jpeg'
    try:
        while True:
            # Wait for the next frame
            #camera.start_encoder(encoder_stream, output_stream)

            # Yield the current frame
            yield (b'--FRAME\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + bytes(output_stream, 'utf-8') + b'\r\n')

    finally:
        camera.stop_recording()

