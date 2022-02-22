import pygame, random, os
from switch import *
os.chdir('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PythonFiles/pacman')

pygame.init()
screen = pygame.display.set_mode((1000, 600))
screen.fill((0, 0, 0))

wallMap = [
  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
  1,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,1,
  1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,0,1,
  1,0,1,1,1,0,0,2,1,3,3,1,2,0,0,1,1,1,0,1,
  1,0,1,0,0,0,1,1,1,3,3,1,1,1,0,0,0,1,0,1,
  1,0,1,1,1,0,1,0,1,3,3,1,0,1,0,1,1,1,0,1,
  1,0,0,0,1,0,1,0,1,3,3,1,0,1,0,1,0,0,0,1,
  1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,
  1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,
  1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
]
def checkBorders(position, matrixMap):
  pos0 = position//1000
  pos1 = position%1000//50
  borders = [
    [3, 3, 3],
    [3, 3, 3],
    [3, 3, 3]
  ]
  try:
    borders[0][0] = matrixMap[pos0-1][pos1-1] if pos0-1 >= 0 and pos1-1 >= 0 else 2
  except IndexError:
    borders[0][0] = 3
  try:
    borders[0][1] = matrixMap[pos0-1][pos1] if pos0-1 >= 0 and pos1 >= 0 else 2
  except IndexError:
    borders[0][1] = 3
  try:
    borders[0][2] = matrixMap[pos0-1][pos1+1] if pos0-1 >= 0 and pos1+1 >= 0 else 2
  except IndexError:
    borders[0][2] = 3
  try:
    borders[1][0] = matrixMap[pos0][pos1-1] if pos0 >= 0 and pos1-1 >= 0 else 2
  except IndexError:
    borders[1][0] = 3
  try:
    borders[1][1] = matrixMap[pos0][pos1] if pos0 >= 0 and pos1 >= 0 else 2
  except IndexError:
    borders[1][1] = 3
  try:
    borders[1][2] = matrixMap[pos0][pos1+1] if pos0 >= 0 and pos1+1 >= 0 else 2
  except IndexError:
    borders[1][2] = 3
  try:
    borders[2][0] = matrixMap[pos0+1][pos1-1] if pos0+1 >= 0 and pos1-1 >= 0 else 2
  except IndexError:
    borders[2][0] = 3
  try:
    borders[2][1] = matrixMap[pos0+1][pos1] if pos0+1 >= 0 and pos1 >= 0 else 2
  except IndexError:
    borders[2][1] = 3
  try:
    borders[2][2] = matrixMap[pos0+1][pos1+1] if pos0+1 >= 0 and pos1+1 >= 0 else 2
  except IndexError:
    borders[2][2] = 3
  switch(borders[1][1])
  returnList = []
  for pos in borders:
    returnList.append([])
    for x in pos:
      returnList[-1].append((case(x) or case(x+2) or case(x-2)))
  return returnList

  return [list(map(case, x)) for x in borders]
def only(checkList, *indexes):
  return all([checkList[x] for x in indexes]) and not any([checkList[x] for x in range(len(checkList)) if not x in indexes])
