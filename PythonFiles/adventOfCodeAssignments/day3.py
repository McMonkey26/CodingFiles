import os
from switch import switch, case #switch is a file i made to have kinda knock-off switch case statements
os.chdir('/Users/jpollack/Desktop/CodingFiles/PythonFiles/adventOfCodeAssignments')
data = []
with open('day3.txt', 'r') as file:
  for i in file:
    data.append(i.rstrip('\n'))
# Part 1 \/\/\/
def pr():
  try:
    print('data:',data)
  except NameError:
    pass
  try:
    print('allDigits:')
    for i in allDigits:
      print(i)
  except NameError:
    pass
  try:
    print('gamma:',gamma)
  except NameError:
    pass
  try:
    print('gamDec:',gamDec)
  except NameError:
    pass
  try:
    print('epsilon:',epsilon)
  except NameError:
    pass
  try:
    print('epsDec:',epsDec)
  except NameError:
    pass
def bintodec(bin):
  digits = list(str(bin))
  dec = 0
  for i in range(len(digits)):
    dec += int(digits[i]) * (2 ** (len(digits) - 1 - i))
  return dec
def mode(array):
  values = {}
  for curVal in array:
    if curVal not in values:
      values[curVal] = 1
    else:
      values[curVal] += 1
  # print(values)
  if values['1'] >= values['0']:
    return 1
  else:
    return 0
def antimode(array):
  values = {}
  for curVal in array:
    if curVal not in values:
      values[curVal] = 1
    else:
      values[curVal] += 1
  print(values)
  if values['0'] >= values['1']:
    return 0
  else:
    return 1
allDigits = [[]for i in range(len(data[0]))]
# pr()
for binary in data:
  for bit in range(len(binary)):
    allDigits[bit].append(binary[bit])
gamma = ''
for bit in allDigits:
  # print('gamma bit',bit, mode(bit))
  gamma += str(mode(bit))

epsilon = ''
for bit in allDigits:
  # print('epsilon bit',bit, antimode(bit))
  epsilon += str(antimode(bit))

gamDec = bintodec(gamma)
epsDec = bintodec(epsilon)
# pr()
print('gamma {} * epsilon {} = power {}'.format(gamDec, epsDec, gamDec * epsDec))
# Part 1 /\/\/\
# Part 2 \/\/\/
o2datas = []
o2Data = list(map(str,data[:]))
count = 0
while len(o2Data) > 1:
  digData = []
  for value in data:
    digData.append(str(value[count]))
  for i in o2Data:
    if i[0] != mode(digData):
      o2Data.remove(i)
  count += 1
  o2datas.append(digData)
print(o2Data)

co2datas = []
co2data = list(map(str,data[:]))
count = 0
while len(co2data) > 1:
  digData = []
  for value in data:
    digData.append(str(value[count]))
  print('1',digData.count('1'))
  print('0',digData.count('0'))
  print('m',antimode(digData))
  for i in co2data:
    if i[0] != antimode(digData):
      co2data.remove(i)
  count += 1
  co2datas.append(digData)
print(co2data)
for i in co2datas:
  print('1:{},0:{},mode:{}'.format(i.count('1'), i.count('0'), mode(i)))
for i in range(len(data)):
  if '010111010' in data[i]:
    print(i)
print(data[17])
print(o2Data)