import time
import datetime
from multiprocessing import Process

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
    
global streaming
picam.start()

while True:
    if button_take_pic.is_pressed:
        photo_thread = Process(target=button_1_take_pic)
        photo_thread.start()
        button_take_pic.wait_for_release()
        photo_thread.join()
        
    elif button_start_stream.is_pressed:
        if not streaming:
            print(streaming)
            stream_thread = Process(target=button_2_streaming)
            stream_thread.start()
        else:
            print(streaming)
            picam.stop_recording()
            stream_thread.join()
        streaming = not streaming
        button_start_stream.wait_for_release()
         
    elif button_capture_vid.is_pressed:
        video_thread = Process(target=button_3_recording)
        video_thread.start()
        video_thread.join()
        button_capture_vid.wait_for_release()
    elif button_stop_stream.is_pressed:
        stream_thread.terminate()
        print('server murdered successfully?')
        button_stop_stream.wait_for_release()
    


picam.close()
