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
class Mario(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self) #Necessary pygame setup line
    self.image = pygame.Surface((16, 16))
    self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PythonFiles/marioImages/mario.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (16, 16))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, height-y)
    self.x = x
    self.y = height-y
    self.vel = [0.0, 0.0]
    self.standing = False
  def collideTop(self, platform):
    return (pygame.Rect(self.rect.x, self.rect.y + self.vel[1]+1, self.rect.width, self.rect.height).colliderect(platform.rect))
  def collideBottom(self, platform):
    return (pygame.Rect(self.rect.x, self.rect.y + self.vel[1]-1, self.rect.width, self.rect.height).colliderect(platform.rect))
  def collideLeft(self, platform):
    return (pygame.Rect(self.rect.x + self.vel[0]+1, self.rect.y, self.rect.width, self.rect.height).colliderect(platform.rect))
  def collideRight(self, platform):
    return (pygame.Rect(self.rect.x + self.vel[0]-1, self.rect.y, self.rect.width, self.rect.height).colliderect(platform.rect))
  def arrowUp(self):
    self.vel[1] -= 10
    if self.vel[1] <= -50:
      self.vel[1] = -50
  def arrowDown(self):
    self.vel[1] += 2
    if self.vel[1] >= 50:
      self.vel[1] = 50
  def arrowLeft(self):
    self.vel[0] -= 1
    if self.vel[0] <= -50:
      self.vel[0] = -50
  def arrowRight(self):
    self.vel[0] += 1
    if self.vel[0] >= 50:
      self.vel[0] = 50
  def update(self):
    if any(map(lambda x:self.collideLeft(x), tiles)):
      player.x -= 1
      player.vel[0] = 0
    if any(map(lambda x:self.collideRight(x), tiles)):
      player.x += 1
      player.vel[0] = 0
    if any(map(lambda x:self.collideTop(x), tiles)):
      player.y -= 1
      player.vel[1] = 0
    if any(map(lambda x:self.collideBottom(x), tiles)):
      player.y += 1
      player.vel[1] = 0
    self.x += self.vel[0]/2
    self.y += self.vel[1]/4
    self.rect.x = self.x
    self.rect.y = self.y
    self.vel[1] += 0.125
    if self.rect.y > 200:
      self.vel[1] = 0
    if self.rect.x > width-self.rect.width:
      self.rect.x = width-self.rect.width
      self.vel[0] = 0
    if self.rect.y > height-self.rect.height:
      self.rect.y = height-self.rect.height
      self.vel[1] = 0
    if self.rect.x < 0:
      self.rect.x = 0
      self.vel[0] = 0
    if self.rect.y < 0:
      self.rect.y = 0
      self.vel[1] = 0
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
    self.frame = 0
    self.standing = False
    self.running = False
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

class Brick(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self) #Necessary pygame setup line
    self.image = pygame.Surface((16, 16))
    self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PythonFiles/marioImages/brick.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (16, 16))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, height-y)
  def update(self):
    pass


tiles = pygame.sprite.Group()
tiles.add(Brick(120, 96))
tiles.add(Brick(152, 96))
tiles.add(Brick(184, 96))
player = Mario(32.0, 48.0)


run = True
#main loop
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        player.arrowLeft()
      if event.key == pygame.K_UP:
        player.arrowUp()
      if event.key == pygame.K_RIGHT:
        player.arrowRight()
      if event.key == pygame.K_DOWN:
        player.arrowDown()
      if event.key == pygame.K_SPACE:
        print(player.rect.topleft,'|',player.vel)
  screen.fill('#5C94FC')
  tiles.draw(screen)
  screen.blit(player.image, player.rect.topleft)
  tiles.update()
  player.update()
  pygame.display.flip()