import pygame, math, time
class Monkey(pygame.sprite.Sprite):
  def __init__(self, master, x, y):
    super().__init__()
    self.master = master
    self.image = pygame.Surface((40, 40))
    self.image.fill((120, 255, 120))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.upgradesOwned = [0, 0, 0]
    self.pops = 0
    self.spent = 0
    self.direction = 90
    self.upgrades = [
      [sharpShots, None, None, None, None],
      [None, None, None, None, None],
      [None, None, None, None, None]
    ]
    self.darts = pygame.sprite.Group()
    self.radius = 150
    self.atkCooldown = 0.950
    self.nextThrow = 0
    self.camo = False
  def upgrade(self, upgradePath):
    if self.upgradesOwned[upgradePath[0]] == upgradePath[1]:
      return None
    tempUpgrade = self.upgrades[upgradePath[0]][upgradePath[1]-1]
    self.master.money -= tempUpgrade.cost
    self.spent += tempUpgrade.cost
    self.upgradesOwned[tempUpgrade.path] = tempUpgrade.level
  def throw(self, direction):
    if (currentTime:=time.time()) >= self.nextThrow:
      self.nextThrow = currentTime+self.atkCooldown
      self.direction = direction
      self.darts.add(Dart(self, 5, 1, 1))
  def detectBloons(self, group):
    tempList = [bloon for bloon in group if (pygame.sprite.collide_circle(bloon, self) and (self.camo or not bloon.camo))]
    try:
      close = min(tempList, key=lambda x:distance(x.rect.center, self.rect.center))
      far = max(tempList, key=lambda x:distance(x.rect.center, self.rect.center))
      first = max(tempList, key=lambda x:x.pos)
      last = min(tempList, key=lambda x:x.pos)
    except ValueError:
      return None
    for bloon in [close, far, first, last]:
      self.direction = angle(self.rect.center, bloon.rect.center)
      self.darts.add(Dart(self, 5, 1, 1))
    for bloon in group:
      if pygame.sprite.collide_circle(bloon, self) and (self.camo or not bloon.camo):
        return None
        self.throw(angle(self.rect.center, bloon.rect.center))
class Dart(pygame.sprite.Sprite):
  def __init__(self, master, speed, pierce, damage):
    super().__init__()
    self.image = pygame.Surface((20, 40))
    self.image.fill((200, 200, 200))
    self.rect = self.image.get_rect()
    self.rect.center = master.rect.center
    self.master = master
    self.direction = self.master.direction
    self.speed = speed
    self.pierce = pierce
    self.damage = damage
  def update(self):
    self.rect.x += math.cos(self.direction) * self.speed
    self.rect.y -= math.sin(self.direction) * self.speed
    if self.rect.right <= 0 or self.rect.x >= 1080 or self.rect.bottom <= 0 or self.rect.y >= 600:
      self.kill()
class Upgrade:
  def __init__(self, name, cost, path, level):
    self.cost = cost
    self.path = path
    self.level = level
    self.name = name
    self.description = 'Placeholder value'
    self.effect = 'Placeholder value'
sharpShots = Upgrade('Sharp Shots', 140, 0, 1)
def distance(p1, p2):
  return ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5
def angle(p1, p2):
  return math.acos((p2[0]-p1[0])/distance(p1,p2)) if p2[1] - p1[1] <= 0 else -math.acos((p2[0]-p1[0])/distance(p1,p2))