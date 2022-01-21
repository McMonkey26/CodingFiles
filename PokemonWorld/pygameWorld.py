import os, random, pygame
from switch import switch, case
os.chdir('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PokemonWorld')
world = []
with open('./worldData.txt', 'r') as file:
  for line in file:
    world.append(line.rstrip('\n'))
tempWorld = list(map(list, world))
[*map(lambda x:print(''.join(x)), tempWorld)]

pygame.init()

screen = pygame.display.set_mode(((width:=640), (height:=640)))

screen.fill([255, 0, 0])

pygame.display.flip()

run = True
class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.Surface((32, 32))
    self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PokemonWorld/images/playerDown.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (32, 32))
    self.rect = self.image.get_rect()
    self.rect.topleft = (400, 320)
    (self.x, self.y) = self.rect.topleft
  def update(self):
    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
      self.x -= 3.2
    if key[pygame.K_w]:
      self.y -= 3.2
    if key[pygame.K_d]:
      self.x += 3.2
    if key[pygame.K_s]:
      self.y += 3.2
    self.rect.topleft = (self.x, self.y)
    screen.blit(self.image, self.rect.topleft)
me = Player()
clock = pygame.time.Clock()
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  clock.tick(40)
  screen.fill((255, 0, 0))
  me.update()
  pygame.display.flip()