import pygame
import dataToJson as dtj

pygame.init()

screen = pygame.display.set_mode((1280, 500))
screen.fill((255, 255, 255))

class Bar(pygame.sprite.Sprite):
  def __init__(self, pokemon):
    super().__init__()
    self.image = pygame.Surface((5, pokemon.usPerc))
    self.image.fill((0, 150, 255) if pokemon.rank % 2 == 0 else (0, 180, 240))
    self.rect = self.image.get_rect()
    self.rect.bottomleft = ((pokemon.rank-1)*5, 500)
    self.poke = pokemon
  def collidePoint(self, pos):
    if pos[0] >= self.rect.left and pos[0] <= self.rect.right and pos[1] >= self.rect.top and pos[1] <= 500:
      return True
bars = pygame.sprite.Group()
for poke in dtj.pokemonObjects[:256]:
  bars.add(Bar(poke))
# testBar = Bar(52.75, 1, dtj.testPoke)
bars.draw(screen)
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if event.type == pygame.MOUSEMOTION:
      for bar in bars:
        if bar.collidePoint(event.pos):
          print(bar.poke.name, bar.poke.rank, bar.poke.usPerc)
  pygame.display.flip()