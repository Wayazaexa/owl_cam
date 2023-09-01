import time, subprocess

# Logging function
def AddLog(status):
    # Add line to status log
    logFile = open('restartlog.txt', 'a')
    timeString = time.asctime(time.localtime(time.time()))
    logFile.write('%s %s\n' % (timeString, status))
    # Force the log to be written out
    logFile.flush()
    logFile.close()

# Start the process first time
cam_process = subprocess.Popen(['python', 'Motion_video.py'])
AddLog('Started')

while True:
    # Check the state of the process
    status = cam_process.poll()

    if status != None:
        # Terminated, restart process
        cam_process = subprocess.Popen(['python', 'Motion_video.py'])
        print ('Termination code %d, restarted' % (status))
        if status == 0:
            AddLog('Restarted')
        else:
            AddLog('Exception raised, restarted')
        
    else:
        # Still running
        AddLog('Still running')
        time.sleep(5)