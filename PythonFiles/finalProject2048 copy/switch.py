import pygame
pygame.init()
class switchClass:
  def __init__(self, var):
    self.var = var
  def case(self, testVar):
    if self.var == testVar:
      return True
switch = switchClass(' ')
def switch(var):
  switch.var = var
def case(testVar):
  return testVar == switch.var
def linePrint(*args, **kwargs):
  import os, inspect, builtins
  builtins.print(*['{:20}'.format(lineFile:=f'{os.path.basename(__file__)}:{inspect.currentframe().f_back.f_back.f_lineno}')+str(x).replace('\n', '\n{:20}'.format(lineFile)) for x in args], **kwargs)
class Button(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height, image=None):
    super().__init__()
    self.image = pygame.Surface((width, height))
    if not image == None:
      self.image = pygame.Surface((image[1][2], image[1][3]))
      self.image.blit(pygame.image.load(image[0]), (0, 0), image[1])
      self.image = pygame.transform.scale(self.image, (width, height)).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
  def onEvent(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pygame.mouse.get_pos()): self.onButtonClick()
    if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()): self.onButtonRelease()
  def onButtonClick(self):
    return False
  def onButtonRelease(self):
    return False
class Slider(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height, min=0, max=100, margin=5, thickness=5, value=0, bg=(255, 255, 255), mg=(180, 180, 180), fg=(120, 120, 120), int=False):
    super().__init__()
    self.image = pygame.Surface((width, height))
    self.image.fill(bg)
    self.width = width-(margin*2)
    self.value = value
    self.bounds = [min, max]
    self.bg = bg
    self.mg = mg
    self.fg = fg
    self.thickness = thickness
    self.margin = margin
    self.perc = (self.value-self.bounds[0]) / (self.bounds[1]-self.bounds[0])
    self.int = int
    self.rect = self.image.get_rect(topleft = (x, y))
    self.image.fill(bg)
    pygame.draw.rect(self.image, self.mg, (self.margin, (height-thickness)//2, self.width, self.thickness))
    pygame.draw.circle(self.image, self.fg, (self.width*self.perc+self.margin, self.rect.height / 2), self.thickness)
  def onEvent(self, event):
    if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()): self.onClick()
    if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()): self.onRelease()
  def onClick(self):
    prog = pygame.mouse.get_pos()[0] - (self.rect.x + self.margin)
    self.perc = prog / self.width
    self.perc = 0 if self.perc < 0 else 1 if self.perc > 1 else round(self.perc, 1)
    self.value = (self.perc * (self.bounds[1] - self.bounds[0])) + self.bounds[0]
    if self.int: self.toInt()
    self.image.fill(self.bg)
    pygame.draw.rect(self.image, self.mg, (self.margin, (self.rect.height-self.thickness)//2, self.width, self.thickness))
    pygame.draw.circle(self.image, self.fg, (self.width*self.perc+self.margin, self.rect.height / 2), self.thickness)
  def toInt(self):
    self.value = int(self.value+0.5)
    self.perc = (self.value-self.bounds[0]) / (self.bounds[1]-self.bounds[0])
  def getValue(self):
    return self.value
  def onRelease(self):
    pass
  def update(self):
    pass
class ProgressBar(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height, length=100, margin=10, value=100, bg=(255, 255, 255), fg=(180, 80, 80)):
    super().__init__()
    self.image = pygame.Surface((width, height))
    self.image.fill(bg)
    self.width = width-(margin*2)
    self.height = height-(margin*2)
    self.value = value
    self.length = length
    self.perc = self.value/length
    self.bg = bg
    self.fg = fg
    self.margin = margin
    pygame.draw.rect(self.image, self.fg, (self.margin, self.margin, self.width*self.perc, self.height))
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
  def update(self):
    if self.value < 0: self.value = 0
    if self.value > self.length: self.value = self.length
    self.perc = self.value/self.length
    self.image.fill(self.bg)
    pygame.draw.rect(self.image, self.fg, (self.margin, self.margin, self.width*self.perc, self.height))
class SGroup(pygame.sprite.Group):
  def __init__(self):
    super().__init__()
  def event(self, event):
    for sprite in self:
      sprite.onEvent(event)
libObjects = SGroup()