#Weasel program

import random

arrayOfChar= {'a', 'b', 'c','d','e','f','g','h','i', 'j', 'k','l','m','n','o','p',
'q','r', 's', 't','u','v','w','x','y','z',' '}
listOfChar = list(arrayOfChar)
numberOfCharacters = len(listOfChar)

#generating random string with 28 character
def randomString():
    new_sequence = ""

    for x in range(28):
        new_sequence = new_sequence + listOfChar[random.randint(0, numberOfCharacters-1)]

    return new_sequence;
    
    
def newGeneration(str, num):

    newGeneration = list(str)
    numberOfTargetSequence = len(newGeneration)
    chanceOfMutation = float(num/100)
    numberOfLoops = int(numberOfTargetSequence * chanceOfMutation)

    #This make at least one mistake per request
    if(numberOfLoops < 1):
        numberOfLoops = 1
        
    #print numberOfLoops

    if(numberOfLoops > 0):
        for x in range(numberOfLoops):
           newGeneration[random.randint(0,numberOfTargetSequence-1)] = listOfChar[random.randint(0, numberOfCharacters-1)]
    
    return newGeneration;
    

targetSequence = "methinks it is like a weasel"
chanceOfMistake = 30.0

#generating random string with 28 character
randomString = randomString()
print randomString

child ="".join(newGeneration("methinks it is like a weasel", 30.0))
print child
    
