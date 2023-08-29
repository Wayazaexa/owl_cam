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

# Start the processes first time
process = subprocess.Popen(['python', 'lektion.py'])
process2 = subprocess.Popen(['python','lektion1.py'])
process3 = subprocess.Popen(['python','lektion2.py'])
AddLog('Started')

while True:
    # Check the state of the process
    status = process.poll()
    status2 = process2.poll()
    status3 = process3.poll()

    if status != None:
        # Terminated, restart process
        process = subprocess.Popen(['python', 'lektion.py'])
        print ('Thread 1: Termination code %d, restarted' % (status))
        if status == 0:
            AddLog('Thread 1: Restarted')
        else:
            AddLog('Thread 1: Exception raised, restarted')
        
    else:
        # Still running
        AddLog('Thread 1: still running')

    if status2 != None:
        # Terminated, restart process
        process2 = subprocess.Popen(['python', 'lektion1.py'])
        print ('Thread 2: Termination code %d, restarted' % (status2))
        if status2 == 0:
            AddLog('Thread 2: Restarted')
        else:
            AddLog('Thread 2: Exception raised, restarted')
        
    else:
        # Still running
        AddLog('Thread 2: Still running')
    
    if status2 != None:
        # Terminated, restart process
        process3 = subprocess.Popen(['python', 'lektion2.py'])
        print ('Thread 3: Termination code %d, restarted' % (status2))
        if status2 == 0:
            AddLog('Thread 3: Restarted')
        else:
            AddLog('Thread 3: Exception raised, restarted')
        
    else:
    # Still running
        AddLog('Thread 3: Still running')
        #process3.kill()
        #process2.kill()
        #process.kill()
        time.sleep(10)
    
