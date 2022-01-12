# variable "name" for your name
#variable "age" with your age
#figure out what year you were born
#print Hello [name], you must have been born in [year] to be [age] this year!

#assigning the variables
name = input("What is your name? ")
age = int(input("How old will you be this december? "))
#figures out your birth year
yearBorn = 2021 - age
#prints the message
print("Hello", name+", you must have been born in", yearBorn, "to be", age, "this year!")
