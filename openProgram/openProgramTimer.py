import psutil
import time

timeOpen = 0

Open = False

#'\n' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

logFileName = 'programTimeLog.txt'
configFileName = 'config.txt'

with open(logFileName, 'a') as openFile:
    writeStr = '\n' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + ' Watcher Started'
    
    openFile.write(writeStr)
    openFile.close()

with open(configFileName, 'r') as reader:
    step = 0 # a counter for how many lines have been read
    for line in reader:
        if step == 0: # if the line being read is the first line
            watchProgram = line.split(',')[0]
        
        if step == 1:
            timeIncrement = int(line) * 60

        step += 1

print(watchProgram)


while True:
    time.sleep(1)
    
    openFile = open(logFileName, 'a')

    processList = []

    for i in psutil.process_iter(): # adding the processes that have an accessible name to a list
        try:
            processList.append(i.name())

        except psutil.AccessDenied:
            pass
    
    if watchProgram in processList: # checks if the program is running
        timeOpen += 1

        if Open == False:
            writeStr = '\n' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + watchProgram + ' Opened'
            openFile.write(writeStr)
            Open = True
        
        if timeOpen%timeIncrement == 0:
            writeStr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + watchProgram + ' open for ' + str(timeOpen)
            openFile.write(writeStr)            

    else: 
        if Open == True:
            writeStr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + watchProgram + ' open for ' + str(timeOpen)
            openFile.write(writeStr)
            writeStr = '\n' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + watchProgram + ' Closed'
            openFile.write(writeStr)
            
            timeOpen = 0
            Open = False

    openFile.close()


