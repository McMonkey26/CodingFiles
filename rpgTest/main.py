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
  '   S   ####    ',
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
    self.damage = 4
    self.health = 100
    self.alive = True
  def interact(self):
    if self.health <= 0:
      self.die()
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
  global tempStm
  # screen.fill((255, 255, 255))
  all_sprites.draw(screen)
  screen.blit(players.julian.image, players.julian.rect.topleft)
  players.julian.stm += players.julian.maxStm/2000
  if players.julian.stm >= players.julian.maxStm: players.julian.stm = players.julian.maxStm
  if not int(players.julian.stm) == tempStm:
    print(int(players.julian.stm))
    tempStm = int(players.julian.stm)
  pygame.display.flip()
tempStm = 100
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      break
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        players.julian.show()
    screen.fill((255, 255, 255))
    players.julian.move(event, all_sprites)
    players.julian.ability(event, screen, enemies)
  gameLoop()