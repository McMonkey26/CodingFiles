#gets the pygame library
import pygame
GREEN = [0, 255, 0]
WIDTH = 1080
HEIGHT = 600
class Player(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self) #The first line, pygame.sprite.Sprite.__init__(self) is required by Pygame - it runs the built-in Sprite classes initializer.
    self.image = pygame.Surface((50, 50))  #creates a 50 x 50 “surface”
    self.color = GREEN
    self.image.fill(self.color) #fills this surface with green
    self.rect = self.image.get_rect()  #creates a rectangle around “image” surface
    self.rect.topleft = (x, y)
    self.velocity = [4, 0]
  def update(self):
    self.rect.x += self.velocity[0] #moves all sprites in the group + 5 along x axis
    if self.rect.right > WIDTH:
      self.velocity[0] = -4
    if self.rect.left < 0:
      self.velocity[0] = 4
class imageSprite(pygame.sprite.Sprite):
  def __init__(self, image, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = Surface((50, 50))
    self.image = pygame.image.load(image).convert_alpha()
    self.image = pygame.transform.scale(self.image, (50, 50))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.velocity = [0,0]
  def update(self):
    self.rect.x += self.velocity[0]
    self.rect.y += self.velocity[1]
    if self.rect.right > WIDTH:
      self.rect.right = WIDTH
    if self.rect.left < 0:
      self.rect.left = 0
    if self.rect.top < 0:
      self.rect.top = 0
    if self.rect.bottom > HEIGHT:
      self.rect.bottom = HEIGHT

#initializes the program
pygame.init()

#sets up the stage of size width, height
screen = pygame.display.set_mode((1080, 600))

#changes the color of the stage, this one will be red RGB
screen.fill([255, 0, 0])

all_sprites = pygame.sprite.Group()#allows easier control of sprites by grouping them
player = Player(50, 50) #creates a player object
player2 = Player(50, 250)
player2.image.fill([0, 0, 255])
testImage = imageSprite('/Users/jpollack/Desktop/CodingFiles/PythonFiles/marioImages/mario.png', 200, 200)
all_sprites.add(player) #adds the object to the group
all_sprites.add(player2)
all_sprites.add(testImage)

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
  screen.fill([255,0,0])
  all_sprites.draw(screen)
  all_sprites.update()
  #updates the screen for the user with anything that happened in the evnets
  pygame.display.flip()