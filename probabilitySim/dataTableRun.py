import random
import dataTableFunctions
import matplotlib.pyplot as plt

numEntries , percentLuck , percentSkill, passReq = 1000 , 95 , 5 , 50
x = dataTableFunctions.dataTableMake(numEntries , percentLuck , percentSkill,passReq)
tableEntry , passArr , numPassed , numPassedNoLuck = x[0] , x[1] , x[2] , x[3]

tableEntry = dataTableFunctions.dataTableSort(tableEntry)

lengthList = list(range(len(tableEntry[0])))
skillBar = plt.bar(lengthList , tableEntry[0])
luckBar = plt.bar(lengthList , tableEntry[1] , 0.8 , tableEntry[0])
for i in lengthList:
    if(tableEntry[2][i]> passReq):
        skillBar[i].set_color("gold")
        luckBar[i].set_color("green")

plt.axhline(passReq ,color = 'r', ls = "--" , linewidth = 0.5)
plt.title("Data Table Results")
plt.ylabel("Score Out of 100")
plt.show()