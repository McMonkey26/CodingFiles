import pygame, time
from constants import *
import inventory
class Cooldown(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.Surface((tileSize*3, tileSize*3))
    self.image.fill((60, 60, 60))
    self.cdU = pygame.Surface((tileSize, tileSize))
    self.cdD = pygame.Surface((tileSize, tileSize))
    self.cdL = pygame.Surface((tileSize, tileSize))
    self.cdR = pygame.Surface((tileSize, tileSize))
    self.cdU.fill((12, 41, 20))
    self.cdD.fill((12, 41, 20))
    self.cdL.fill((12, 41, 20))
    self.cdR.fill((12, 41, 20))
    self.image.blit(self.cdU, (tileSize, 0))
    self.image.blit(self.cdD, (tileSize, tileSize*2))
    self.image.blit(self.cdL, (0, tileSize))
    self.image.blit(self.cdR, (tileSize*2, tileSize))
    self.rect = self.image.get_rect()
  def update(self, adventurer):
    self.cdU = pygame.Surface((int(tileSize*adventurer.moveU.percUntilNextUse()), tileSize))
    self.cdD = pygame.Surface((int(tileSize*adventurer.moveD.percUntilNextUse()), tileSize))
    self.cdL = pygame.Surface((int(tileSize*adventurer.moveL.percUntilNextUse()), tileSize))
    self.cdR = pygame.Surface((int(tileSize*adventurer.moveR.percUntilNextUse()), tileSize))
    self.cdU.fill((12, 41, 20))
    self.cdD.fill((12, 41, 20))
    self.cdL.fill((12, 41, 20))
    self.cdR.fill((12, 41, 20))
    self.image.fill((40, 40, 40))
    self.image.blit(self.cdU, (tileSize, 0))
    self.image.blit(self.cdD, (tileSize, tileSize*2))
    self.image.blit(self.cdL, (0, tileSize))
    self.image.blit(self.cdR, (tileSize*2, tileSize))
testing = Cooldown()
class adventurer(pygame.sprite.Sprite):
  def __init__(self, name, race, health, moves=[None, None, None], nick=None):
    super().__init__()
    self.name = name
    self.nick = name if nick == None else nick
    self.race = race
    self.maxHp = health
    self.hp = health
    self.xp = 0
    self.lvl = 0
    self.xpTillNext = int(100 ** 1+(self.lvl / 5))
    self.maxMana = 100
    self.mana = 100
    self.strength = 0
    self.dexterity = 0
    self.constitution = 0
    self.wisdom = 0
    self.intelligence = 0
    self.charisma = 0
    self.coins = 0
    self.keys = []
    self.image = pygame.Surface((tileSize, tileSize))
    self.image.fill((0, 0, 0))
    self.rect = self.image.get_rect()
    self.rect.topleft = (tileSize, tileSize)
    self.pos = [1, 1]
    self.speed = 1
    self.combat = False
    self.moveL = moves[0]
    self.moveU = moves[1]
    self.moveR = moves[2]
    self.moveD = moves[3]
    self.weaponKeys = {
      pygame.K_LEFT: self.moveL,
      pygame.K_RIGHT: self.moveR,
      pygame.K_UP: self.moveU,
      pygame.K_DOWN: self.moveD
    }
    self.inv = inventory.Inventory(self)
    self.world = [1, 0]
  def show(self):
    print(self.name,'('+self.nick+')')
    print(self.race)
    print('HP:',self.hp,'/',self.maxHp)
    print(str(type(self))[(str(type(self)).find('.') if not str(type(self)).find('.') == -1 else str(type(self)).find('\''))+1:-2])
  def move(self, event, group):
    if (event.type == pygame.KEYDOWN or event.type == pygame.KEYUP) and self.hp > 0:
      if event.key in [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d]:
        self.moveU.turn(event.key)
        self.moveL.turn(event.key)
        self.moveR.turn(event.key)
        self.moveD.turn(event.key)
        if event.mod & pygame.KMOD_SHIFT:
          return None
      moveValues = [0, 0]
      if event.key == pygame.K_a: moveValues[0] = -0.5*self.speed
      if event.key == pygame.K_w: moveValues[1] = -0.5*self.speed
      if event.key == pygame.K_d: moveValues[0] = 0.5*self.speed
      if event.key == pygame.K_s: moveValues[1] = 0.5*self.speed
      self.rect.x += tileSize*moveValues[0]
      self.rect.y += tileSize*moveValues[1]
      self.pos[0] += moveValues[0]
      self.pos[1] += moveValues[1]
      if (hits:=pygame.sprite.spritecollide(self, group, False)):
        self.rect.x -= tileSize*moveValues[0]
        self.rect.y -= tileSize*moveValues[1]
        self.pos[0] -= moveValues[0]
        self.pos[1] -= moveValues[1]
        print([hit.type for hit in hits])
        for hit in hits:
          if hit.type == 'Enemy':
            if hit.alive: self.hp -= hit.damage
          elif hit.type == 'Chest':
            hit.open(self)
          elif hit.type == 'Door':
            hit.open(self)
          elif hit.type == 'Wall':
            pass
      if self.rect.right <= 0 and self.world[0] > 0:
        print('go to left')
        self.world[0] -= 1
        self.rect.x = tileSize*width
        self.pos[0] = width
      elif self.rect.bottom <= 0 and self.world[1] > 0:
        print('go to top')
        self.world[1] -= 1
        self.rect.y = tileSize*height
        self.pos[1] = height
      elif self.rect.x >= tileSize*width and self.world[0] < 2:
        print('go to right')
        self.world[0] += 1
        self.rect.right = 0
        self.pos[0] = -1
      elif self.rect.y >= tileSize*7 and self.world[1] < 1:
        print('go to bottom')
        self.world[1] += 1
        self.rect.bottom = 0
        self.pos[1] = -1
      print((self.rect.x, self.rect.y),'->',(self.rect.right, self.rect.bottom),'World',self.world)
  def ability(self, event, screen, group):
    if event.type == pygame.KEYDOWN and self.hp > 0:
      try:
        self.useWeapon(self.weaponKeys[event.key], group, screen)
      except KeyError:
        pass
  def useWeapon(self, weapon, group, screen):
    if weapon.checkCooldown(): return('Cooldown')
    weapon.use()
    for enemy in group:
      if self.hurtbox(weapon).colliderect(enemy) and enemy.alive:
        enemy.health -= weapon.damage
      enemy.interact(self)
    pygame.draw.rect(screen, (255, 0, 0), self.hurtbox(weapon))
  def hurtbox(self, weapon):
    return offset(scale(weapon.rect, tileSize), self.rect.topleft)
  def update(self, screen, group):
    if self.hp == 0: return None
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]: self.useWeapon(self.weaponKeys[pygame.K_UP], group, screen)
    if key[pygame.K_DOWN]: self.useWeapon(self.weaponKeys[pygame.K_DOWN], group, screen)
    if key[pygame.K_LEFT]: self.useWeapon(self.weaponKeys[pygame.K_LEFT], group, screen)
    if key[pygame.K_RIGHT]: self.useWeapon(self.weaponKeys[pygame.K_RIGHT], group, screen)
    if self.hp <= 0: self.hp = 0
    if self.mana <= 0: self.mana = 0
    if self.xp <= 0: self.xp = 0
    self.inv.update()
