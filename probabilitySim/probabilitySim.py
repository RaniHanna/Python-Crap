import random

skill =[]
luck = []
aggregate = []

def dataTableMake(tableSize = 10 , percentSkill = 95 , percentLuck = 5):
    if(percentSkill + percentLuck != 100):
        percentLuck += 100 - (percentSkill + percentLuck) # Will replace percentLuck with 100 - percentSkill
        # Doing this ensures our total sum will equal 100, but we send a warning message to the user 
        # As nothing in the code breaks but the output will be off
        print(percentLuck)
        print(percentSkill + percentLuck)
    for i in range(tableSize):
        skill.append(random.random())
        skill[i] *= percentSkill
        luck.append(random.random())
        luck[i] *= percentLuck
        aggregate.append(skill[i] + luck[i])
        if(aggregate[i] < 0):
            aggregate[i] = 0
dataTableMake(10 , 90 , 10)
print(aggregate)
print(luck)
print(skill)

