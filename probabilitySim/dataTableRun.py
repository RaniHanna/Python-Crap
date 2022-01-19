import random
import dataTableFunctions
import matplotlib.pyplot as plt
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# For tomorrow: Create fct for the portion where we generate data and plots, so we can call to re-generate the data and plots
# While the app window is still open, we can continuously check via a while loop if an "update" button is/isn't pressed
# This can be done in the bottom GUI code and view the link open in Chrome for similar implementation
# When making the fcts, split one for making the data and another for plotting the data 


# Code For Bar Graph Output of Dataset
def plotDataTable(tableSize = 10 , percentSkill = 95 , percentLuck = 5 , passReq = 50):

    # Data Table Generation
    x = dataTableFunctions.dataTableMake(tableSize , percentSkill , percentLuck ,passReq)
    tableEntry , passArr , numPassed , numPassedNoLuck = x[0] , x[1] , x[2] , x[3]

    # Sorting Data Table, To run unsorted just comment the line below out
    tableEntry = dataTableFunctions.dataTableSort(tableEntry)

    # Main Plotting Portion
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

fig = plt.gcf()  # if using Pyplot then get the figure from the plot
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds

# Window Layout
layout = [[sg.Canvas(size=(figure_w * 0.84, figure_h * 0.84), key='Plot')],
          [sg.Text('Please input the Number of Applicants') , sg.InputText(size = 10 , key = 'numEntries')],
          [sg.Text('Please provide Percent Allocated to Skill, the rest will be luck') , sg.InputText(size = 10 , key = 'skillSlider')],
          [sg.Text('Please provide the pass requirement percentage') , sg.InputText(size = 10 , key = 'passReqSlider')],
          [sg.Button('Generate Plot' , key = 'genPlot') , sg.Button('Refresh Plot' , key = 'refreshPlot' , disabled = True)]
         ]

# Creating Window
window = sg.Window('Probability Simulator Project GUI', layout, force_toplevel=True, finalize=True)

# show it all again and get buttons
while True:
    event, values = window.read(timeout = 20)
    if(event == 'genPlot'):
        #skillSliderVals = int(values['skillSlider'])
        plotDataTable()
        # int(values['numEntries']) , skillSliderVals , 100 - skillSliderVals , int(values['passReqSlider'])
        fig = plt.gcf()  # if using Pyplot then get the figure from the plot
        fig_photo = draw_figure(window['Plot'].TKCanvas, fig)

        window['genPlot'].update(disabled = True)
        window['refreshPlot'].update(disabled = False)
        
    if(event == 'refreshPlot'):
        fig_photo.get_tk_widget().forget()
        plt.clf()

        skillSliderVals = int(values['skillSlider'])
        plotDataTable()
        fig = plt.gcf()  # if using Pyplot then get the figure from the plot
        fig_photo = draw_figure(window['Plot'].TKCanvas, fig)

    if event == sg.WIN_CLOSED:
        break

window.close()