class Paladin(adventurer):
  def __init__(self, name, race, health, moves=[None, None, None], nick=None):
    super().__init__(name, race, health, moves, nick)
    self.type = 'Paladin'
class weapon:
  def __init__(self, id, name, type, damage, dType, hBox, stamina):
    self.id = id
    try:
      self.image = pygame.image.load(f'/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/rpgTest/images/{self.id}.png')
      self.image = pygame.transform.scale(self.image, (tileSize, tileSize))
    except FileNotFoundError:
      self.image = pygame.Surface((tileSize, tileSize))
      self.image.fill((60, 60, 60))
    self.name = name
    self.type = type
    self.damage = damage
    self.dType = dType
    self.hurtbox = hBox
    self.rect = pygame.Rect(hBox[0], hBox[1], hBox[2], hBox[3])
    self.defRect = pygame.Rect(hBox[0], hBox[1], hBox[2], hBox[3])
    self.cooldown = stamina / 100
    self.nextUse = time.time()
  def turn(self, direction):
    if direction == pygame.K_w: self.rect = pygame.Rect(self.defRect.y, -self.defRect.x - self.defRect.width + 1, self.defRect.height, self.defRect.width)
    if direction == pygame.K_s: self.rect = pygame.Rect(self.defRect.y, self.defRect.x, self.defRect.height, self.defRect.width)
    if direction == pygame.K_a: self.rect = pygame.Rect(-self.defRect.x - self.defRect.width + 1, self.defRect.y, self.defRect.width, self.defRect.height)
    if direction == pygame.K_d: self.rect = pygame.Rect(self.defRect.x, self.defRect.y, self.defRect.width, self.defRect.height)
  def checkCooldown(self):
    return (time.time() < self.nextUse)
  def use(self):
    self.nextUse = time.time() + self.cooldown
  def percUntilNextUse(self):
    return(1-(((self.nextUse - time.time()) if self.nextUse - time.time() > 0 else 0) / self.cooldown))
def offset(rectangle, amt):
  return pygame.Rect(rectangle.x+amt[0], rectangle.y+amt[1], rectangle.width, rectangle.height)
def scale(rectangle, amt):
  return pygame.Rect(rectangle.x*amt, rectangle.y*amt, rectangle.width*amt, rectangle.height*amt)
elvenBlade = weapon('elvenBlade', 'Elven Blade', 'sword', 10, 'Normal', (1,0,2,1), 20)
thievesKnife = weapon('thievesKnife', 'Thieve\'s Knife', 'dagger', 50, 'Normal', (1,0,1,1), 10)
fight = weapon('fight', 'Fight', 'sword', 15, 'Normal', (1, 0, 2, 1), 25)
elvenBow = weapon('elvenBow', 'Elven Bow', 'bow', 20, 'Projectile', (1,0,5,1), 50)
flight = weapon('flight', 'Flight', 'sword', 15, 'Normal', (1, 0, 2, 1), 25)
bomb = weapon('bomb', 'Bomb', 'explosive', 30, 'Blast', (2,-1,3,3), 70)