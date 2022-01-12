#import os
#import random
#open file in read form, set that to variable
#make empty list to store file
#loop through file variable
#add line (with \n at end removed) to empty list
#close file
#take string input as a yes or no question
#while loop as long as the string input isn't 'no more questions'
#>pick a random number 0 to the max index of the list
#>say the line at the index of the random number above
#>take input again
#end of while loop

import os
import random

inputFile = open("magic.txt", "r")

possAnswers = []

for line in inputFile:
    possAnswers.append(line.rstrip('\n'))
inputFile.close()
inputQuestion = input("Ask a yes or no question: ")
while(inputQuestion != "no more questions"):
    chosenAnswer = random.randint(0,len(possAnswers) - 1)
    os.system("say " + possAnswers[chosenAnswer])
    print(possAnswers[chosenAnswer])
    inputQuestion = input("Ask another question: ")
