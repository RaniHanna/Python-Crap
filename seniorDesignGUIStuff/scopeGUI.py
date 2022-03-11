import matplotlib.pyplot as plt
import serial
import pandas as pd
import os
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time

# Establishes serial comms w/ MCU 
device = serial.Serial(port='COM4', baudrate = 115200, timeout=.1) 
i = 0

# Creates CSV and writes headers
graphCSV = open('graphCSV.csv' , 'a')
graphCSV.write('time , Voltage \n')
graphCSV.close()

# Varibles to be used in multiple functions
runningFlag = True
csvIndex = 0
t = []
V = []

'''
makeGraph() 
    - Creates empty plot prior to GUI main loop so graph can continuously update
    - Also sets the graph axes/limits, note that xlim corresponds to len(t), this will change to the amt allocated in the time/div

generateData()
    - Reads voltage reading from MCU's internal ADC and converts to an integer value to be stored in the CSV 
    - CSV data is converted back to integer values and stored into the t & V lists for plotting

updateGraph()
    - Deletes the empty figure/plot made in the makeGraph portion and generates a new plot by calling the generateData() fct
    - By calling generateData() we get the most recently updated data from the t & V lists
    - Will be called continuously while in the GUI main loop, throws an error when not triggered via an "Update" event
'''
def makeGraph():
    global savePlot
    global t
    global V
    savePlot = plt.figure()
    plt.plot(t , V)
    plt.ylim((0 , 5))
    plt.xlim((0 , len(t)))
    plt.xlabel('Sample #')
    plt.ylabel('Voltage (V)')
    global figManip
    figManip = draw_figure(window['Plot'].TKCanvas , savePlot)

def generateData():
    global csvIndex
    global i
    global t
    global V
    reading = device.readline().decode()
    readingValid = bool(reading.strip())
    if(readingValid):
        x = int(reading.strip())
        x *= (3.3 / 1023)
        print(x)
        csvIndex += 1
        '''
        # We COULD just do this instead of dealing with the CSV but I already did that work soo whatever it might come in handy
        t.append(csvIndex)
        V.append(x)
        '''        
        
        graphCSV = open('graphCSV.csv' , 'a')
        graphCSV.write(str(csvIndex) + ", " + str(x) + "\n")
        graphCSV.close()

        data = pd.read_csv('graphCSV.csv')
        z = [list(x) for x in data.values]
        
        t.append(z[i][0])
        V.append(z[i][1])
        i += 1

def updateGraph():
    global figManip
    global savePlot
    global t
    global V
    figManip.get_tk_widget().forget()
    generateData()
    '''
    #Old Code to generate some quick data before we ironed out the CSV parsing for data plotting
    t = [0 , 1 , 2 , 3]
    V = [random.random() , random.random() , random.random() , random.random()]
    '''
    plt.clf()
    plt.ylim((0 , 5))
    plt.xlim((0 , len(t)))
    plt.xlabel('Sample #')
    plt.ylabel('Voltage (V)')
    plt.plot(t , V)
    figManip = draw_figure(window['Plot'].TKCanvas , savePlot)

# ------------------------------- GUI Helper Function -------------------------------
def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg
# ------------------------------- Beginning of GUI CODE -------------------------------
layout = [[sg.Canvas(key = 'Plot')],
          [sg.Button('Start')],[sg.Button('Stop')],
         ]
window = sg.Window('Virtual Oscilloscope GUI', layout, force_toplevel=True, finalize=True)

makeGraph()

while(True):
    event, values = window.read(timeout = .001)
    # timeout value = time to wait until read in ms

    # NOTE: no "top level" error when the updateGraph() fct is called via 'Update' key instead of continuous calling

    if event == 'Start':
        runningFlag = True
    if event == 'Stop':
        runningFlag = False

    if runningFlag == True:
        generateData()
        updateGraph()

    if event == sg.WIN_CLOSED:
        graphCSV.close()
        runningFlag = False
        os.remove('graphCSV.csv')
        break

window.close()
#os.remove('graphCSV.csv')