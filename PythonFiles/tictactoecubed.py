import pygame

pygame.init()
screen = pygame.display.set_mode((810, 810))
class Game:
  player = 0
  box = None
ORANGE = (255, 165, 0)
BLUE = (0, 0, 255)
colors = [ORANGE, BLUE]
class Box:
  def __init__(self, pos, tier, master):
    self.master = master
    self.tier = tier
    self.pos = pos[1]*3+pos[0]
    self.image = pygame.Surface((10*(3**tier)-1, 10*(3**tier)-1))
    self.image.fill((255-tier*50,255-tier*50,255-tier*50))
    self.player = None
    self.rect = self.image.get_rect(topleft = (pos[0]*10*(3**tier), pos[1]*10*(3**tier)))
    try:
      self.globalRect = self.image.get_rect(topleft = (pos[0]*10*(3**tier)+self.master.globalRect.x, pos[1]*10*(3**tier)+self.master.globalRect.y))
    except AttributeError:
      self.globalRect = self.image.get_rect(topleft = (pos[0]*10*(3**tier), pos[1]*10*(3**tier)))
    if tier >= 1:
      self.innards = []
      for i in range(9):
        self.innards.append(Box((i%3, i//3), tier-1, self))
        self.image.blit(self.innards[-1].image, self.innards[-1].rect)
  def event(self, event):
    if self.tier >= 1:
      for box in self.innards:
        box.event(event)
      try:
        self.master.image.blit(self.image, self.rect)
      except AttributeError:
        pass
    else:
      if self.rect.collidepoint(pygame.mouse.get_pos()): self.onClick()
  def onClick(self):
    print('hrm')
    if self.tier == 0 and self.player == None and self.master in Game.box:
      self.player = Game.player%2
      self.image.fill(colors[Game.player%2])
      Game.player += 1
      Game.box = [self.master.master.innards[self.pos]]
tempBox = Box((0, 0),4, None)
Game.box = tempBox.innards[0].innards[0].innards
run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: run = False
    tempBox.event(event)
  screen.blit(tempBox.image, tempBox.rect)
  pygame.display.flip()