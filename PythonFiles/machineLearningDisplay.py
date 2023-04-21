#gets the pygame library
import pygame, random
from PIL import Image
from numpy import *

# fimg = [[x for x in y] for y in asarray(Image.open('./PythonFiles/slime.jpeg'))]
# print(fimg[0][0])
# fimg = [[[255,255,255] for x in range(len(fimg[y]))] for y in range(len(fimg))]
s = 4
fimg = [[[255,255,255] for x in range(1024//s)] for x in range(512//s)]
maps = [[[0,0,0] for x in range(len(fimg[y]))] for y in range(len(fimg))]
# print(fimg[32][32][2])
#initializes the program
pygame.init()
w = len(fimg[0])
h = len(fimg)
#sets up the stage of size width, height
screen = pygame.display.set_mode((w*s, h*s))
#changes the color of the stage, this one will be red RGB
screen.fill([0, 0, 0])

def checkBoundsNew(x, y):
  for a, b, c, d in [
    [x+1,y,x-1,y],
    [x+1,y,x,y+1],
    [x+1,y,x,y-1],
    [x-1,y,x,y+1],
    [x-1,y,x,y-1],
    [x,y-1,x,y+1]
  ]:
    try:
      return sum(maps[a][b]) > sum(maps[x][y]) and sum(maps[c][d]) > sum(maps[x][y])
    except IndexError: pass
  return False
def checkBounds(x, y):
  # try:
  #   return sum(maps[x+1][y]) > sum(maps[x][y]) and sum(maps[x-1][y]) > sum(maps[x][y])
  # except IndexError: pass
  # try:
  #   return sum(maps[x+1][y]) > sum(maps[x][y]) and sum(maps[x][y+1]) > sum(maps[x][y])
  # except IndexError: pass
  # try:
  #   return sum(maps[x+1][y]) > sum(maps[x][y]) and sum(maps[x][y-1]) > sum(maps[x][y])
  # except IndexError: pass
  # try:
  #   return sum(maps[x-1][y]) > sum(maps[x][y]) and sum(maps[x][y+1]) > sum(maps[x][y])
  # except IndexError: pass
  # try:
  #   return sum(maps[x-1][y]) > sum(maps[x][y]) and sum(maps[x][y-1]) > sum(maps[x][y])
  # except IndexError: pass
  # try:
  #   return sum(maps[x][y-1]) > sum(maps[x][y]) and sum(maps[x][y+1]) > sum(maps[x][y])
  # except IndexError: pass
  return False
def higher(x, y, x1, y1):
  try:
    return sum(maps[x1][y1]) > sum(maps[x][y])
  except IndexError:
    return False
def lower(x, y, x1, y1):
  try: 
    return sum(maps[x1][y1]) < sum(maps[x][y])
  except IndexError:
    return False
#Shows the screen to the user
pygame.display.flip()

# maps = [[[0,0,0] for x in range(w)] for y in range(h)]
# fimg = [[[255, 255, 255] for i in range(w)] for i in range(h)]
#control variable for main loop
run = True

count = 0
#main loop
while run:
  #allows you to press the x in the top corner of pygame window and close it
  count += 1
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    #allows for movement with arrow keys
  screen.fill([0, 0, 255])
  for i in range(1):
    for x in range(w):
      for y in range(h):
        if maps[y][x][0] > fimg[y][x][0]: maps[y][x][0] = fimg[y][x][0]
        if maps[y][x][1] > fimg[y][x][1]: maps[y][x][1] = fimg[y][x][1]
        if maps[y][x][2] > fimg[y][x][2]: maps[y][x][2] = fimg[y][x][2]
        # pygame.draw.rect(screen, fimg[y][x], pygame.Rect(x*s, y*s, s, s))
        pygame.draw.rect(screen, maps[y][x], pygame.Rect(x*s, y*s, s, s))
        if checkBoundsNew(y, x) != checkBounds(y, x):
          run = False
          print('aaaa')
        if checkBounds(y, x) or random.random() >= 0.9:
          maps[y][x][0] += 10
          maps[y][x][1] += 10
          maps[y][x][2] += 10
  #updates the screen for the user with anything that happened in the evnets
  pygame.display.flip()
print(count)