import string
#we didn't split the code up into different sections for each person to do, we just each came up with solutions to certain problems throughout the code
#adds the dictionary list
dictionary = []

fileName = open("longlist.txt")

for line in fileName:
    dictionary.append(line.rstrip())

#makes a new list that contains every word in the dictionary with all letters lowercase
lowerDict = []

for word in dictionary:
    lowerDict.append(word.lower())


#gets string input, and makes it lower case
inp = input("Input a string:")
inp.lower()
#makes a list to contain the alphabet, to reference later
alphabetList = list(string.printable)
#make a list to store the amount of each letter in the input word, and also in each word in the dictionary
inputAlphabet = [0]*len(alphabetList)
dictAlphabet = [[0]*len(alphabetList)for i in range(len(lowerDict))]
#makes an empty list to store anagrams
#\/\/\/#
anagrams = []
#goes through each letter in the input word, comparing it to each letter in the alphabet, and if they match, it adds one to that element in the input alphabet list

for i in inp:
    for letter in range(len(alphabetList)):
        if i == alphabetList[letter]:
            inputAlphabet[letter] += 1
#/\/\/\#
#stores what word the for loop below is on
wordPos = 0

#same as for loop above, but for every word in the dictionary list
for word in lowerDict:
    for wordLetter in word:
        for letter in range(len(alphabetList)):
            if wordLetter == alphabetList[letter]:
                dictAlphabet[wordPos][letter] += 1
    #if the alphabet list for this word matches with the alphabet list for the input, it adds the word to the list that stores the anagrams
    if(dictAlphabet[wordPos] == inputAlphabet):
        anagrams.append(lowerDict[wordPos])
    wordPos += 1
#prints all the anagrams that were found
print(anagrams)
