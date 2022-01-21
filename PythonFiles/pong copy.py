#gets the pygame library
import pygame, sys

#initializes the program
pygame.init()

width = 1080
height = 600
#sets up the stage of size width, height
screen = pygame.display.set_mode((width, height))

#changes the color of the stage, this one will be red RGB
screen.fill([0, 0, 0])

class Paddle(pygame.sprite.Sprite):
  def __init__(self, player, x, y):
    super().__init__()
    self.image = pygame.Surface((20, 100))
    self.image.fill((255, 255, 255))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.player = player
    self.velo = 0
  def update(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and self.player == 2:
      self.velo = -2
    elif key[pygame.K_w] and self.player == 1:
      self.velo = -2
    elif key[pygame.K_DOWN] and self.player == 2:
      self.velo = 2
    elif key[pygame.K_s] and self.player == 1:
      self.velo = 2
    else:
      self.velo = 0
    self.rect.y += self.velo
    if self.rect.y < 20:
      self.rect.y = 20
    if self.rect.y > height-self.rect.height-20:
      self.rect.y = height-self.rect.height - 20
    screen.blit(self.image, self.rect.topleft)

class Ball(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.Surface((20, 20))
    self.image.fill((255, 255, 255))
    self.rect = self.image.get_rect()
    self.rect.center = (width/2, height/2)
    self.velo = [2, 2]
  def update(self):
    self.checkScore()
    self.collision(borders)
    self.collision(players)
    self.rect.x += self.velo[0]
    self.rect.y += self.velo[1]
    screen.blit(self.image, self.rect.topleft)
  def checkScore(self):
    if self.rect.x < 0 and len(goals) >= 1:
      print('Player 2 won')
      sys.exit(0)
    if self.rect.x > width and len(goals) >= 2:
      print('Player 1 won')
      sys.exit(0)
  def collision(self, group):
    self.horizontalCollision(group)
    self.verticalCollision(group)
  def horizontalCollision(self, group):
    self.rect.x += self.velo[0]
    if pygame.sprite.spritecollide(self, group, False):
      self.velo[0] = -self.velo[0]
      self.rect.x += self.velo[0]
    else:
      self.rect.x -= self.velo[0]
  def verticalCollision(self, group):
    self.rect.y += self.velo[1]
    if pygame.sprite.spritecollide(self, group, False):
      self.velo[1] = -self.velo[1]
      self.rect.y += self.velo[1]
    else:
      self.rect.y -= self.velo[1]
class Border(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height):
    super().__init__()
    self.image = pygame.Surface((width, height))
    self.image.fill((50, 50, 50))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
class Goal(pygame.sprite.Sprite):
  def __init__(self, player):
    super().__init__()
    if player == 1:
      self.image = pygame.Surface((20, height-40))
      self.image.fill([255, 0, 0])
      self.rect = self.image.get_rect()
      self.rect.topleft = (0, 20)
    elif player == 2:
      self.image = pygame.Surface((20, height-40))
      self.image.fill([0, 0, 255])
      self.rect = self.image.get_rect()
      self.rect.topleft = (width-20, 20)
borders = pygame.sprite.Group()
borders.add(Border(0, 0, width, 20))
borders.add(Border(0, height-20, width, 20))
player1 = Paddle(1, 20, 250)
player2 = Paddle(2, 1040, 250)
players = pygame.sprite.Group()
players.add(player1)
players.add(player2)
balls = pygame.sprite.Group() #this is just so i can make more balls later
balls.add(Ball())
goals = pygame.sprite.Group()
goals.add(Goal(1))
goals.add(Goal(2))
#Shows the screen to the user
pygame.display.flip()

#control variable for main loop
run = True

#main loop
while run:
  #allows you to press the x in the top corner of pygame window and close it
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  screen.fill((0, 0, 0))
  borders.draw(screen)
  goals.draw(screen)
  players.update()
  balls.update()
  #updates the screen for the user with anything that happened in the evnets
  pygame.display.flip()