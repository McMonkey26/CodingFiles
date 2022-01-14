import os
from switch import switch, case #switch is a file i made to have kinda knock-off switch case statements
os.chdir('/Users/jpollack/Desktop/CodingFiles/PythonFiles/adventOfCodeAssignments')
data = []
with open('day2.txt', 'r') as file:
  for i in file:
    data.append(i.rstrip('\n'))
# Part 1 \/\/\/
splitData = map(lambda x: x.split(), data)
horPos = 0
depth = 0
for value in splitData:
  switch(value[0])
  if case('forward'):
    horPos += int(value[1])
  elif case('down'):
    depth += int(value[1])
  elif case('up'):
    depth -= int(value[1])
  else:
    print('wat{}'.format(value))
print('horPos {} * depth {} = answer {}'.format(horPos, depth, horPos*depth))
# Part 1 /\/\/\
# Part 2 \/\/\/
splitData = map(lambda x: x.split(), data)
aim = 0
horPos = 0
depth = 0
for value in splitData:
  switch(value[0])
  if case('forward'):
    horPos += int(value[1])
    depth += aim * int(value[1])
  elif case('down'):
    aim += int(value[1])
  elif case('up'):
    aim -= int(value[1])
  else:
    print('wat{}'.format(value))
print('horPos {} * depth {} = answer {}'.format(horPos, depth, horPos*depth))