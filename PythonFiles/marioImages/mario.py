#gets the pygame library
import pygame, os

#initializes the program
pygame.init()

#sets up the stage of size width, height
screen = pygame.display.set_mode(((width:=240), (height:=240)))
#changes the color of the stage
screen.fill([92, 148, 252])
# 5C94FC
#Shows the screen to the user
pygame.display.flip()
class player:
  def __init__(self, name, x, y, width, height):
    self.image = pygame.transform.scale(pygame.image.load('/Users/jpollack/Desktop/CodingFiles/PythonFiles/marioImages/'+name.lower()+'.png').convert_alpha(), (width, height))
    self.name = name
    self.hitbox = pygame.Rect(x, y, width, height)
    self.x = x
    self.y = y
    self.width = width
    self.height = height
    self.xSpeed = 0
    self.ySpeed = 0
    self.standing = False
    self.leftCol = []
    self.rightCol = []
    self.topCol = []
    self.bottomCol = []
  def draw(self):
    self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
    self.leftCol = []
    self.rightCol = []
    self.topCol = []
    self.bottomCol = []
    screen.blit(self.image, (self.x, self.y))

class tile:
  def __init__(self, block, x, y, contents=None):
    self.block = block
    self.image = pygame.transform.scale(pygame.image.load('/Users/jpollack/Desktop/CodingFiles/PythonFiles/marioImages/'+block+'.png').convert_alpha(), (16, 16))
    self.x = x
    self.y = height-y
    self.hitbox = pygame.Rect(x, height-y, 16, 16)
    self.topBox = pygame.Rect(x, height-y-1, 16, 1)
    self.bottomBox = pygame.Rect(x, height-y+16, 16, 1)
    self.leftBox = pygame.Rect(x-1, height-y, 1, 16)
    self.rightBox = pygame.Rect(x+16, height-y, 1, 16)
    self.hitboxes = self.hitbox, self.topBox, self.bottomBox, self.leftBox, self.rightBox
  def draw(self):
    self.hitbox = pygame.Rect(self.x, self.y, 16, 16)
    self.topBox = pygame.Rect(self.x, self.y-1, 16, 1)
    self.bottomBox = pygame.Rect(self.x, self.y+16, 16, 1)
    self.leftBox = pygame.Rect(self.x-1, self.y, 1, 16)
    self.rightBox = pygame.Rect(self.x+16, self.y, 1, 16)
    self.hitboxes = self.hitbox, self.topBox, self.bottomBox, self.leftBox, self.rightBox
    screen.blit(self.image, (self.x, self.y))
  def drawHitbox(self):
    self.hitbox = pygame.Rect(self.x, self.y, 16, 16)
    self.topBox = pygame.Rect(self.x, self.y-1, 16, 1)
    self.bottomBox = pygame.Rect(self.x, self.y+16, 16, 1)
    self.leftBox = pygame.Rect(self.x-1, self.y, 1, 16)
    self.rightBox = pygame.Rect(self.x+16, self.y, 1, 16)
    self.hitboxes = self.hitbox, self.topBox, self.bottomBox, self.leftBox, self.rightBox
    pygame.draw.rect(screen, (255, 0, 0), self.hitbox)
    pygame.draw.rect(screen, (0, 255, 0), self.topBox)
    pygame.draw.rect(screen, (0, 255, 0), self.bottomBox)
    pygame.draw.rect(screen, (0, 255, 0), self.leftBox)
    pygame.draw.rect(screen, (0, 255, 0), self.rightBox)

#control variable for main loop
mario = player('mario', 32, height-48, 16, 16)
bricks = [
  tile('brick', 320, 96),
  tile('brick', 352, 96),
  tile('brick', 384, 96),
]
questions = [
  tile('question',256, 96),
  tile('question', 336, 96),
  tile('question', 368, 96),
  tile('question', 352, 160),
]
ground = []
for i in range(68):
  ground.append(tile('ground', i*16, 16))
  ground.append(tile('ground', i*16, 32))
pipes = [
  tile('pipeBottomLeft', 448, 48),
  tile('pipeBottomRight', 464, 48),
  tile('pipeTopLeft', 448, 64),
  tile('pipeTopRight', 464, 64),
]
allTiles = []
for tileset in [bricks, questions, ground, pipes]:
  for tile in tileset:
    allTiles.append(tile)
run = True
#main loop
while run:
  testHitbox = pygame.Rect(mario.x, mario.y, mario.width, mario.height)
  testHitbox.x += mario.xSpeed / 100
  testHitbox.y += mario.ySpeed / 100
  for tile in allTiles:
    mario.leftCol.append(   testHitbox.colliderect(tile.leftBox))
    mario.rightCol.append(  testHitbox.colliderect(tile.rightBox))
    mario.topCol.append(    testHitbox.colliderect(tile.topBox))
    mario.bottomCol.append( testHitbox.colliderect(tile.bottomBox))
    if testHitbox.colliderect(tile.bottomBox) and tile.block == 'question':
      tile.block = 'hitQuestion'
      tile.image = pygame.transform.scale(pygame.image.load('/Users/jpollack/Desktop/CodingFiles/PythonFiles/marioImages/hitQuestion.png').convert_alpha(), (16, 16))
  if any(mario.leftCol) or any(mario.rightCol):
    mario.xSpeed = 0
  if any(mario.topCol) or any(mario.bottomCol):
    mario.ySpeed = 0
  if any(mario.topCol):
    mario.standing = True
  else:
    mario.standing = False
  mario.x += mario.xSpeed / 100
  mario.y += mario.ySpeed / 100
  mario.ySpeed += 2
  mario.xSpeed += 2 if mario.xSpeed < 0 else (-2 if mario.xSpeed > 0 else 0)
  if mario.x >= width-mario.width:
    mario.x = width-mario.width
    mario.xSpeed = 0
  if mario.x <= 0:
    mario.x = 0
    mario.xSpeed = 0
  key = pygame.key.get_pressed()
  if key[pygame.K_LEFT]:
    if mario.xSpeed >= -47:
      mario.xSpeed -= 3
    else:
      mario.xSpeed = -50
  if key[pygame.K_RIGHT]:
    if mario.xSpeed <= 47:
      mario.xSpeed += 3
    else:
      mario.xSpeed = 50
  if key[pygame.K_UP] and mario.standing:
    if not mario.xSpeed == 0:
      mario.ySpeed = -175
    else:
      mario.ySpeed = -150
  #allows you to press the x in the top corner of pygame window and close it
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  if mario.x > 120:
    mario.x -= 1
    for tile in allTiles:
      tile.x -= 1
  if mario.x < 10 and allTiles[7].x < 0:
    mario.x += 1
    for tile in allTiles:
      tile.x += 1
  if mario.y > height:
    print('You lose!')
    break
  screen.fill('#5C94FC')
  mario.draw()
  for tile in allTiles:
    tile.draw()
  #updates the screen for the user with anything that happened in the evnets
  pygame.display.flip()