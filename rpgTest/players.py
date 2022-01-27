import pygame
class adventurer(pygame.sprite.Sprite):
  def __init__(self, name, race, health, moves=[None, None, None], nick=None):
    super().__init__()
    self.name = name
    self.nick = name if nick == None else nick
    self.race = race
    self.maxHp = health
    self.hp = health
    self.maxStm = 100
    self.stm = 100
    self.strength = 0
    self.dexterity = 0
    self.constitution = 0
    self.wisdom = 0
    self.intelligence = 0
    self.charisma = 0
    self.coins = 0
    self.keys = []
    self.image = pygame.Surface((16, 16))
    self.image.fill((0, 0, 0))
    self.rect = self.image.get_rect()
    self.rect.topleft = (0, 0)
    self.pos = [0, 0]
    self.velo = [0, 0]
    self.combat = False
    for move in moves:
      setattr(self, move.id, move)
  def show(self):
    print(self.name,'('+self.nick+')')
    print(self.race)
    print('HP:',self.hp,'/',self.maxHp)
    print('Stamina:',self.stm,'/',self.maxStm)
    print(str(type(self))[(str(type(self)).find('.') if not str(type(self)).find('.') == -1 else str(type(self)).find('\''))+1:-2])
  def move(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
      self.velo[1] = -3
    elif key[pygame.K_s]:
      self.velo[1] = 3
    else:
      self.velo[1] = 0
    if key[pygame.K_d]:
      self.velo[0] = 3
    elif key[pygame.K_a]:
      self.velo[0] = -3
    else:
      self.velo[0] = 0
  def ability(self, event):
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP:
        print('up')
      elif event.key == pygame.K_DOWN:
        print('down')
      elif event.key == pygame.K_RIGHT:
        print('right')
      elif event.key == pygame.K_LEFT:
        print('left')
  def frame(self, screen):
    self.move()
    self.pos[0] += self.velo[0] * 0.16
    self.pos[1] += self.velo[1] * 0.16
    if self.pos[0] <= 0:
      self.pos[0] = 0
    elif self.pos[0] >= 240:
      self.pos[0] = 240
    if self.pos[1] <= 0:
      self.pos[1] = 0
    if self.pos[1] >= 112-16:
      self.pos[1] = 112-16
    screen.blit(self.image, self.pos)
    self.rect.topleft = self.pos
  def attack(self, weapon, target):
    print(self.nick,'used',weapon.name,'on',target.name)
    target.hp -= weapon.damage
    self.stm -= weapon.stamina
  def collide(self, group):
    hits = pygame.sprite.spritecollide(self, group, False)
    for hit in hits:
      try:
        hit.open(self)
      except AttributeError:
        pass
class Paladin(adventurer):
  def __init__(self, name, race, health, moves=[None, None, None], nick=None):
    super().__init__(name, race, health, moves, nick)
    self.type = 'Paladin'
class weapon:
  def __init__(self, id, name, type, damage, dType, hBox, stamina):
    self.id = id
    self.name = name
    self.type = type
    self.damage = damage
    self.dType = dType
    self.hurtbox = hBox
    self.stamina = stamina
elvenBlade = weapon('elvenBlade', 'Elven Blade', 'sword', 20, 'Normal', None, 10)
elvenBow = weapon('elvenBow', 'Elven Bow', 'bow', 10, 'Projectile', None, 20)
thievesKnife = weapon('thievesKnife', 'Thieve\'s Knife', 'dagger', 5, 'Normal', None, 3)
bomb = weapon('bomb', 'Bomb', 'explosive', 10, 'Blast', ([-1, -1], [1, 1]), 20)

julian = adventurer('Hawk Feather', 'Tabaxi', 81, [elvenBlade, elvenBow, thievesKnife], 'Hawk')
julian.show()