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
  def drawHitbox(self):
    pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height))
  def showData(self):
    Font = pygame.font.Font('freesansbold.ttf', 20)
    text = Font.render('({:3},{:3}) dx:{:2} dy:{:2}'.format(self.rect.x, self.rect.y, self.vel[0], self.vel[1]), False, (255, 255, 255), '#5C94FC')
    screen.blit(text, (0, 0))
  def collideTop(self, platform):
    return (pygame.Rect(self.rect.x, self.rect.y+1, self.rect.width, self.rect.height).colliderect(platform.rect))
  def collideBottom(self, platform):
    return (pygame.Rect(self.rect.x, self.rect.y-1, self.rect.width, self.rect.height).colliderect(platform.rect))
  def collideLeft(self, platform):
    return (pygame.Rect(self.rect.x+1, self.rect.y, self.rect.width, self.rect.height).colliderect(platform.rect))
  def collideRight(self, platform):
    return (pygame.Rect(self.rect.x-1, self.rect.y, self.rect.width, self.rect.height).colliderect(platform.rect))
  def arrowUp(self):
    if self.standing:
      self.vel[1] = -175
  def arrowLeft(self):
    self.vel[0] -= 3
    if self.vel[0] <= -52:
      self.vel[0] = -52
  def arrowRight(self):
    self.vel[0] += 3
    if self.vel[0] >= 52:
      self.vel[0] = 52
  def collide(self):
    if any(map(lambda x:self.collideLeft(x), tiles)):
      self.x -= 1
      self.vel[0] = 0
      self.rect.x = self.x
      self.rect.y = self.y
    if any(map(lambda x:self.collideRight(x), tiles)):
      self.x += 1
      self.vel[0] = 0
      self.rect.x = self.x
      self.rect.y = self.y
    if any(map(lambda x:self.collideBottom(x), tiles)):
      self.y += 1
      self.vel[1] = 0
      self.rect.x = self.x
      self.rect.y = self.y
    if any(map(lambda x:self.collideTop(x), tiles)):
      if self.vel[1] > 0:
        self.vel[1] = 0
      self.standing = True
      self.rect.x = self.x
      self.rect.y = self.y
    else:
      self.standing = False
  def checkBounds(self):
    if self.x > width-self.rect.width:
      self.x = width-self.rect.width
      self.vel[0] = 0
    if self.y > height-self.rect.height:
      self.y = height-self.rect.height
      self.vel[1] = 0
      self.standing = True
    if self.x < 0:
      self.x = 0
      self.vel[0] = 0
    if self.y < 0:
      self.y = 0
      self.vel[1] = 0
  def update(self):
    self.showData()
    self.collide()
    # self.drawHitbox()
    self.x += self.vel[0]/100
    self.y += self.vel[1]/100
    self.rect.x = self.x
    self.rect.y = self.y
    self.vel[1] += 2
    self.vel[0] += 2 if self.vel[0] < 0 else (-2 if self.vel[0] > 0 else 0)
    self.checkBounds()
    

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

def drawGrid():
  for column in range((width+15)//16):
    pygame.draw.line(screen, (255, 255, 255), (column*16, 0), (column*16, height))
  for row in range((height+15)//16):
    pygame.draw.line(screen, (255, 255, 255), (0, row*16), (width, row*16))

tiles = pygame.sprite.Group()
tiles.add(Brick(120, 96))
tiles.add(Brick(152, 96))
tiles.add(Brick(184, 96))
tiles.add(Brick(32, 32))
tiles.add(Brick(48, 32))
tiles.add(Brick(64, 32))
tiles.add(Brick(80, 32))
tiles.add(Brick(96, 32))
tiles.add(Brick(112, 32))
player = Mario(32, 48)


run = True
#main loop
while run:
  pygame.time.wait(0)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        print(player.rect.topleft,'|',player.vel)
  key = pygame.key.get_pressed()
  if key[pygame.K_UP]:
    player.arrowUp()
  if key[pygame.K_LEFT]:
    player.arrowLeft()
  if key[pygame.K_RIGHT]:
    player.arrowRight()
  screen.fill('#5C94FC')
  drawGrid()
  tiles.draw(screen)
  screen.blit(player.image, player.rect.topleft)
  tiles.update()
  player.update()
  pygame.display.flip()