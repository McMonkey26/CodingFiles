import pygame, math, time
from switch import switch, case
class Monkey(pygame.sprite.Sprite):
  def __init__(self, pos=(0, 0), tier=[0, 0, 0], type='', range=0, pierce=0, damage=0, atkCooldown=0, cost=0):
    super().__init__()
    self.image = pygame.Surface((40, 40))
    self.image.fill((80, 255, 120))
    self.rect = self.image.get_rect()
    self.rect.center = pos
    self.ownedUpgrades = tier
    self.topPath = [None for _ in range(5)]
    self.midPath = [None for _ in range(5)]
    self.botPath = [None for _ in range(5)]
    self.type = type
    self.range = range
    self.pierce = pierce
    self.damage = damage
    self.cooldown = atkCooldown
    self.cost = cost
    self.nextThrow = time.time()
    self.camo = False
  def onDetectBloon(self, bloon):
    if self.canSee(bloon):
      try:
        self.throw(bloon)
      except AttributeError:
        raise AttributeError('Monkey has no throw method')
  def canSee(self, bloon):
    return self.camo or not bloon.camo
  def upgrade(self, upgrade):
    upgrade.buy(self)
class DartMonkey(Monkey):
  def __init__(self, pos):
    super().__init__(pos, type='dartMonkey', range=128, pierce=2, damage=1, atkCooldown=0.95, cost=200)
  def throw(self, bloon):
    angle = math.atan((bloon.pos[1]-self.pos[1])/(bloon.pos[0]-self.pos[0]))