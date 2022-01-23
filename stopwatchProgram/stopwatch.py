from datetime import datetime, timedelta
import PySimpleGUI as sg
import pandas as pd
import os

flag_GUI_Time = False
currentTime = '0:00:00'
comment = ''
win2_active = False

# Starts the counter 
# Takes in no arguments, the startTime variable is set to the current time when called   
def startCounter():
    global startTime
    startTime = datetime.now()
    global diff
    diff = timedelta(days=0, seconds=0, microseconds=0)
    
    # For Debugging
    # print("The start time is: " + str(startTime))

# Ends the counter through user input of 'end'
def endCounter():
        global endTime
        endTime = datetime.now()

        # For Debugging
        # print("The final time is: " + str(endTime))

# CSV saving function
def saveAsCSV():
    try:
        openCSV = open('openCSV.csv' , 'r')
        openCSV.close()
        openCSV = open('openCSV.csv' , 'a')
        openCSV.write(str(startTime) + ", " + str(endTime) + ", " + str(timeElapsed) + ", " + str(comment) + "\n")
        openCSV.close()
    
    except:
        openCSV = open('openCSV.csv' , 'a')
        openCSV.write("Start Time , End Time , Time Elapsed (HH:MM:SS.ms) , Comments \n")
        openCSV.write(str(startTime) + ", " + str(endTime) + ", " + str(timeElapsed) + ", " + str(comment) + "\n")
        openCSV.close()

# Excel saving function
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
# 3 buttons (Start, End, and Log Run)
layout = [ [sg.Text("Please Press 'Start' to Begin Timing")],
           [sg.Text(currentTime, key = 'GUI_Time')],
           [sg.Button('Start'), sg.Button('Resume' , disabled = True), sg.Button('End', disabled = True) , sg.Button('Log Run' , disabled = True)]
#           [sg.Button('Save with Comment', visible = False) , sg.Button('Save without Comment', visible = False)],
#           [sg.Input(key = 'comment' , visible = False)],
#           [sg.Button('Confirm' , visible = False)]
         ]

# Create window with all elements centered
window = sg.Window("Stopwatch Program", layout, element_justification='c')

# ------------------------------------------------------------------------------------------------ #

# Main loop
if __name__ == "__main__":
    
    while True:
        # Tree elements and their respective events
        event, values = window.read(timeout=10)

        # If the window is ever closed, exit the loop
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        # Updates the currentTime
        if flag_GUI_Time == True:
            currentTime = datetime.now() - startTime - diff
            window['GUI_Time'].update(currentTime)

        # User presses start and calls the startCounter() function
        # Record start time
        if event == 'Start':
            print("You have pressed the start button")
            
            # Change the button states 
            window['Start'].update('Start', disabled=True)
            window['Resume'].update(disabled = True)
            window['Log Run'].update(disabled = True)
            window['End'].update(disabled=False)

            startCounter()

            # Sets a flag to start the infinite timer
            flag_GUI_Time = True
        
        # User presses resume and the timer resumes
        # PROBLEM (The time in the real world will continue and the calculation will be inaccurate)
        if event == 'Resume':
            print("You have pressed the resume button")

            # Change the button states
            window['Start'].update(disabled=True)
            window['Resume'].update(disabled=True)
            window['Log Run'].update(disabled=True)
            window['End'].update(disabled=False)

            # Record the difference of time from when you stopped the timer and when you restart it
            diff += datetime.now() - endTime

            # Allow the time to continue again
            flag_GUI_Time = True
            continue

        # Timer runs till user presses stop
        # Stop is pressed and calls the endCounter function
        if event == 'End':
            print("You have pressed the end button")

            # Change the button states
            window['Start'].update('Reset', disabled=False)
            window['End'].update(disabled=True)
            window['Resume'].update(disabled = False)
            window['Log Run'].update(disabled = False)

            endCounter()

            # Calculate the Elapsed time and stop the GUI_Time calculation
            timeElapsed = endTime - startTime - diff
            flag_GUI_Time = False
            window['GUI_Time'].update(timeElapsed)

        #To properly log outputs, we'll just have the user log the output themselves by pressing the button


        if event == "Log Run" and not win2_active:

# --------------------------------------REDACTED----------------------------------------------------------- #
            # Elapsed time is calculated (end-start) and recorded to the csv file
            # timeElapsed = endTime - startTime
            
            # Disable's the button to prevent the user from double-logging
#            window['Log Run'].update(disabled = True)
#            window['Save with Comment'].update(visible = True)
#            window['Save without Comment'].update(visible = True)
# --------------------------------------REDACTED----------------------------------------------------------- #

            # Essentially we will open another window and ask the user for the format of how they want to save their file
            # Declare that the 2nd window is active and hide the timer (window)
            win2_active = True
            window.hide()

            # Set the layout for the User's choice
            layout2 = [[sg.Text('How do you wish to log your time?')],
                       [sg.Button('Save with Comment'), sg.Button('Save without Comment')]]

            # Reveal the 2nd window to be only active
            window2 = sg.Window('Window 2', layout2)

            while True:
                event2, values2 = window2.read()
                
                # If the user decides to close the window
                if event2 == sg.WIN_CLOSED:
                    # Close the second window and unhide the timer
                    window2.close()
                    win2_active = False
                    window.UnHide()
                    break
                
                # Within the second window if either these buttons get clicked then do these operations
                if event2 == 'Save with Comment':
                    comment = sg.popup_get_text('Please enter your comment:', keep_on_top=True)
                    saveAsCSV()
                    saveAsEXCEL()
                    sg.popup('Time has been logged')

                    # Close the second window and unhide the timer
                    window2.close()
                    win2_active = False
                    window.UnHide()

                if event2 == 'Save without Comment':
                    comment = ''
                    saveAsCSV()           
                    saveAsEXCEL()
                    sg.popup('Time has been logged')

                    # Close the second window and unhide the timer
                    window2.close()
                    win2_active = False
                    window.UnHide()

            # After logging the time disable the log button
            window['Log Run'].update(disabled = True)

# --------------------------------------REDACTED----------------------------------------------------------- #       
#        if event == 'Save with Comment':

#            window['Save with Comment'].update(visible = False)
#            window['Save without Comment'].update(visible = False)
#            window['Confirm'].update(visible = True)
#            window['comment'].update(visible = True)

#        if event == 'Confirm':
#            comment = str(values['comment'])
#            saveAsCSV()           
#            saveAsEXCEL()
#            window['Confirm'].update(visible = False)
#            window['comment'].update(visible = False)


#        if event == 'Save without Comment':
#            comment = ''
#            saveAsCSV()           
#            saveAsEXCEL()
#            window['Save with Comment'].update(visible = False)
#            window['Save without Comment'].update(visible = False)
# --------------------------------------REDACTED----------------------------------------------------------- #

        # Debugging
        #print(event,values)
        
    # Always called like a file close (safely frees up resources)
    window.close()

#---------------------------------------------------------------------------------#
