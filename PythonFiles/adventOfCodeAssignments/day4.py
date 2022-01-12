import os
from switch import * #switch is a file i made to have kinda knock-off switch case statements
os.chdir('/Users/jpollack/Desktop/CodingFiles/PythonFiles/adventOfCodeAssignments')
data = []
with open('day4.txt', 'r') as file:
  for i in file:
    data.append(i.rstrip('\n'))
board = 0
bingos = {}
for line in data:
  if line == '':
    board += 1
  else:
    bingos[str(board)] = 