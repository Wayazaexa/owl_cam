import time
import datetime
from gpiozero import Button
from signal import pause
from picamera2 import Picamera2, Preview
from picamera2.outputs import FfmpegOutput
from picamera2.encoders import H264Encoder

from stream_test_lib import * 

#buttons
button = Button(27)
button2 = Button(22)
button3 = Button(23)

picam = Picamera2()
picam.configure(picam.create_video_configuration(main={"size": (640, 480)}))

def get_file_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

picam.start()
while True:
    if button.is_pressed:
        
        print("button 1 is pressed")
        
        file_name_photo = get_file_name()
        picam.capture_file('Photos/'+file_name_photo+'.jpg')
    elif button2.is_pressed:
        print("button 2 is pressed")
        picam.start_recording(JpegEncoder(), FileOutput(output_stream))
        try:
            address = ('', 8000)
            server = StreamingServer(address, StreamingHandler)
            server.serve_forever()
            
        finally:
            picam.stop_recording()
    elif button3.is_pressed:
        print("button 3 is pressed")
        
        encoder_vid = H264Encoder(10000000)
        
        file_name = get_file_name()
        
        picam.start_recording(encoder_vid, FfmpegOutput('videos/'+file_name+'.mp4'))
        #picam.start_encoder(encoder_vid, output_vid, name="main")
        time.sleep(5)
        picam.stop_recording()
        #picam.stop_encoder(encoder_vid)
        
    
    time.sleep(0.1)
        

    
picam.close()