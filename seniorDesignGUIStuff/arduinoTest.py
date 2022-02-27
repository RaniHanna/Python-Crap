import matplotlib.pyplot as plt
import serial
import pandas as pd
import os
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

device = serial.Serial(port='COM3', baudrate = 9600, timeout=.1)
i = 0

graphCSV = open('graphCSV.csv' , 'a')
graphCSV.write('time , Voltage \n')
graphCSV.close()
csvIndex = 0
t = []
V = []

def makeGraph():
    global savePlot
    savePlot = plt.figure()
    plt.plot(t , V)
    plt.ylim((0 , 1))
    plt.xlim((0 , 3))
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
        x *= (5 / 1023)
        print(x)
        csvIndex += 1

        graphCSV = open('graphCSV.csv' , 'a')
        graphCSV.write(str(csvIndex) + ", " + str(x) + "\n")
        graphCSV.close()

        data = pd.read_csv('graphCSV.csv')
        z = [list(x) for x in data.values]
        
        t.append(z[i][0])
        V.append(z[i][1])
        print(V)
        i += 1

def updateGraph():
    global figManip
    global savePlot
    global t
    global V
    figManip.get_tk_widget().forget()
    generateData()
    '''
    t = [0 , 1 , 2 , 3]
    V = [random.random() , random.random() , random.random() , random.random()]
    '''
    plt.clf()
    '''
    plt.ylim((0 , 1))
    plt.xlim((0 , 3))
    '''
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
          [sg.Button('Update')]
         ]
window = sg.Window('Virtual Oscilloscope GUI', layout, force_toplevel=True, finalize=True)

makeGraph()

while(True):
    event, values = window.read(timeout = 100)
    generateData()
    #if event == 'Update':
    updateGraph()

    if event == sg.WIN_CLOSED:
        graphCSV.close()
        os.remove('graphCSV.csv')
        break

window.close()
os.remove('graphCSV.csv')