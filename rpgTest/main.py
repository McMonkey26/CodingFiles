import players, pygame
from constants import *
pygame.init()

screen = pygame.display.set_mode((tileSize*15, tileSize*10))
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
  '   S   ####    ',
  '       ####    ',
  '#####  ########'
]
world00 = [
  '###############',
  '###############',
  '####   ########',
  '####   ########',
  '####           ',
  '####           ',
  '###############'
]
world10 = [
  '###############',
  '#  CC  ## c   #',
  '#      ####   #',
  '##     ####   #',
  '   S   ####    ',
  '       ####    ',
  '#####  ########'
]
world20 = [
  '###############',
  '###############',
  '#####   #######',
  '####    #######',
  '       ########',
  '      #########',
  '###############'
]
world01 = [
  '###############',
  '###############',
  '###############',
  '###############',
  '###############',
  '###############',
  '###############'
]
world11 = [
  '#####  ########',
  '#####  ########',
  '#####    ######',
  '#####    ######',
  '###############',
  '###############',
  '###############'
]
world21 = [
  '###############',
  '###############',
  '###############',
  '###############',
  '###############',
  '###############',
  '###############'
]
worldMaps = [
  [world00, world10, world20],
  [world01, world11, world21]
]
spriteMaps = [
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()],
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()]
]
wallMaps = [
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()],
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()]
]
chestMaps = [
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()],
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()]
]
enemyMaps = [
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()],
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()]
]
class Wall(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((tileSize, tileSize))
    self.image.fill((69, 44, 14))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x*tileSize, y*tileSize)
    self.type = 'Wall'
class CoinChest(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((tileSize, tileSize))
    self.image.fill((125, 62, 31))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x*tileSize, y*tileSize)
    self.type = 'Chest'
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
    self.type = 'Chest'
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
    self.type = 'Enemy'
    self.damage = 4*size
    self.health = 50*size
    self.size = size
    self.alive = True
  def interact(self, player):
    if self.health <= 0:
      self.die(player)
  def die(self, player):
    self.image.fill((66, 42, 5))
    self.alive = False
    player.xp += 10*self.size
class Dummy(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.Surface((tileSize*3, tileSize*3))
    self.image.fill((180, 180, 180))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x*tileSize, y*tileSize)
    self.health = 100
    self.text = pygame.font.SysFont('arial', int(1.25*tileSize)).render(str(self.health), True, (255, 255, 255))
    self.textRect = self.text.get_rect(center=(1.5*tileSize, 1.5*tileSize))
    self.image.blit(self.text, self.textRect)
    self.type = 'NPC'
    self.damage = 0
    self.alive = True
  def interact(self, player):
    if self.health <= 0: self.health = 100
    self.image.fill((180, 180, 180))
    self.text = pygame.font.SysFont('arial', int(1.25*tileSize)).render(str(self.health), True, (255, 255, 255))
    self.textRect = self.text.get_rect(center=(1.5*tileSize, 1.5*tileSize))
    self.image.blit(self.text, self.textRect)
for x in range(len(worldMaps)):
  for y in range(len(worldMaps[x])):
    for line in range(len(worldMaps[x][y])):
      for tile in range(len(worldMaps[x][y][line])):
        if worldMaps[x][y][line][tile] == '#':
          tempVariable = Wall(tile, line)
          wallMaps[x][y].add(tempVariable)
        elif worldMaps[x][y][line][tile] == 'C':
          tempVariable = CoinChest(tile, line)
          chestMaps[x][y].add(tempVariable)
        elif worldMaps[x][y][line][tile] == 'c':
          tempVariable = KeyChest(tile, line, 'testingtesting123')
          chestMaps[x][y].add(tempVariable)
        elif worldMaps[x][y][line][tile] == 'S':
          tempVariable = Slime(tile, line, 2)
          enemyMaps[x][y].add(tempVariable)
        elif worldMaps[x][y][line][tile] == 's':
          tempVariable = Slime(tile, line, 1)
          enemyMaps[x][y].add(tempVariable)
        else:
          continue
        spriteMaps[x][y].add(tempVariable)
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
tempVariable = Dummy(0, 7)
all_sprites.add(tempVariable)
enemies.add(tempVariable)
julian = players.adventurer('Hawk Feather', 'Tabaxi', 81, [players.fight, players.elvenBow, players.flight, players.bomb], 'Hawk')
def gameLoop():
  # screen.fill((128, 128, 128))
  all_sprites.draw(screen)
  screen.blit(julian.image, julian.rect.topleft)
  screen.blit(julian.inv.image, (0, tileSize*7))
  players.testing.update(julian)
  screen.blit(players.testing.image, (tileSize*12, tileSize*7))
  pygame.display.flip()
def worldLoop(world):
  spriteMaps[world[1]][world[0]].draw(screen)
  screen.blit(julian.image, julian.rect.topleft)
  screen.blit(julian.inv.image, (0, tileSize*7))
  players.testing.update(julian)
  screen.blit(players.testing.image, (tileSize*12, tileSize*7))
  pygame.display.flip()
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      break
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        julian.show()
    screen.fill((128, 128, 128))
    julian.move(event, spriteMaps[julian.world[1]][julian.world[0]])
    julian.ability(event, screen, enemyMaps[julian.world[1]][julian.world[0]])
  julian.update(screen, enemyMaps[julian.world[1]][julian.world[0]])
  worldLoop(julian.world)