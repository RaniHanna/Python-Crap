import random
import dataTableFunctions
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# For tomorrow: Create fct for the portion where we generate data and plots, so we can call to re-generate the data and plots
# While the app window is still open, we can continuously check via a while loop if an "update" button is/isn't pressed
# This can be done in the bottom GUI code and view the link open in Chrome for similar implementation
# When making the fcts, split one for making the data and another for plotting the data 

# Generating Data Table & Assigning Values
numEntries , percentLuck , percentSkill, passReq = 10 , 95 , 5 , 50
x = dataTableFunctions.dataTableMake(numEntries , percentLuck , percentSkill,passReq)
tableEntry , passArr , numPassed , numPassedNoLuck = x[0] , x[1] , x[2] , x[3]

# Sorting Data Table, To run unsorted just comment the line below out
tableEntry = dataTableFunctions.dataTableSort(tableEntry)

# Code For Bar Graph Output of Dataset
lengthList = list(range(len(tableEntry[0])))
skillBar = plt.bar(lengthList , tableEntry[0])
luckBar = plt.bar(lengthList , tableEntry[1] , 0.8 , tableEntry[0])
for i in lengthList:
    if(tableEntry[2][i]> passReq):
        skillBar[i].set_color("gold")
        luckBar[i].set_color("green")

# Dotted line to see pass value, labels, and results
plt.axhline(passReq ,color = 'r', ls = "--" , linewidth = 0.5)
plt.title("Data Table Results")
plt.ylabel("Score Out of 100")

# ------------------------------- Beginning of Matplotlib helper code -----------------------
def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg

# ------------------------------- Beginning of GUI CODE -------------------------------
sg.theme('Light Brown 3')

fig = plt.gcf()  # if using Pyplot then get the figure from the plot
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds

# define the window layout
layout = [[sg.Canvas(size=(figure_w , figure_h), key='-CANVAS-')],
          [sg.OK(pad=((figure_w /2, 0), 3), size=(6, 1))]]

# create the form and show it without the plot
window = sg.Window('Probability Simulator Project GUI',
    layout, force_toplevel=True, finalize=True)

# add the plot to the window
fig_photo = draw_figure(window['-CANVAS-'].TKCanvas, fig)

# show it all again and get buttons
event, values = window.read()

window.close()