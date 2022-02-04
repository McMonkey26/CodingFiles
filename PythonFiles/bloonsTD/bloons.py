import pygame, math
import dartMonkey

pygame.init()
screen = pygame.display.set_mode((1080, 600))
screen.fill((50, 50, 50))

class Bloon(pygame.sprite.Sprite):
  def __init__(self, x, y, level='ghost', *, regrow=False, fort=False, camo=False):
    super().__init__()
    bloonId = level
    if regrow: bloonId += 'Regrow'
    if fort: bloonId += 'Fortified'
    if camo: bloonId += 'Camo'
    self.image = pygame.image.load(f'/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PythonFiles/bloonsTD/images/bloons/{bloonId}.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (self.image.get_width()/4, self.image.get_height()/4))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.bloon = level
    self.regrow = regrow
    self.fort = fort
    self.camo = camo
    self.pos = 0
  def setPos(self, pathMap):
    try:
      self.rect.center = pathMap[self.pos]
    except IndexError:
      player.lives -= 1
thirdBloon = Bloon(200, 50, 'moab')
bloons = pygame.sprite.Group()
bloons.add(thirdBloon)
class Object(object):
  def __init__(self, **kwargs):
    for arg in kwargs:
      setattr(self, arg, kwargs[arg])
player = Object(money=0, lives=0)
monkeys = pygame.sprite.Group()
monkeys.add(dartMonkey.Monkey(player, 300, 400))
mapPath = [
  pygame.Rect(0, 210, 540, 40),
  pygame.Rect(500,  80, 40, 170),
  pygame.Rect(370,  80, 170, 40),
  pygame.Rect(370,  80, 40, 400),
  pygame.Rect(230, 440, 180, 40),
  pygame.Rect(230, 300, 40, 180),
  pygame.Rect(230, 300, 520, 40),
  pygame.Rect(710, 200, 40, 140),
  pygame.Rect(710, 200, 120, 40),
  pygame.Rect(810, 200, 40, 220),
  pygame.Rect(480, 380, 370, 40),
  pygame.Rect(480, 380, 40, 220)
]
mapPoints = []
mapPoints += [(-40+i, 230) for i in range(560)]
mapPoints += [(520, 230-i) for i in range(130)]
mapPoints += [(520-i, 100) for i in range(130)]
mapPoints += [(390, 100+i) for i in range(360)]
mapPoints += [(390-i, 460) for i in range(140)]
mapPoints += [(250, 460-i) for i in range(140)]
mapPoints += [(250+i, 320) for i in range(480)]
mapPoints += [(730, 320-i) for i in range(100)]
mapPoints += [(730+i, 220) for i in range( 80)]
mapPoints += [(830, 220+i) for i in range(180)]
mapPoints += [(830-i, 400) for i in range(330)]
mapPoints += [(500, 400+i) for i in range(240)]
def distance(p1, p2):
  return ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5
def angle(p1, p2):
  return math.acos((p2[0]-p1[0])/distance(p1,p2))

running = True
direction = 0
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_1:
        if event.mod & pygame.KMOD_SHIFT:
          tempCamo = True
        else:
          tempCamo = False
        tempCamo = False
        if event.mod & pygame.KMOD_CTRL:
          tempRegrow = True
        else:
          tempRegrow = False
        if event.mod & pygame.KMOD_ALT:
          tempFort = True
        else:
          tempFort = False
        bloons.add(Bloon(-20, -20, level='red', regrow=tempRegrow, fort=tempFort, camo=tempCamo))
  key = pygame.key.get_pressed()
  if key[pygame.K_RIGHT]:
    for bloon in bloons:
      bloon.pos += 2
      bloon.setPos(mapPoints)
  if key[pygame.K_LEFT]:
    for bloon in bloons:
      bloon.pos -= 2
      bloon.setPos(mapPoints)
  for monkey in monkeys:
    monkey.detectBloons(bloons)
  screen.fill((50, 50, 50))
  for rectangle in mapPath:
    pygame.draw.rect(screen, (200, 200, 200), rectangle)
  monkeys.draw(screen)
  bloons.draw(screen)
  for monkey in monkeys:
    monkey.darts.draw(screen)
    monkey.darts.update()
  pygame.display.flip()