str = "laptops out for harambe"

print(str[5:])
print(str[7:11])
print(str[16:])
print(str[10:13])


string = input("Input a word: ")
lastChar = string[len(string)-1]
print(lastChar,string.rstrip(string[-1]))
gibString = lastChar + string.rstrip(string[-1]) + "ha"
print(gibString)
