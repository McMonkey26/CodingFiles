import players, pygame, random
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
  '#####  ########']
world00 = [
  '###############',
  '###############',
  '####   ########',
  '####   ########',
  '####           ',
  '####           ',
  '###############']
world10 = [
  '###############',
  '#  CC     c   #',
  '#      ####z  #',
  '##     ####   #',
  '^  S   ####    ',
  'v      ####    ',
  '#####{}########']
world20 = [
  '###############',
  '###############',
  '#####sss#######',
  '####ssss#######',
  '     ss########',
  '      #########',
  '####  #########']
world01 = [
  '###############',
  '###############',
  '###############',
  '###############',
  '###############',
  '###############',
  '###############']
world11 = [
  '#####  ########',
  '#####  ########',
  '#####          ',
  '#####          ',
  '###############',
  '###############',
  '###############']
world21 = [
  '####  #########',
  '####  #########',
  '      #########',
  '      #########',
  '###############',
  '###############',
  '###############']
worldMaps = [
  [world00, world10, world20],
  [world01, world11, world21]]
spriteMaps = [
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()],
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()]]
wallMaps = [
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()],
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()]]
chestMaps = [
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()],
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()]]
enemyMaps = [
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()],
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()]]
doorMaps = [
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()],
  [pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()]]
class Wall(pygame.sprite.Sprite):
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.image.load("/Users/jpollack/Desktop/CodingFiles/CodingFiles/rpgTest/images/walls.png")
    # self.image.fill((69, 44, 14))
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
class WeaponChest(pygame.sprite.Sprite):
  def __init__(self, x, y, id):
    super().__init__()
    self.image = pygame.Surface((tileSize, tileSize))
    self.image.fill((66, 66, 66))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x*tileSize, y*tileSize)
    self.type = 'Chest'
    self.weapon = players.crescentRose
    def open(self, player):
      pass
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
class KeyDoor(pygame.sprite.Sprite):
  def __init__(self, x, y, orient, id):
    super().__init__()
    self.image = pygame.Surface(((tileSize*2) if orient == 'h' else tileSize, tileSize if orient == 'h' else (tileSize*2)))
    self.image.fill((84, 55, 21))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x*tileSize, y*tileSize)
    self.type = 'Door'
    self.keyId = id
  def open(self, player):
    if self.keyId in player.keys: self.kill()
class EnemyDoor(pygame.sprite.Sprite):
  def __init__(self, x, y, orient):
    super().__init__()
    self.image = pygame.Surface(((tileSize*2) if orient == 'h' else tileSize, tileSize if orient == 'h' else (tileSize*2)))
    self.image.fill((64, 48, 29))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x*tileSize, y*tileSize)
    self.type = 'Door'
  def open(self, player):
    if len([True for enemy in enemyMaps[player.world[1]][player.world[0]] if enemy.alive])==0:self.kill()
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
    if self.health <= 0 and self.alive:
      self.die(player)
  def die(self, player):
    self.image.fill((66, 42, 5))
    self.alive = False
    player.xp += 10*self.size
class Zombie(pygame.sprite.Sprite):
  def __init__(self, x, y, size):
    super().__init__()
    self.image = pygame.Surface((tileSize*size, tileSize*size))
    self.image.fill((89, 145, 16))
    self.bgImage = pygame.Surface((tileSize*size, tileSize*size))
    self.bgImage.fill((128, 128, 128))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x*tileSize, y*tileSize)
    self.type = 'Enemy'
    self.damage = 8*size
    self.health = 100*size
    self.size = size
    self.speed = size
    self.alive = True
    self.movePath = {
      (832, 128): [-32*self.speed,0],
      (704, 128): [0, 32*self.speed],
      (704, 320): [32*self.speed,0],
      (832, 320): [0,-32*self.speed]}
    self.lastDirec = self.movePath[self.rect.topleft]
  def interact(self, player):
    if self.health <= 0 and self.alive:
      self.die(player)
  def die(self, player):
    self.image.fill((20, 20, 20))
    self.alive = False
    player.xp += 30*self.size
  def update(self, group):
    if frame%10 == 0 and self.alive:
      screen.blit(self.bgImage, self.rect)
      if self.rect.topleft in self.movePath.keys():
        self.lastDirec = self.movePath[self.rect.topleft]
      self.rect.x += self.lastDirec[0]
      self.rect.y += self.lastDirec[1]
      if ((hits:=pygame.sprite.spritecollide(self, group, False)) and len(hits) > 1) or self.rect.x < 0 or self.rect.y < 0 or self.rect.right > tileSize*15 or self.rect.bottom > tileSize*7 or pygame.sprite.collide_rect(self, julian):
        if pygame.sprite.collide_rect(self, julian): julian.hp -= self.damage
        self.rect.x -= self.lastDirec[0]
        self.rect.y -= self.lastDirec[1]
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
        elif worldMaps[x][y][line][tile] == '{':
          tempVariable = KeyDoor(tile, line, 'h', 'testingtesting123')
          doorMaps[x][y].add(tempVariable)
        elif worldMaps[x][y][line][tile] == '[':
          tempVariable = KeyDoor(tile, line, 'v', 'testingtesting123')
          doorMaps[x][y].add(tempVariable)
        elif worldMaps[x][y][line][tile] == '<':
          tempVariable = EnemyDoor(tile, line, 'h')
          doorMaps[x][y].add(tempVariable)
        elif worldMaps[x][y][line][tile] == '^':
          tempVariable = EnemyDoor(tile, line, 'v')
          doorMaps[x][y].add(tempVariable)
        elif worldMaps[x][y][line][tile] == 'Z':
          tempVariable = Zombie(tile, line, 2)
          enemyMaps[x][y].add(tempVariable)
        elif worldMaps[x][y][line][tile] == 'z':
          tempVariable = Zombie(tile, line, 1)
          enemyMaps[x][y].add(tempVariable)
        else:
          continue
        spriteMaps[x][y].add(tempVariable)
julian = players.adventurer('Hawk Feather', 'Tabaxi', 81, [players.crescentRose, players.elvenBow, players.flight, players.bomb], 'Hawk')
def gameLoop():
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
clock = pygame.time.Clock()
frame = 0
running = True
while running:
  clock.tick(60)
  frame += 1
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
  for sprite in enemyMaps[julian.world[1]][julian.world[0]]:
    try:
      sprite.update(spriteMaps[julian.world[1]][julian.world[0]])
    except AttributeError:
      pass
  worldLoop(julian.world)