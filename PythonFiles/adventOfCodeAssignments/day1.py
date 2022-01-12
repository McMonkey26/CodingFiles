import os
os.chdir('/Users/jpollack/Desktop/CodingFiles/PythonFiles/adventOfCodeAssignments')
data = []
with open('day1.txt', 'r') as file:
  for i in file:
    data.append(int(i.rstrip('\n')))
# Part 1 \/\/\/
# increases = 0
# count = 0
# print(data[0] + 'n/a')
# for i in range(len(data)-1):
#   count += 1
#   if data[i+1] > data[i]:
#     increases += 1
#     if count % 10 == 0:
#       print(f'{data[i+1]} (increases) {increases}')
#   else:
#     if count % 10 == 0:
#       print(f'{data[i+1]} (decreases) {increases}')
# print(increases)
# Part 1 /\/\/\
# Part 2 \/\/\/
sums = []
for i in range(len(data) - 2):
  sums.append(data[i] + data[i+1] + data[i+2])
increases = 0
count = 0
print(str(sums[0]) + ' n/a')
for i in range(len(sums)-1):
  count += 1
  if sums[i+1] > sums[i]:
    increases += 1
    if count % 10 == 0:
      print(f'{sums[i+1]} (increases) {increases}')
  else:
    if count % 10 == 0:
      print(f'{sums[i+1]} (decreases) {increases}')
print(increases)