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
button_take_pic = Button(27)
button_start_stream = Button(22)
button_capture_vid = Button(23)
button_stop_stream = Button(24)

picam = Picamera2()
#vid_config = picam.create_video_configuration(main={"size": (1280, 720)}, lores={"size": (640, 480)})
vid_config = picam.create_video_configuration(main={"size": (640, 480)})
pic_config = picam.create_still_configuration({"size": (1920, 1080)})
picam.configure(vid_config)

try:
    

def get_file_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")

def button_1_take_pic():
    print("button 1 is pressed")
    picam.switch_mode(pic_config)
    file_name_photo = get_file_name()
    picam.capture_file('photos/'+file_name_photo+'.jpg')

def button_2_streaming():
    print("button 2 is pressed")
    picam.switch_mode(vid_config)
    picam.start_recording(JpegEncoder(), FileOutput(output_stream))
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()

    finally:
        return

def button_3_recording():
    print("button 3 is pressed")
    picam.switch_mode(vid_config)
        
    encoder_vid = H264Encoder(10000000)
        
    file_name = get_file_name()
        
    picam.start_recording(encoder_vid, FfmpegOutput('videos/'+file_name+'.mp4'))
    time.sleep(7)
    picam.stop_recording()
    
streaming = False
picam.start()

while True:
    if button_take_pic.is_pressed:
        
        button_1_take_pic()
        #photo_thread = threading.Thread(target=button_1_take_pic)
        #photo_thread.start()
        button_take_pic.wait_for_release()
        
    elif button_start_stream.is_pressed:
        if not streaming:
            stream_thread = threading.Thread(target=button_2_streaming)
            stream_thread.start()
        else:
            picam.stop_recording()
        streaming = not streaming
        button_start_stream.wait_for_release()
         
    elif button_capture_vid.is_pressed:
        video_thread = threading.Thread(target=button_3_recording)
        video_thread.start()
        button_capture_vid.wait_for_release()
    elif button_stop_stream.is_pressed:
        print('Button 4 pressed. Good job!')
        button_stop_stream.wait_for_release()

    
picam.close()