import sys
import os
import numpy as np
import random

# Number 1
'''
This implementation uses two separate lists outside of the ArrayList interface so this can be implemented with any list or array
interface assuming the methods len() and pop() exist for the given interface. 
'''

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

def resize():
    global arr
    global n
    
    arr2 = np.zeros(2 * n)
    for i in range(0 , n):
        arr2[i] = arr[i]
    arr = arr2
    return(arr)

class List:
    
    global n
    global arr
    arr = np.zeros(1)
    n = 0
    

    def get(self, i):
        global arr
        global n 

        if(i < 0 or i > n - 1):
            sys.exit('Index is out of bounds')
        return(arr[i])

    def size(self):
        global arr
        
        return(len(arr))

    def contents(self):
        global arr
        
        return(arr)

    def set(self , i , x):
        global arr
        global n
        
        if(i < 0 or i > n - 1):
            sys.exit('Index is out of bounds')
        y = arr[i]
        arr[i] = x
        return(y)


    def add(self, i , x):
        global arr
        global n 

        if(i < 0 or i > n):
            sys.exit('Index is out of bounds')
        if(len(arr) == n):
            arr = resize()
        for j in range(n , i , -1):
            arr[j] = arr[j - 1]
        arr[i] = x
        n = n + 1

    def addQueue(self , x):
        global arr
        global n 
        i = 0
        if(len(arr) == n):
            arr = resize()
        for j in range(n , i , -1):
            arr[j] = arr[j - 1]
        arr[i] = x
        n = n + 1

    def remove(self, i):
        global arr
        global n 

        if(i < 0 or i > n - 1):
            sys.exit('Index is out of bounds')
        saveRemoved = arr[i]
        for j in range(i , n):
            arr[j] = arr[j + 1]
        n = n - 1
        if(len(arr) > 3 * n):
            arr = resize()
        return(saveRemoved)

# Number 2: 
    '''
    The randomRemove method was included inside the list interface instead of being its own interface as ArrayStack and 
    ArrayQueue are special cases of the ArrayList interface, this basically just takes the normal remove() function from 
    ArrayList and ensures that the element removed is a random number within the number of elements of the given list.
    Another method addQueue() was created to give us an add method for an ArrayQueue interface.  
    '''

    def randomRemove(self):
        global arr
        global n 

        i = random.randrange(0 , n)
        print(i)

        saveRemoved = arr[i]
        for j in range(i , n):
            arr[j] = arr[j + 1]
        n = n - 1
        if(len(arr) > 3 * n):
            arr = resize()
        return(saveRemoved)

a = List()
a.addQueue(1)
a.addQueue(2)
a.addQueue(3)
a.addQueue(4)
a.randomRemove()
print(a.contents())

# Number 3

'''
Th
'''
def rotateArr(a , r):
    b = np.zeros(len(a))
    for i in range(0 , len(a)):
        b[i] = a[(i + r) % len(a)]
    a = b 
    return(a)

a = np.array([1 , 2 , 3 , 4])
aa = rotateArr(a , 3)
print(aa)

# Number 4
def towerOfHanoi():
    def gameStatus():
        print(rodA)
        print(rodB)
        print(rodC)
    
    numDisks = int(input('How Many Disks? \n'))
    gameOngoingFlag = True
    if(numDisks <= 0 or numDisks > 6):
        sys.exit('Invalid # of Disks, must be within 1-6')
    rodA = []
    rodB = []
    rodC = []
    for i in range(0 , numDisks):
        rodA.append(numDisks - i)
    finalSol = rodA
    gameStatus()
    while(gameOngoingFlag):
        x = input("Type 'A to B' to move the last index of A to the first of B, 'B to C', 'A to C' etc. \n")
        if(x == 'End Game'):
            gameOngoingFlag = False
        if(x == 'A to B'):
            if(len(rodA) > 0):
                rodB.append(rodA.pop())
                gameStatus()
            else:
                print('Invalid Move, Empty Rod')
        if(x == 'A to C'):
            if(len(rodA) > 0):
                rodC.append(rodA.pop())
                gameStatus()
        if(x == 'B to A'):
            rodA.append(rodB.pop())
            gameStatus()
        if(x == 'B to C'):
            rodC.append(rodB.pop())
            gameStatus()
        if(x == 'C to B'):
            rodB.append(rodC.pop())
            gameStatus()
        if(x == 'C to A'):
            rodA.append(rodC.pop())
            gameStatus()
        if(len(rodA) > 1):
            for i in range(len(rodA) - 1 , 0 , -1):
                if(rodA[i] > rodA[i - 1]):
                    print('Invalid Disk Formation, Game Failed')
                    gameOngoingFlag = False
        if(len(rodB) > 1):
            for i in range(len(rodB) - 1 , 0 , -1):
                if(rodB[i] > rodB[i - 1]):
                    print('Invalid Disk Formation, Game Failed')
                    gameOngoingFlag = False
        if(len(rodC) > 1):
            for i in range(len(rodC) - 1 , 0 , -1):
                if(rodC[i] > rodC[i - 1]):
                    print('Invalid Disk Formation, Game Failed')
                    gameOngoingFlag = False
        if(rodB == finalSol or rodC == finalSol):
            print("Success!")
            gameOngoingFlag = False


towerOfHanoi()