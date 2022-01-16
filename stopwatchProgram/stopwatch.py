from datetime import datetime
import PySimpleGUI as sg


# Starts the counter through user input of 'start'    
def startCounter():
    print("Please Type 'start' in the prompt below to start counting time")
    beginCount = input()
    
    # If the user types 'start' then record the current time and output it
    if(beginCount == 'start' or beginCount == 'Start'):
        global startTime
        startTime = datetime.now()
        print("The start time is: " + str(startTime))
    
    # Else recursively call the function again 
    else:
        startCounter()

# Ends the counter through user input of 'end'
def endCounter():
    print("When you are finished, type 'end' to finish counting time")
    endCount = input() 

    # If the user types 'start' then record the current time and output it
    if(endCount == "end" or endCount == "End"):
        global endTime
        endTime = datetime.now()
        print("The final time is: " + str(endTime))

        # Else recursively call the function again 
    
    else:
        endCounter()

# GUI begins :)

GUI_Time = datetime.now()

# Initial
# Box
# Elapsed time starts at 00:00:00
# 2 buttons (Start and End)
layout = [ [sg.Text("Here's your stopwatch Jojo that you could have made yourself")],
           [sg.Text(GUI_Time)],
           [sg.Button('Start'), sg.Button('End')]
         ]

window = sg.Window("Jojo's Timer", layout, element_justification='c')

# Test to see how tf event and values are read and displayed
while True:
    # Tree elements and their respective events
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    print(event,values)

# Always called like a file close (safely frees up resources)
window.close()

# User presses start and calls the startCounter() function
# Record start time
# Call the datetime.now() infinitely and display it on the GUI (EQ = datime.now() - startTime)

# Timer runs till user presses stop
# Stop is pressed and calls the endCounter function
# End time is also displayed on the GUI (EQ = datime.now() - startTime)

# Elapsed time is calculated (start) and recorded to the csv file

#---------------------------------------------------------------------------------#

# Fancy feature 
# Buttons (If start button is pressed, it becomes grayed out or locked and only the stop button is active)
# Only one of the buttons depending on the state of the timer (running or not) is active or availble to be pressed
# ^ If it's difficult with GUI library tools to do this, we could combine the buttons into one start/stop button

# Display the actual running time as its starting 
# Display the actual time when it stops


""" startCounter()
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
    openCSV.close() """