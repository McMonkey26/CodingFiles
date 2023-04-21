field = [['0' for x in range(64)] for y in range(16)]
start = [0,6]
field[start[1]][start[0]] = '1'
for y in field:
  print(*y, sep='')