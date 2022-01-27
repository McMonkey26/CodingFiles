import players, pygame

tileSize = 16
pygame.init()

screen = pygame.display.set_mode((tileSize*15, tileSize*7))
screen.fill((255, 255, 255))

#| # -> wall
#| C -> coin chest
#| c -> key chest
#| D -> unlocked door
#| k -> key door
world = [
  '###############',
  '#  CC  ## c   #',
  '#      ####   #',
  '##     ####   #',
  '       ####    ',
  '       ####    ',
  '#####  ########'
]
class Wall(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((tileSize, tileSize))
    self.image.fill((69, 44, 14))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x*tileSize, y*tileSize)
class CoinChest(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((tileSize, tileSize))
    self.image.fill((125, 62, 31))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x*tileSize, y*tileSize)
    self.coins = 3
  def open(self, player):
    player.coins += self.coins
    self.image.fill((202, 245, 29))
class KeyChest(pygame.sprite.Sprite):
  def __init__(self, x, y, id):
    super().__init__()
    self.image = pygame.Surface((tileSize, tileSize))
    self.image.fill((130, 92, 42))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x*tileSize, y*tileSize)
    self.keyId = id
  def open(self, player):
    player.keys.append(self.keyId)
    self.image.fill((51, 34, 12))
class Slime(pygame.sprite.Sprite):
  def __init__(self, x, y, size):
    super().__init__()
    self.image = pygame.Surface((tileSize*size, tileSize*size))
    self.image.fill((90, 186, 20))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x*tileSize, y*tileSize)
    self.alive = True
  def die(self):
    self.image.fill((66, 42, 5))
    self.alive = False
all_sprites = pygame.sprite.Group()
walls = pygame.sprite.Group()
chests = pygame.sprite.Group()
enemies = pygame.sprite.Group()
for line in range(len(world)):
  for tile in range(len(world[line])):
    if world[line][tile] == '#':
      tempVariable = Wall(tile, line)
      walls.add(tempVariable)
    elif world[line][tile] == 'C':
      tempVariable = CoinChest(tile, line)
      chests.add(tempVariable)
    elif world[line][tile] == 'c':
      tempVariable = KeyChest(tile, line, 'testingtesting123')
      chests.add(tempVariable)
    elif world[line][tile] == 'S':
      tempVariable = Slime(tile, line, 2)
      enemies.add(tempVariable)
    elif world[line][tile] == 's':
      tempVariable = Slime(tile, line, 1)
      enemies.add(tempVariable)
    else:
      continue
    all_sprites.add(tempVariable)

def gameLoop():
  screen.fill((255, 255, 255))
  all_sprites.draw(screen)
  players.julian.frame(screen)
  pygame.display.flip()

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      break
    players.julian.ability(event)
  gameLoop()