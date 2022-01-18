from datetime import date, datetime
import PySimpleGUI as sg
import pandas as pd
import os

flag_GUI_Time = False
currentTime = '0:00:00'

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

# CSV saving function
def saveAsCSV():
    try:
        openCSV = open('openCSV.csv' , 'r')
        openCSV.close()
        openCSV = open('openCSV.csv' , 'a')
        openCSV.write(str(startTime) + ", " + str(endTime) + ", " + str(timeElapsed) + "\n")
        openCSV.close()
    
    except:
        openCSV = open('openCSV.csv' , 'a')
        openCSV.write("Start Time , End Time , Time Elapsed (HH:MM:SS.ms) \n")
        openCSV.write(str(startTime) + ", " + str(endTime) + ", " + str(timeElapsed) + "\n")
        openCSV.close()

def saveAsEXCEL():
    CSV_Saver = pd.read_csv('openCSV.csv')
    saveAsExcel = pd.ExcelWriter('badFileType.xlsx')
    CSV_Saver.to_excel(saveAsExcel , index = False)
    saveAsExcel.save()



# GUI begins :)
# ------------------------------------------------------------------------------------------------ #

# Initial
# Box
# Elapsed time starts at 00:00:00
# 2 buttons (Start and End)
layout = [ [sg.Text("Please Press 'Start' to Begin Timing")],
           [sg.Text(currentTime, key = 'GUI_Time')],
           [sg.Button('Start'), sg.Button('End') , sg.Button('Log Run' , disabled = True)]
         ]

window = sg.Window("Stopwatch Program", layout, element_justification='c')

# ------------------------------------------------------------------------------------------------ #

# Main loop
if __name__ == "__main__":
    while True:

        # Tree elements and their respective events
        event, values = window.read(timeout=10)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        
        # Updates the currentTime
        if flag_GUI_Time == True:
            currentTime = datetime.now() - startTime

        # User presses start and calls the startCounter() function
        # Record start time
        if event == 'Start':
            print("You have pressed the start button")
            
            # Change the button states
            window['Start'].update(disabled=True)
            window['End'].update(disabled=False)

            startCounter()

            # Sets a flag to start the infinite timer
            flag_GUI_Time = True
            
        # Timer runs till user presses stop
        # Stop is pressed and calls the endCounter function
        if event == 'End':
            print("You have pressed the end button")

            # Change the button states
            window['Start'].update(disabled=False)
            window['End'].update(disabled=True)
            endCounter()
            timeElapsed = endTime - startTime
            flag_GUI_Time = False
            window['GUI_Time'].update(timeElapsed)

            # We update the log run button after we hit end because that's when it can actually log a run properly
            window['Log Run'].update(disabled = False)

        #To properly log outputs, we'll just have the user log the output themselves by pressing the button
        if event == "Log Run":

            # Elapsed time is calculated (end-start) and recorded to the csv file
            # timeElapsed = endTime - startTime
            saveAsCSV()           
            saveAsEXCEL()
            
            window['Log Run'].update(disabled = True)

        window['GUI_Time'].update(currentTime)

        # print(event,values)


    #str(datetime.now().hour) + ':' + str(datetime.now().minute) + ':' + str(datetime.now().second)
        # Call the datetime.now() infinitely and display it on the GUI (EQ = datime.now() - startTime)    
        
    # Always called like a file close (safely frees up resources)
    window.close()

#---------------------------------------------------------------------------------#
