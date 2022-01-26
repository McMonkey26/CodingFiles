import pygame, random

screen = pygame.display.set_mode((1080, 600))
screen.fill((0, 0, 0))

class Pen(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.Surface((5, 5))
    self.image.fill((255, 255, 255))
    self.rect = self.image.get_rect()
    self.rect.center = (540, 300)
    self.velo = [random.randint(1, 20), random.randint(1, 20)]
  def update(self):
    if self.rect.left <= 0 or self.rect.right >= 1080:
      self.velo[0] = -self.velo[0]
    if self.rect.top <= 0 or self.rect.bottom >= 600:
      self.velo[1] = -self.velo[1]
    self.rect.x += self.velo[0]
    self.rect.y += self.velo[1]
    screen.blit(self.image, self.rect.topleft)
pen = Pen()
run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      break
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        screen.fill((0, 0, 0))
        pen = Pen()
      if event.key == pygame.K_v:
        print(pen.velo)
  pen.update()
  pygame.display.flip()