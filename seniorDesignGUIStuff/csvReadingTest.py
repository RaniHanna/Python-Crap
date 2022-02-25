import pandas as pd
import os
import matplotlib.pyplot as plt
import serial

t = []
v = []
plt.plot(t , v)
plt.show()


'''
device = serial.Serial(port='COM3', baudrate = 9600, timeout=.1)
x = 0

graphCSV = open('graphCSV.csv' , 'a')
graphCSV.write('time , Voltage \n')

csvIndex = 0
t = []
V = []

while(x < 3.25):
    reading = device.readline().decode()
    readingValid = bool(reading.strip())
    if(readingValid):
        x = int(reading.strip())
        x *= (5 / 1023)
        print(x)
        csvIndex += 1
        graphCSV.write(str(csvIndex) + ", " + str(x) + "\n")
        data = pd.read_csv('graphCSV.csv')
        print(data)
        t = data['time']
        V = data['Voltage']
        plt.plot(t , V)
        plt.show()
        

graphCSV.close()
os.remove('graphCSV.csv')
'''