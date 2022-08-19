import pygame
pygame.init()
screen = pygame.display.set_mode((320, 320))
screen.fill((255, 255, 255))

class Slider(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height, min=0, max=100, margin=5, thickness=10, value=0, bg=(255, 255, 255), mg=(180, 180, 180), fg=(120, 120, 120)):
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
    self.perc = self.value / (self.bounds[1]-self.bounds[0])
    self.rect = self.image.get_rect(topleft = (x, y))
    self.image.fill(bg)
    pygame.draw.rect(self.image, self.mg, (self.margin, (height-thickness)//2, self.width, self.thickness))
    pygame.draw.circle(self.image, self.fg, (self.width*self.perc+self.margin, self.rect.centery), self.thickness)
  def onEvent(self, event):
    if pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos()): self.onClick()
    if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pygame.mouse.get_pos()): self.onClick()
    if event.type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(pygame.mouse.get_pos()): self.onRelease()
  def onClick(self):
    prog = pygame.mouse.get_pos()[0] - (self.rect.x + self.margin)
    self.perc = prog / self.width
    self.perc = 0 if self.perc < 0 else 1 if self.perc > 1 else self.perc
    self.value = (self.perc * (self.bounds[1] - self.bounds[0])) + self.bounds[0]
  def onRelease(self):
    pass
  def update(self):
    self.image.fill(self.bg)
    pygame.draw.rect(self.image, self.mg, (self.margin, (self.rect.height-self.thickness)//2, self.width, self.thickness))
    pygame.draw.circle(self.image, self.fg, (self.width*self.perc+self.margin, self.rect.height / 2), self.thickness)
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
sld = Slider(40, 40, 240, 30)
slidGrp = pygame.sprite.Group()
slidGrp.add(Slider(40, 80, 240, 30, min=100, max=1000, bg=(255, 0, 0), mg=(255, 255, 255), fg=(0, 0, 0), thickness = 5, margin = 20))
run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        print(sld.value)
    sld.onEvent(event)
    [slid.onEvent(event) for slid in slidGrp]
  screen.fill((255, 200, 150))
  slidGrp.draw(screen)
  slidGrp.update()
  screen.blit(sld.image, sld.rect)
  sld.update()
  pygame.display.flip()