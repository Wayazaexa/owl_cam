from gpiozero import MotionSensor

# Setup
pir = MotionSensor(4)

# Infinite loop that prints when motion is detected and when it stops
while True:
	pir.wait_for_motion()
	print("Motion Detected")
	pir.wait_for_no_motion()
	print("Motion Stopped")
