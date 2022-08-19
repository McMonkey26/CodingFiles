import random, os, urllib.request, ssl
ssl._create_default_https_context = ssl._create_unverified_context
os.chdir('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PythonFiles')
def getDictFromURL():
  url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words.txt'
  file = urllib.request.urlopen(url)
  wordList = []
  for line in file:
    decoded_line = line.decode("utf-8").rstrip('\n')
    if len(decoded_line) == 5 and all(list(map(lambda x: x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', decoded_line))):
      wordList.append(decoded_line.upper())
  return wordList
def getDictFromFile(fileName):
  with open(fileName, 'r') as file:
    wordList = list(map(lambda x:x.rstrip('\n').upper(), file))
  return wordList
def checkWord(goal, userInput):
  goal = list(goal)
  returnWord = ''
  for letter in range(len(userInput)):
    if userInput[letter] in goal:
      if userInput[letter] == goal[letter]:
        returnWord += userInput[letter]
      else:
        returnWord += userInput[letter].lower()
      goal[goal.index(userInput[letter])] = '_'
    else:
      returnWord += '_'
  return returnWord
def getPos(word, dictionary):
  dictList = [x for x in dictionary]
  for entry in dictionary:
    for letter in range(5):
      if word[letter].islower():
        if (not word[letter].upper() in entry) or word[letter].upper() == entry[letter]:
          dictList.remove(entry)
          break
      else:
        if not(word[letter] == entry[letter] or word[letter] == '_'):
          dictList.remove(entry)
          break
  return dictList
def getInput(dictionary, choiceDictionary):
  userInput = input()
  while not userInput.upper() in choiceDictionary:
    if userInput.startswith('checkword'):
      print(getPos(userInput.split(' ')[1], dictionary))
      userInput = input()
    else:
      print('That is not a valid word.')
      userInput = input('Please input a 5 letter word.\n')
  return userInput.upper()
wordList = getDictFromFile('wordleChoice.txt')
choiceList = getDictFromFile('wordleDict.txt')
tries = 1
dailyWord = random.choice(wordList).upper()
inputWord = getInput(wordList, choiceList)
print(checkWord(dailyWord, inputWord))
while not inputWord == dailyWord:
  tries += 1
  inputWord = getInput(wordList, choiceList)
  print(checkWord(dailyWord, inputWord))
print('It took you {} tries. Casual'.format(tries))
# if lowercase in spot x, make sure the answer doesnt have the letter in spot x