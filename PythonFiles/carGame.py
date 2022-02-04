#gets the pygame library
import pygame, random

#initializes the program
pygame.init()

#sets up the stage of size width, height
screen = pygame.display.set_mode(((width:=600), (height:=750)))
screen.fill([0, 0, 0])

speed = 10
crashed = False

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
class Base(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((80, 80))
    self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PythonFiles/base.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (80,80))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
  def update(self):
    self.rect.y += speed
    if self.rect.y >= height:
      carSprite.points += 1
      carSprite.coinText = pygame.font.SysFont('arial', 30).render('Coins: {}'.format(carSprite.coins), True, (100, 255, 100))
      carSprite.coinRect = carSprite.coinText.get_rect(topright=(width, 0))
      carSprite.pointText = pygame.font.SysFont('arial', 30).render('Points: {}'.format(carSprite.points), True, (100, 255, 100))
      carSprite.pointRect = carSprite.pointText.get_rect(topleft=(0, 0))
      try:
        pygame.time.set_timer(pygame.USEREVENT, (2000//carSprite.points) if carSprite.points < 8 else 250)
      except ZeroDivisionError:
        pygame.time.set_timer(pygame.USEREVENT, 2000)
      self.kill()
bases = pygame.sprite.Group()
class Coin(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((40, 40))
    self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PythonFiles/rings.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (40, 40))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
  def update(self):
    self.rect.y += speed
    if pygame.sprite.spritecollide(self, bases, False) or self.rect.y >= height:
      self.kill()
coins = pygame.sprite.Group()
class Car(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((100, 180))
    self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PythonFiles/guschillin.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (100, 180))
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.velo = [0, 0]
    self.crashed = False
    self.coins = 0
    self.points = 0
    self.coinText = pygame.font.SysFont('arial', 30).render('Coins: {}'.format(self.coins), True, (100, 255, 100))
    self.coinRect = self.coinText.get_rect(topright=(width, 0))
    self.pointText = pygame.font.SysFont('arial', 30).render('Points: {}'.format(self.points), True, (100, 255, 100))
    self.pointRect = self.pointText.get_rect(topleft=(0, 0))
  def collide(self, group):
    return pygame.sprite.spritecollide(self, group, False)
  def crash(self):
    global crashed
    self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PythonFiles/deadGus.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (100, 180))
    crashed = True
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
    if self.collide(bases):
      self.crash()
    for hit in self.collide(coins):
      hit.kill()
      self.coins += 1
    self.coinText = pygame.font.SysFont('arial', 30).render('Coins: {}'.format(self.coins), True, (100, 255, 100))
    self.coinRect = self.coinText.get_rect(topright=(width, 0))
    self.pointText = pygame.font.SysFont('arial', 30).render('Points: {}'.format(self.points), True, (100, 255, 100))
    self.pointRect = self.pointText.get_rect(topleft=(0, 0))
carSprite = Car(300, 600)
pygame.time.set_timer(pygame.USEREVENT, 2000)
pygame.time.set_timer(pygame.USEREVENT+1, 500)

def gameLoop():
  global run, frame, clock
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.USEREVENT:
      bases.add(Base(random.randint(0, width), -60))
    if event.type == pygame.USEREVENT+1:
      coins.add(Coin(random.randint(0, width), -30))
  #updates the screen for the user with anything that happened in the evnets
  screen.fill((0, 0, 0))
  carSprite.update()
  background.update()
  bases.update()
  coins.update()
  background.draw(screen)
  bases.draw(screen)
  coins.draw(screen)
  screen.blit(carSprite.image, carSprite.rect.topleft)
  screen.blit(carSprite.pointText, carSprite.pointRect.topleft)
  screen.blit(carSprite.coinText, carSprite.coinRect.topleft)
  # screen.blit(pygame.font.SysFont('arial', 30).render(str(int(clock.get_fps())), True, (100, 255, 100)), pygame.font.SysFont('arial', 30).render(str(int(clock.get_fps())), True, (100, 255, 100)).get_rect(topleft=(0, 0)).topleft)
def winScreen():
  global run, crashed
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        crashed = False
        carSprite.points = 0
        carSprite.coins = 0
        for sprite in bases:
          sprite.kill()
        for sprite in coins:
          sprite.kill()
        carSprite.rect.center = (width/2, height/2)
        carSprite.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PythonFiles/guschillin.png').convert_alpha()
        carSprite.image = pygame.transform.scale(carSprite.image, (100, 180))
        carSprite.coinText = pygame.font.SysFont('arial', 30).render('Coins: {}'.format(carSprite.coins), True, (100, 255, 100))
        carSprite.coinRect = carSprite.coinText.get_rect(topright=(width, 0))
        carSprite.pointText = pygame.font.SysFont('arial', 30).render('Points: {}'.format(carSprite.points), True, (100, 255, 100))
        carSprite.pointRect = carSprite.pointText.get_rect(topleft=(0, 0))
  screen.fill((0, 0, 0))
  background.draw(screen)
  bases.draw(screen)
  screen.blit(carSprite.image, carSprite.rect.topleft)
  screen.blit(pygame.font.SysFont('arial', 40).render('You evaded {} base{}.'.format(carSprite.points, '' if carSprite.points == 1 else 's'), True, (255, 255, 255)), pygame.font.SysFont('arial', 40).render('You evaded {} base{}.'.format(carSprite.points, '' if carSprite.points == 1 else 's'), True, (255, 255, 255)).get_rect(center=(width/2, height/2)).topleft)
  screen.blit(pygame.font.SysFont('arial', 40).render('You got {} coin{}.'.format(carSprite.coins, '' if carSprite.coins == 1 else 's'), True, (255, 255, 255)), pygame.font.SysFont('arial', 40).render('You got {} coin{}'.format(carSprite.coins, '' if carSprite.coins == 1 else 's'), True, (255, 255, 255)).get_rect(center=(width/2, height/2+40)).topleft)
  screen.blit(pygame.font.SysFont('arial', 40).render('Try getting good.', True, (255, 255, 255)), pygame.font.SysFont('arial', 40).render('Try getting good.', True, (255, 255, 255)).get_rect(center=(width/2, height/2+80)).topleft)
  screen.blit(pygame.font.SysFont('arial', 40).render('Press SPACE to restart', True, (255, 255, 255)), pygame.font.SysFont('arial', 40).render('Press SPACE to restart', True, (255, 255, 255)).get_rect(center=(width/2, height/2+120)).topleft)
run = True
clock = pygame.time.Clock()
frame = 0
#main loop
while run:
  clock.tick(60)
  frame += 1
  if not crashed:
    gameLoop()
  else:
    winScreen()
  pygame.display.flip()