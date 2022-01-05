import random
import dataTableMake
dataTableMake.dataTableMake(5 , 95 , 5 , 90)
print(dataTableMake.tableEntry)
def dataTableSort(tableEntry):
    aggregateSort = sorted(tableEntry[2])
    skillSort = [None] * len(tableEntry[0])
    luckSort = [None] * len(tableEntry[0])
    for i in range(len(tableEntry[2])):
        for j in range(len(tableEntry[2])):
            if(tableEntry[0][j] + tableEntry[1][j] == aggregateSort[i]):
                skillSort[i] = tableEntry[0][j]
                luckSort[i] = tableEntry[1][j]
    tableEntry = [skillSort , luckSort , aggregateSort]
    return(tableEntry)

dataTableSort(dataTableMake.tableEntry)
print(dataTableMake.tableEntry)