from datetime import datetime
from faulthandler import disable
import PySimpleGUI as sg


# Starts the counter through user input of 'start'    
def startCounter():
    global startTime
    startTime = datetime.now()
    print("The start time is: " + str(startTime))

# Ends the counter through user input of 'end'
def endCounter():
        global endTime
        endTime = datetime.now()
        print("The final time is: " + str(endTime))

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

    # User presses start and calls the startCounter() function
    # Record start time
    if event == 'Start':
        print("You have pressed the start button")
        
        # Change the button states
        window['Start'].update(disabled=True)
        window['End'].update(disabled=False)
        

        startCounter()

    # Timer runs till user presses stop
    # Stop is pressed and calls the endCounter function
    if event == 'End':
        print("You have pressed the end button")

        # Change the button states
        window['Start'].update(disabled=False)
        window['End'].update(disabled=True)
        endCounter()

    # Call the datetime.now() infinitely and display it on the GUI (EQ = datime.now() - startTime)    
    print(event,values)


# Elapsed time is calculated (end-start) and recorded to the csv file
# timeElapsed = endTime - startTime


# Problem with this is the CSV file saving and creation
# After trying to save another time, the program creates another CSV file rather than appending to the one already within the directory
"""        

        try:
            openCSV = open('openCSV.csv' , 'r')
            openCSV.close()
            openCSV = open('openCSV.csv' , 'a')
            openCSV.write(str(startTime) + ", " + str(endTime) + ", " + str(timeElapsed) + "\n")
        except:
            openCSV = open('openCSV.csv' , 'a')
            openCSV.write("Start Time , End Time , Time Elapsed (HH:MM:SS.ms) \n")
            openCSV.write(str(startTime) + ", " + str(endTime) + ", " + str(timeElapsed) + "\n")
            openCSV.close()"""



# Always called like a file close (safely frees up resources)
window.close()

# End time is also displayed on the GUI (EQ = datime.now() - startTime)

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