#Map Key:
#T -> Tree
#E -> Ground
#U -> Ledge (walk down from up)
#D -> Ledge (walk down from down)
#L -> Ledge (walk down from left)
#R -> Ledge (walk down from right)
#G -> Grass
#P -> Path

#NPC Key
#N -> NPC
#0 -> No NPC

#Level Key:
#0-9 -> Level
#Level difference of 1 is a ledge
#Level difference of 0.5 doesn't show

#20x20 window size

import os, random, pygame
from switch import switch, case
os.chdir('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PokemonWorld')
world = []
with open('./worldData.txt', 'r') as file:
  for line in file:
    world.append(line.rstrip('\n'))
tileMap = list(map(list, world))
[*map(lambda x:print(''.join(x)), tileMap)]

pygame.init()

screen = pygame.display.set_mode(((width:=1024), (height:=448)))

screen.fill([255, 255, 255])

pygame.display.flip()

run = True
class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.Surface((16, 16))
    self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PokemonWorld/images/playerDown.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (16, 16))
    self.rect = self.image.get_rect()
    self.rect.topleft = (160, 160)
    (self.x, self.y) = self.rect.topleft
  def update(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
      self.x -= 3.2
    if key[pygame.K_w]:
      self.y -= 3.2
    if key[pygame.K_d]:
      self.x += 3.2
    if key[pygame.K_s]:
      self.y += 3.2
    self.rect.topleft = (self.x, self.y)
    screen.blit(self.image, self.rect.topleft)
class Tree(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((64, 80))
    self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PokemonWorld/images/tree.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (64, 80))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x-16, y-32)
    self.x = x-16
    self.y = y-32
class Grass(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((16, 16))
    self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PokemonWorld/images/tall_grass.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (16, 16))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.x = x
    self.y = y
class Ledge(pygame.sprite.Sprite):
  def __init__(self, x, y, direc):
    super().__init__()
    self.image = pygame.Surface((16, 16))
    switch(direc.lower())
    if case('u'):
      self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PokemonWorld/images/upLedgeMid.png').convert_alpha()
    else:
      self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PokemonWorld/images/noTextures.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (16, 16))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.x = x
    self.y = y
class Ground(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((16, 16))
    self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PokemonWorld/images/grass.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (16, 16))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.x = x
    self.y = y
me = Player()

all_sprites = pygame.sprite.Group()
ground_layer = pygame.sprite.Group()
trees = pygame.sprite.Group()
tall_grass = pygame.sprite.Group()
ledges = pygame.sprite.Group()
for row in range(len(tileMap)):
  y = row * 16
  for column in range(len(tileMap[row])):
    x = column * 16
    ground_layer.add(Ground(x, y))
for row in range(len(tileMap)):
  y = row * 16
  for column in range(len(tileMap[row])):
    x = column * 16
    switch(tileMap[row][column].lower())
    if case('t'):
      tempSprite = Tree(x, y)
      trees.add(tempSprite)
    elif case('u') or case('d') or case('l') or case('r'):
      tempSprite = Ledge(x, y, tileMap[row][column].lower())
      ledges.add(tempSprite)
    elif case('g'):
      tempSprite = Grass(x, y)
      tall_grass.add(tempSprite)
    else:
      continue
    all_sprites.add(tempSprite)
clock = pygame.time.Clock()
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  clock.tick(40)
  screen.fill((255, 255, 255))
  ground_layer.draw(screen)
  all_sprites.draw(screen)
  me.update()
  pygame.display.flip()