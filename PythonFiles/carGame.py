#gets the pygame library
import pygame

#initializes the program
pygame.init()

#sets up the stage of size width, height
screen = pygame.display.set_mode(((width:=600), (height:=750)))
screen.fill([0, 0, 0])

speed = 3

class Road(pygame.sprite.Sprite):
  def __init__(self, yLevel):
    super().__init__()
    self.image = pygame.Surface((600, 600))
    self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PythonFiles/road.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (600, 600))
    self.rect = self.image.get_rect()
    self.rect.topleft = (0, yLevel)
  def update(self):
    self.rect.y += speed
    if self.rect.y >= 1200:
      self.rect.y -= 2400
background = pygame.sprite.Group()
background.add(Road(0))
background.add(Road(600))
background.add(Road(1200))
background.add(Road(1800))

class Car(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((100, 180))
    self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PythonFiles/guschillin.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (100, 180))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.velo = [0, 0]
  def move(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
      self.velo[0] = -speed
    elif key[pygame.K_d]:
      self.velo[0] = speed
    else:
      self.velo[0] = 0
    if key[pygame.K_w]:
      self.velo[1] = -speed
    elif key[pygame.K_s]:
      self.velo[1] = speed
    else:
      self.velo[1] = 0
  def update(self):
    self.move()
    self.rect.x += self.velo[0]
    self.rect.y += self.velo[1]
    if self.rect.x < 0:
      self.rect.x = 0
      self.velo[0] = 0
    if self.rect.right > width:
      self.rect.right = width
      self.velo[0] = 0
    if self.rect.y < 0:
      self.rect.y = 0
      self.velo[1] = 0
    if self.rect.bottom > height:
      self.rect.bottom = height
      self.velo[1] = 0
carSprite = Car(300, 600)

run = True
#main loop
while run:
  #allows you to press the x in the top corner of pygame window and close it
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  #updates the screen for the user with anything that happened in the evnets
  screen.fill((0, 0, 0))
  carSprite.update()
  background.update()
  background.draw(screen)
  screen.blit(carSprite.image, carSprite.rect.topleft)
  pygame.display.flip()