wallMap2d = [wallMap[x:x+20] for x in range(len(wallMap)) if x%20==0]
intersectionList = {}
for point in range(len(wallMap)):
  if wallMap[point] == 0 or wallMap[point] == 2:
    border = checkBorders(point*50, wallMap2d)
    tempList = [border[1][2], border[1][0], border[0][1], border[2][1]]
    if not (only(tempList, 0, 1) or only(tempList, 2, 3)):
      intersectionList[((point*50)%1000, (point//20)*50)] = [x for x in range(4) if tempList[x]]
def getImage(borderMap):
  tempImage = pygame.Surface((16, 16))
  spriteMap = pygame.image.load('./walls.png')
  borders = [borderMap[0][1], borderMap[1][2], borderMap[2][1], borderMap[1][0]]
  if only(borders, 0):
    tempImage.blit(spriteMap, (0, 0), (0, 32, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 0)
  elif only(borders, 1):
    tempImage.blit(spriteMap, (0, 0), (0, 32, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 270)
  elif only(borders, 2):
    tempImage.blit(spriteMap, (0, 0), (0, 32, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 180)
  elif only(borders, 3):
    tempImage.blit(spriteMap, (0, 0), (0, 32, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 90)
  elif only(borders, 0, 1):
    tempImage.blit(spriteMap, (0, 0), (0, 0, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 90)
  elif only(borders, 1, 2):
    tempImage.blit(spriteMap, (0, 0), (0, 0, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 0)
  elif only(borders, 2, 3):
    tempImage.blit(spriteMap, (0, 0), (0, 0, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 270)
  elif only(borders, 3, 0):
    tempImage.blit(spriteMap, (0, 0), (0, 0, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 180)
  elif only(borders, 0, 2):
    tempImage.blit(spriteMap, (0, 0), (16, 0, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 90)
  elif only(borders, 1, 3):
    tempImage.blit(spriteMap, (0, 0), (16, 0, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 0)
  elif only(borders, 0, 1, 2):
    tempImage.blit(spriteMap, (0, 0), (0, 16, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 0)
  elif only(borders, 1, 2, 3):
    tempImage.blit(spriteMap, (0, 0), (0, 16, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 270)
  elif only(borders, 2, 3, 0):
    tempImage.blit(spriteMap, (0, 0), (0, 16, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 180)
  elif only(borders, 3, 0, 1):
    tempImage.blit(spriteMap, (0, 0), (0, 16, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 90)
  elif all(borders):
    tempImage.blit(spriteMap, (0, 0), (16, 16, 16, 16))
  else:
    tempImage.blit(spriteMap, (0, 0), (16, 32, 16, 16))
  return pygame.transform.scale(tempImage, (50, 50))
class Wall(pygame.sprite.Sprite):
  def __init__(self, pos):
    super().__init__()
    self.image = pygame.Surface((50, 50))
    self.rect = self.image.get_rect()
    self.rect.topleft = (pos%1000, (pos//1000)*50)
    border = checkBorders(pos, wallMap2d)
    self.image = getImage(border)
class Dot(pygame.sprite.Sprite):
  def __init__(self, pos):
    super().__init__()
    self.image = pygame.Surface((10, 10))
    self.image.fill((255, 255, 255))
    self.rect = self.image.get_rect()
    self.rect.center = (pos%1000+25, (pos//1000)*50+25)
  def collide(self, pacman):
    if pygame.sprite.collide_rect(self, pacman):
      self.kill()
class Ghost(pygame.sprite.Sprite):
  def __init__(self, color, pos):
    super().__init__()
    self.image = pygame.Surface((16, 16))
    self.sprite = pygame.image.load('./pacmanSprites.png').convert_alpha()
    self.color = color
    self.baseCoords = [3, 64 + 16 * self.color, 16, 16]
    self.image.blit(self.sprite, (0, 0), self.baseCoords)
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.topleft = (pos%1000, (pos//1000)*50)
    self.direction = Dir.RIGHT
    self.frame = 0
    self.velo = [10, 0]
  def setImage(self):
    self.baseCoords[1] = 64 + 16 * self.color
    self.baseCoords[0] = 3 + (self.frame//10 % 2) * 16 + (self.direction * 32)
    self.image = pygame.Surface((16, 16))
    self.image.blit(self.sprite, (0, 0), self.baseCoords)
    self.image = pygame.transform.scale(self.image, (50, 50))
  def update(self):
    self.switchDirec()
    switch(self.direction)
    if case(Dir.LEFT): self.velo = [-10, 0]
    elif case(Dir.RIGHT): self.velo = [10, 0]
    elif case(Dir.UP): self.velo = [0, -10]
    elif case(Dir.DOWN): self.velo = [0, 10]
    self.frame += 1
    self.setImage()
    if self.frame%2 == 0:
      self.rect.x += self.velo[0]
      self.rect.y += self.velo[1]
    screen.blit(self.image, self.rect)
  def switchDirec(self):
    if self.rect.topleft in intersectionList.keys():
      if self.direction in intersectionList[self.rect.topleft] and random.random() > 0.4:
        return None
      self.direction = random.choice(intersectionList[self.rect.topleft])
class Direction:
  def __init__(self):
    self.RIGHT = 0
    self.LEFT = 1
    self.UP = 2
    self.DOWN = 3
Dir = Direction()
walls = pygame.sprite.Group()
dots = pygame.sprite.Group()
ghosts = pygame.sprite.Group()
color = 0
for tile in range(len(wallMap)):
  if wallMap[tile] == 1:
    walls.add(Wall(tile*50))
  elif wallMap[tile] == 0:
    dots.add(Dot(tile*50))
  elif wallMap[tile] == 2:
    ghosts.add(Ghost(color%4, tile*50))
    color += 1
class Pacman(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.Surface((16, 16))
    self.sprite = pygame.image.load('./pacmanSprites.png').convert_alpha()
    self.image.blit(self.sprite, (0, 0), (0, 0, 16, 16))
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.topleft = (450, 400)
    self.direction = 'r'
    self.frame = 0
    self.velo = [0, 0]
    self.dead = False
    self.died = False
    self.deathFrame = 0
    self.lives = 3
  def setImage(self):
    global winState
    spriteCoords = [3, 0, 16, 16]
    if (self.frame%20 >= 10): spriteCoords[0] = 19
    switch(self.direction)
    if case(pygame.K_LEFT): spriteCoords[1] = 16
    elif case(pygame.K_UP): spriteCoords[1] = 32
    elif case(pygame.K_DOWN): spriteCoords[1] = 48
    if self.dead:
      spriteCoords[1] = 0
      spriteCoords[0] = 35 + 16 * (self.deathFrame//5)
      if self.deathFrame == 70:
        self.lives -= 1
        self.died = True
        if self.lives == 0:
          winState = 0 #lost
    self.image = pygame.Surface((16, 16))
    self.image.blit(self.sprite, (0, 0), spriteCoords)
    self.image = pygame.transform.scale(self.image, (50, 50))
  def update(self):
    global winState
    switch(self.velo)
    if case([-10, 0]): self.direction = pygame.K_LEFT
    elif case([10, 0]): self.direction = pygame.K_RIGHT
    elif case([0, -10]): self.direction = pygame.K_UP
    elif case([0, 10]): self.direction = pygame.K_DOWN
    self.frame += 1
    if self.dead: self.deathFrame += 1
    self.setImage()
    self.turn()
    if self.velo[0] < 0 and any(list(map(lambda x: pygame.Rect(self.rect.x-1, self.rect.y, self.rect.width, self.rect.height).colliderect(x), walls))): self.velo[0] = 0
    if self.velo[0] > 0 and any(list(map(lambda x: pygame.Rect(self.rect.x+1, self.rect.y, self.rect.width, self.rect.height).colliderect(x), walls))): self.velo[0] = 0
    if self.velo[1] < 0 and any(list(map(lambda x: pygame.Rect(self.rect.x, self.rect.y-1, self.rect.width, self.rect.height).colliderect(x), walls))): self.velo[1] = 0
    if self.velo[1] > 0 and any(list(map(lambda x: pygame.Rect(self.rect.x, self.rect.y+1, self.rect.width, self.rect.height).colliderect(x), walls))): self.velo[1] = 0
    if self.frame%2 == 0: self.rect.x += self.velo[0]
    if self.frame%2 == 0: self.rect.y += self.velo[1]
    if pygame.sprite.spritecollide(self, ghosts, False): self.die()
    if len(dots.sprites()) == 0:
      winState = 2 #won
    screen.blit(self.image, self.rect)
    # pygame.draw.rect(screen, (180, 180, 180), self.rect)
  def turn(self):
    if self.dead: return None
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and not any(list(map(lambda x: pygame.Rect(self.rect.x, self.rect.y-1, self.rect.width, self.rect.height).colliderect(x), walls))):
      self.velo[0] = 0
      self.velo[1] = -10
    elif key[pygame.K_DOWN] and not any(list(map(lambda x: pygame.Rect(self.rect.x, self.rect.y+1, self.rect.width, self.rect.height).colliderect(x), walls))):
      self.velo[0] = 0
      self.velo[1] = 10
    elif key[pygame.K_LEFT] and not any(list(map(lambda x: pygame.Rect(self.rect.x-1, self.rect.y, self.rect.width, self.rect.height).colliderect(x), walls))):
      self.velo[0] = -10
      self.velo[1] = 0
    elif key[pygame.K_RIGHT] and not any(list(map(lambda x: pygame.Rect(self.rect.x+1, self.rect.y, self.rect.width, self.rect.height).colliderect(x), walls))):
      self.velo[0] = 10
      self.velo[1] = 0
  def die(self):
    global winState
    self.velo = [0, 0]
    self.dead = True
    for ghost in ghosts: ghost.kill()
    
  def start(self):
    if self.lives == 0:
      return None
    self.rect.topleft = (450, 400)
    self.dead = False
    self.died = False
    self.deathFrame = 0
    self.setImage()
    color = 0
    for tile in range(len(wallMap)):
      if wallMap[tile] == 2:
        ghosts.add(Ghost(color%4, tile*50))
        color += 1


pacman = Pacman()

winState = 1
run = True
clock = pygame.time.Clock()

def gameScreen():
  screen.fill((0, 0, 0))
  pacman.update()
  list(map(lambda x:x.collide(pacman), dots))
  walls.draw(screen)
  dots.draw(screen)
  ghosts.update()
  pygame.display.flip()
def winScreen():
  screen.fill((0, 0, 0))
  font = pygame.font.SysFont('arial', 80, True)
  textSprite = font.render('You Win!', True, (255, 255, 255))
  textRect = textSprite.get_rect()
  textRect.center = (500, 300)
  screen.blit(textSprite, textRect)
  pygame.display.flip()
def loseScreen():
  screen.fill((0, 0, 0))
  font = pygame.font.SysFont('arial', 80, True)
  textSprite = font.render('GAME OVER', True, (180, 40, 40))
  textRect = textSprite.get_rect()
  textRect.center = (500, 300)
  screen.blit(textSprite, textRect)
  pygame.display.flip()
while run:
  clock.tick(40)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        print(pacman.lives,'lives')
        print(winState,'win')
      if event.key == pygame.K_SPACE and pacman.died and winState == 1:
        pacman.start()
  if winState == 0:
    loseScreen()
  elif winState == 1:
    gameScreen()
  elif winState == 2:
    winScreen()