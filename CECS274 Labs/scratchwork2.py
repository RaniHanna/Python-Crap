import sys
import os
import numpy as np

# Number 2:

def resize():
    global arr
    global n
    global j
    
    arr2 = np.zeros(2 * n)
    for i in range(0 , n):
        arr2[i] = arr[(j + i) % len(arr)]
    arr = arr2
    j = 0
    return(arr)

class randomQueue:
    
    global n
    global arr
    global j
    arr = np.zeros(1)
    n = 0
    j = 0

    def contents(self):
        global arr
        
        return(arr)
    
    def enqueue(self, x):
        global arr
        global n 
        global j

        
        if(n == len(arr)):
            resize()
        arr[(j + n) % len(arr)] = x
        n = n + 1

    def dequeue(self):
        global arr
        global j 
        global n
        
        if(n == 0):
            sys.exit('Invalid')
        j = (j + 1) % len(arr)
        n = n - 1
        if(len(arr) > 3 * n):
            resize()
        

def addAll(positionAdd , list1 , list2):
    listOut = [None] * (len(list1) + len(list2))
    if(positionAdd > len(list2)):
        sys.exit('Out of Range')
    for i in range(0 , len(list1)):
        listOut[positionAdd + i] = list1[i]
    for i in range(0 , len(listOut)):
        if(listOut[i] == None and len(list2) > 0):
            listOut[i] = list2[0]
            list2.pop(0)
    return(listOut)

li1 = [1 , 2 , 3]
li2 = [4 , 5 , 6]
x = addAll(3 , li2 , li1)
print(x)