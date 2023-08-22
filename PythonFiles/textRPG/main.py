import keyboard
import time

map = [
  list('###############'),
  list('#             #'),
  list('#      ##     #'),
  list('#      ##     #'),
  list('###############')
]
playerPos = [11, 2]
print(*map, sep='\n')
pressed = False

for i in range(100):
  keyboard.wait("left")

  map[playerPos[1]][playerPos[0]] = 'i'
  for line in map:
    print(''.join(line))
  map[playerPos[1]][playerPos[0]] = ' '
  print(i)
  time.sleep(0.1)