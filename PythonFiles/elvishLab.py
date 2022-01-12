#get a word from the user
word0 = input("Put in a word: ")

splitWords = word0.split()

for word in splitWords:
    wordStage1 = word.upper()
    wordStage2 = wordStage1.replace("A", "E")
    wordStage2 = wordStage2.replace("I", "E")
    wordStage2 = wordStage2.replace("O", "E")
    wordStage2 = wordStage2.replace("U", "E")

    wordStage3 = wordStage2
    if(wordStage3[len(wordStage3)-1] == "S"):
        wordStage3 = wordStage3[:len(wordStage3)-1]
        wordStage3 += "Y"

    wordStage4 = wordStage3[1:]
    wordStage4 += wordStage3[0]
    print(wordStage4)
