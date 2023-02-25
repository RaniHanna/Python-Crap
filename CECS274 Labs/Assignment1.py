import sys
import os
import numpy as np

# Number 1:
inFile = open('input.txt' , 'r') # I needed to define these prior to entering my function so I don't get a run error when it runs
outFile = open('out.txt' , 'a')

def reverseTxt(inputTxt , outputTxt):
    verifyTxt = open('verifyIfTXT.txt' , 'r')
    if(type(inputTxt) != type(verifyTxt)):
        sys.exit('Input File Type is not a text file OR input txt file not open prior to running')
    if(type(outputTxt) != type(verifyTxt)):
        sys.exit('output File Type is not a text file OR output txt file not open prior to running')
    
    fileList = inputTxt.readlines()
    fileLength = len(fileList)

    for i in range(0 , fileLength):
        outputTxt.write(str(fileList[fileLength - i - 1]))

#reverseTxt(inFile , outFile)

inFile.close()
outFile.close()

'''
In order to implement this, I took the last element of the initial list and placed it in the front of the reversed list.
This resembles a stack where the last element of my original data will be the first element of my reversed data. 
'''

# Number 2:

'''
For this one, we can just iterate thru all the elements in our input text file and place them into a set, and then we can
iterate through the set to give us the output with no duplicates as sets cannot contain duplicates, so we get a cleaned version
of our input text file. I used a different text file named "og.txt" in order to keep the other "originalFile" in tact from #1
'''
originalFile = open('log-1.txt' , "r")
destinationFile = open('out2.txt' , 'a')

def removeDuplication(inputTxt , outputTxt):
    inSet = set({})
    verifyTxt = open('verifyIfTXT.txt' , 'r')
    if(type(inputTxt) != type(verifyTxt)):
        sys.exit('Input File Type is not a text file OR input txt file not open prior to running')
    if(type(outputTxt) != type(verifyTxt)):
        sys.exit('output File Type is not a text file OR output txt file not open prior to running')
    fileList = inputTxt.readlines()
    fileLength = len(fileList)

    for i in range(0 , fileLength):
        inSet.add(fileList[i])
    for i in inSet:
        outputTxt.write(str(i).strip() + "\n")

#removeDuplication(originalFile , destinationFile)

originalFile.close()
destinationFile.close()

# Number 3:
'''
We can use our work from Number 2
'''

originalFile = open('log-1.txt' , "r")
destinationFile = open('out3.txt' , 'a')

def sortAndRemoveDupes(originalFile , destinationFile):
    postDupeDump = open('mid.txt','a')
    removeDuplication(originalFile , postDupeDump)
    postDupeDump.close()
    postDupeDump = open('mid.txt','r')

    fileList = postDupeDump.readlines()
    fileLength = len(fileList)
    sortedFileList = []


    while(fileLength > len(sortedFileList)):
        maxVal = fileList[0]
        for i in range(0 , len(fileList)):
            if(len(fileList[i]) > len(maxVal)):
                maxVal = fileList[i]
                
        sortedFileList.append(maxVal)
        fileList.remove(maxVal)

    for i in range(len(sortedFileList)):
        destinationFile.write(str(sortedFileList[i]))

    postDupeDump.close()
    os.remove('mid.txt')

#sortAndRemoveDupes(originalFile , destinationFile)

originalFile.close()
destinationFile.close()


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

li = List()
# Insert methods here
print(li.contents())


    # Unsorted Sets
class uSet:
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

    def add(self, x):
        global arr
        global n 
        global isNotDupe
        global firstEmpty
        isNotDupe = True
        if(len(arr) == n):
            arr = resize()
        for j in range(len(arr)):
            if(arr[j] == x):
                isNotDupe = False
            if(arr[j] == 0):
                firstEmpty = j
        if(isNotDupe):
            arr[firstEmpty] = x
            n = n + 1
    
    def remove(self, x):
        global arr
        global n 
        for j in range(len(arr)):
            if(arr[j] == x):
                arr[j] = 0
                n = n - 1
        if(len(arr) > 3 * n):
            arr = resize()

st = uSet()
# Insert Methods Here
print(st.contents())

    # Sorted Sets
class sSet:
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

    def add(self, x):
        global arr
        global n 
        global isNotDupe
        global firstEmpty

        isNotDupe = True
        if(len(arr) == n):
            arr = resize()
        for j in range(len(arr)):
            if(arr[j] == x):
                isNotDupe = False
            if(arr[j] == 0):
                firstEmpty = j
        if(isNotDupe):
            arr[firstEmpty] = x
            n = n + 1
        if(len(arr) > 0):
            for i in range(len(arr) - 1):
                for j in range(len(arr) - 1):
                    if(arr[j] < arr[j + 1]):
                        y = arr[j]
                        arr[j] = arr[j + 1]
                        arr[j + 1] = y

    
    def remove(self, x):
        global arr
        global n 
        for j in range(len(arr)):
            if(arr[j] == x):
                arr[j] = 0
                n = n - 1
        if(len(arr) > 0):
            for i in range(len(arr) - 1):
                for j in range(len(arr) - 1):
                    if(arr[j] < arr[j + 1]):
                        y = arr[j]
                        arr[j] = arr[j + 1]
                        arr[j + 1] = y
        if(len(arr) > 3 * n):
            arr = resize()


st = sSet()
# Insert Methods Here
print(st.contents())

