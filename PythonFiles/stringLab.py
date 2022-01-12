#gets the input
str = input("Input a string: ")
#set a variable for the length of the string
length = len(str)
#gets the position of the middle character
mid = int(len(str) / 2)
#prints the length and the middle character
print("The string is",length,"characters long, and the middle character is",str[mid]+".")

letters = 0;

for pos in str:
    letters += 1
    print(pos,letters)
if letters == length:
    print("Length was correct.")
