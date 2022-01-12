#take input word
#make a bunch of lists to refer to in for each loops later
#lists have all monsters, monsters i make (empty), alphabet, amount of each letter in scrambled word, and lists of amount of each letter in each monster
#get amount of each letter in input word with for loop
#go through every word in the list of monsters
#get amount of each letter in every word with for loop
#start a loop that continues until every letter has been used
#go through every list in the list of lists of letters
#check if it has at least as many of every letter as the input word
#if it does, take the amount of each letter int he monster word from the amount in the input word, and add the monster word to the list of the monsters we got
#print the list
#/\/\PSUEDOCODE/\/\#

#\/\/CODE\/\/#
#take input word to sort later
inputWord = input("What word scramble do you need to be exorcised? ")
#make array of all monsters that could be in the word
possMonsters = ["frankenstein","ghost","jack","mummy","skeleton","vampire","werewolf","witch","zombie"]
#make array to store the monsters that are in the word
totalMonsters = []
#make sure the input word is all lower case, so that it only needs to be compared against lowercase letters
scrambleRemaining = inputWord.lower()
#make array of letters in the alphabet to run through later
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#make empty array to store the amount of each letter in the input word
abcCount = [0] * 26
#make empty 2d array to store the amount of each letter in each monster word
monCount = [[0]*26 for i in range(9)]
#run through every letter in the alphabet for every letter in the input word, and add one to that position in the empty alphabet list if they match. this will get the amount of each letter in the input word
for letter in scrambleRemaining:
    for let in range(len(alphabet)):
        if letter == alphabet[let]:
            abcCount[let] += 1
#do the exact same thing as above, but do it for every monster in the monster list
for monster in range(len(possMonsters)):
    for letter in possMonsters[monster]:
        for let in range(len(alphabet)):
            if letter == alphabet[let]:
                monCount[monster][let] += 1
#initializes a variable to store the current monster we're checking
currentMonsterIndex = -1
#check monsters until no letter is left unused
while(sum(abcCount) > 0):
    #run through every letter list in the list of lists
    for monster in monCount:
        #go to the next monster index, if it goes over the max allowed value, reset back to 0
        currentMonsterIndex += 1
        if currentMonsterIndex >= len(possMonsters):
            currentMonsterIndex = 0
        #go through every letter in the monster alphabet list, and if at any point there is more of some letter in the monster word than the input word, break out of the for loop and move on to the next monster
        for letter in range(len(monster)):
            if abcCount[letter] < monster[letter]:
                break
        else: #runs only if the for loop finishes and the break doesnt trigger
            #go through every letter in the monster alphabet list, and take that many away from the input alphabet list
            for letter in range(len(monster)) :
                abcCount[letter] -= monster[letter]
            #add the monster word to the list of found monsters
            totalMonsters.append(possMonsters[currentMonsterIndex])
#print the list. i used sorted because it looks better, even though we haven't learned it, but since it doesn't affect the functionality of the code, I thought it was fine.
print("%d monsters were found:%s" % (len(totalMonsters),sorted(totalMonsters)))
