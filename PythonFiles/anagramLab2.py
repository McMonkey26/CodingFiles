dictionary = []


fileName = open("longlist.txt")



for line in fileName:


    dictionary.append(line.rstrip())



print(dictionary)

inp = input("Input a word: ")
lists = [[]]*len(inp)
for x in dictionary:
    if(len(x) == len(inp)):
        lists[0].append(x)
for i in lists:
    print(i)
