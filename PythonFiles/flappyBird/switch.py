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
  def onButtonClick(self):
    return False
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