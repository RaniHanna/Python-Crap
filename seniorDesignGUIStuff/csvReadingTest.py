import pandas as pd
import os
import matplotlib.pyplot as plt
import serial
import csv

t = []
v = []



device = serial.Serial(port='COM3', baudrate = 9600, timeout=.1)
x = 0

graphCSV = open('graphCSV.csv' , 'a')
graphCSV.write('time , Voltage \n')
graphCSV.close()

csvIndex = 0
t = []
V = []
i = 0

while(x < 3.25):
    reading = device.readline().decode()
    readingValid = bool(reading.strip())
    if(readingValid):
        x = int(reading.strip())
        x *= (5 / 1023)
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

        
        
        


os.remove('graphCSV.csv')