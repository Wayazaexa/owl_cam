from gpiozero import MotionSensor
import time
from picamera2 import Picamera2, Preview

# Setup
picam = Picamera2()
config= picam.create_preview_configuration()
picam.configure(config)
picam.start_preview(Preview.QTGL)

# Show input from camera sensor and delay for 2 seconds
picam.start()
time.sleep(2)

# Take a picture and close the camera object
picam.capture_file("test_python.jpg")
picam.close()

