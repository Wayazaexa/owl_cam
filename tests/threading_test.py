import time
import datetime
import threading

from gpiozero import Button
from signal import pause
from picamera2 import Picamera2, Preview
from picamera2.outputs import FfmpegOutput
from picamera2.encoders import H264Encoder


from stream_test_lib import * 

#buttons
button1 = Button(27)
button2 = Button(22)
button3 = Button(23)

picam = Picamera2()
picam.configure(picam.create_video_configuration(main={"size": (640, 480)}))

def get_file_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

def button_1_take_pic():
    print("button 1 is pressed")
    file_name_photo = get_file_name()
    picam.capture_file('Photos/'+file_name_photo+'.jpg')

def button_2_streaming():
    print("button 2 is pressed")
    picam.start_recording(JpegEncoder(), FileOutput(output_stream))
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
            
    finally:
        return

def button_3_recording():
    print("button 3 is pressed")
        
    encoder_vid = H264Encoder(10000000)
        
    file_name = get_file_name()
        
    picam.start_recording(encoder_vid, FfmpegOutput('videos/'+file_name+'.mp4'))
    time.sleep(5)
    picam.stop_recording()
    
control = 0
picam.start()
while True:
    if button1.is_pressed:
          photo_thread = threading.Thread(target=button_1_take_pic)
          photo_thread.start()
          time.sleep(0.1)
     
    elif button2.is_pressed:
        
        if control == 0:
             stream_thread = threading.Thread(target=button_2_streaming)
             stream_thread.start()
             control +=1
        else:
            picam.stop_recording()
            control -=1
    
        time.sleep(0.1)
         
         
    elif button3.is_pressed:
         video_thread = threading.Thread(target=button_3_recording)
         video_thread.start()
        
    
    time.sleep(0.1)
        

    
picam.close()