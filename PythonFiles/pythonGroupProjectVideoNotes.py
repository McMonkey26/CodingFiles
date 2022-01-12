60 second minimum
There are some structures and variables in my section of the code, which all help the code run much more smoothly.
Talk about every structure and variable:
    Structures:
        for i in inp:
            This for loop goes through every letter in the word you put in. This is used so we can reference each letter in the word, and also so if the word has multiple of one letter, it doesn't get skipped
        for letter in range(len(alphabetList)):
            This for loop runs through numbers 0-26 exclusive, the length of alphabetList, which stores every letter in the alphabet. This is used as an index, to run through each letter in the alphabet, one by one. We put an index for loop instead of just going through the list for reasons I will get to in this if statement.
        if i == alphabetList[letter]:
            This if statement checks if the letter we\'re at in the string, i, is the same letter as the letter we\'re at in the alphabet, alphabetList[letter]. This is used to know which letters are in a word, and more specifically, how many of each letter is in a word. If it returns true, then it adds one to the list that stores how much of each letter we have.
    Variables:
            anagrams:
                this variable is initialized to store all words that are determined to be anagrams of the input.
            alphabetList:
                This stores every letter in the alphabet, to shorten the code by about half
            inputAlphabet:
                this stores how many of each letter are in the input word, to reference when checking for an anagram
Challenges of the code:
    This code was somewhat challenging because we had to find a solution to go through every letter of the alphabet. At first, the solution we had made the file incredibly large, as we just checked each letter as its own if statement. However, we realized that if we made a list that stored every letter in the alphabet, we could run through that list in a for loop, and only need 3 lines, instead of 52. However, that raised another problem, in that we had to figure out a way to go through the alphabetList, but also know what position we were at so we know where to add on the inputAlphabet. We solved this by running through the list with a for in range statement, instead of a for in statement, allowing us to reference that to find both the current letter, and the amount of that letter.
Advantages of the code:
    This code is advantageous because it runs through every letter of a string and every letter in the alphabet in only 4 lines. If this were to be hardcoded, instead of using for loops, it would require 52 lines of code, times the length of the input word. Even a one letter word, hardcoded in, would more than double the length of the file. Another, very visible advantage is that it allows the user to input strings of multiple lengths, but there's also a more subtle advantage, in that it lets you make the alphabetList as long as you need, meaning you can have more than just the twenty-six letters in the alphabet. You could also change the list slightly to add capital letters, or every possible character python can handle, and instead of adding hundreds to thousands of lines of code, all you need is a few more elements in a list
How does it affect the overall program:
    This section of the code allows the program to compare words based on only the amount of each letter, without needing to worry about the order.
Would you change anything about the code if you rewrote it:
    If I were to rewrite it, I think the only things I would change would be to space the comment throughout the for loops, instead of one comment at the start, and possibly change the variable i to a name that conveys what it does better.
Is there any situations when the code won't work:
    The only situations where the code won't work is if the input string has characters that are not letters, and the user wants to include those non-letter characters in the anagram check. However, this would be very easy to solve, by just adding those characters to the alphabetList, and changing the length of inputAlphabet and dictAlphabet[] respectively. Also, as I was making this script, I found a simple way to make the list contain every printable ASCII character, meaning the code should now work in every possible string, and will also take about 30 seconds per anagram.
