# started off with encrypted key (ZLYYTY)
# went through possible caesar shifts until i found an actual word (FREEZE)

# assign encrypted text and cipher key (extended to length of encrypted text) to variables
cipherText = 'yyiemwbvvxnxmvypsmrrxipyjjxmnrtwpmeiyyiymmavvwdesuizdvdklmmknjjsqxdkas'
cipherKey = 'freeze'*(len(cipherText)//6+1)
# assign alphabet to variable to find letter numbers
alphabet = 'abcdefghijklmnopqrstuvwxyz'*2
# assign empty variable to store the decrypted text
decodedText = ''
# loop through every letter in encrypted text
for i in range(len(cipherText)):
  # assign a variable for the current letter
  letter = cipherText[i]
  # assign a variable for the current letter's position
  alphLetter = alphabet.find(letter)
  # assign a variable for the current letter in the cipher
  cipherLetter = cipherKey[i]
  # assign a variable for it's position
  alphCipher = alphabet.find(cipherLetter)
  # assign a variable for the decrypted letters' position
  # gets the position by subtracting the cipher letter's position from the encrypted letter's position
  decodedLetterPos = alphLetter - alphCipher
  # assign a variable for the decrypted letter
  decodedLetter = alphabet[decodedLetterPos]
  # print the letter, cipher, and decoded letter and their positions for testing
  print('Current letter:{} [{:2}]'.format(letter, alphLetter), end=' | ')
  print('Current cipher:{} [{:2}]'.format(cipherLetter, alphCipher), end=' | ')
  print('Decoded letter:{} [{:2}]'.format(decodedLetter, decodedLetterPos))
  # add the decoded letter to the decrypted text variable
  decodedText += decodedLetter
# print out the decoded text
print(decodedText)
