import pandas as pd

constraintOut = open('versalConstraint.txt' , 'a')

data = pd.read_csv('Versal Constraint CSV.csv')
z = [data.values]

for i in range(0 , len(z[0])):
    constraintOut.write('set_property PACKAGE_PIN ' +  str(z[0][i][3]) + '[get_ports ' + str(z[0][i][0]) + ']' + '\n')
    constraintOut.write('set_property IOSTANDARD ' +  str(z[0][i][1]) + '[get_ports ' + str(z[0][i][0]) + ']' + '\n')
    constraintOut.write("\n")
#set_property PACKAGE_PIN L37 [get_ports CTRL_CLK]
#set_property IOSTANDARD LVCMOS_33 [get_ports CTRL_CLK]

constraintOut.close()