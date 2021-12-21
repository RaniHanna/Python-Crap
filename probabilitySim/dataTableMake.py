import random

# Variable Declarations
skill =[]
luck = []
aggregate = []
tableEntry = [skill , luck , aggregate]

def dataTableMake(tableSize = 10 , percentSkill = 95 , percentLuck = 5):
    if(percentSkill + percentLuck != 100):
        percentLuck += 100 - (percentSkill + percentLuck) # Will replace percentLuck with 100 - percentSkill
        # Doing this ensures our total sum will equal 100, but we send a warning message to the user 
        # As nothing in the code breaks but the output will be off\
        print('Your Values Will Yield An Innacurate Result, Program Still Runs')

    for i in range(tableSize):
        skill.append(random.random())
        skill[i] *= percentSkill
        luck.append(random.random())
        luck[i] *= percentLuck
        aggregate.append(skill[i] + luck[i])
        if(aggregate[i] < 0):
            aggregate[i] = 0
           
dataTableMake(10 , 100, 0)
passArr = []
numPassed = 0
for i in range(10):
    if(tableEntry[2][i] >= 90):
        passArr.append(tableEntry[1][i])
        numPassed += 1
    else:
        passArr.append(-1)
print(passArr)
print(numPassed)

