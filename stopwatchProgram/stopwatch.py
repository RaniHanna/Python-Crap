from datetime import datetime
    
def startCounter():
    print("Please Type 'start' in the prompt below to start counting time")
    beginCount = input()
    if(beginCount == 'start' or beginCount == 'Start'):
        global startTime
        startTime = datetime.now()
        print("The start time is: " + str(startTime))
    else:
        startCounter()

def endCounter():
    print("When you are finished, type 'end' to finish counting time")
    endCount = input() 
    if(endCount == "end" or endCount == "End"):
        global endTime
        endTime = datetime.now()
        print("The final time is: " + str(endTime))
    else:
        endCounter()

startCounter()
endCounter()
timeElapsed = endTime - startTime

try:
    openCSV = open('openCSV.csv' , 'r')
    openCSV.close()
    openCSV = open('openCSV.csv' , 'a')
    openCSV.write(str(startTime) + ", " + str(endTime) + ", " + str(timeElapsed) + "\n")
except:
    openCSV = open('openCSV.csv' , 'a')
    openCSV.write("Start Time , End Time , Time Elapsed (HH:MM:SS.ms) \n")
    openCSV.write(str(startTime) + ", " + str(endTime) + ", " + str(timeElapsed) + "\n")
    openCSV.close()