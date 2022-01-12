#take int input from user
#generate random number 1-20
#if numbers are equal, print success, otherwise print False

import random

#gets input
userInput = int(input("Pick a number, 0-20:"))
#gets random number
computerInput = random.randint(0,20)
#determines if theyre equal and prints a success/failure message
if userInput==computerInput:
    print("Success!")
else:
    print("Failure. The correct number was:",computerInput)
