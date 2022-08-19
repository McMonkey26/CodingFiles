import pygame, random
pygame.init()
screen = pygame.display.set_mode((600, 600))
curse = ''
class SnakeBox(pygame.sprite.Sprite):
  def __init__(self, pos, color):
    super().__init__()
    self.image = pygame.Surface((30, 30))
    self.image.fill(color)
    self.rect = self.image.get_rect()
    self.rect.topleft = pos
    self.pos = 0
  def update(self):
    global frame
    self.pos += 1
    if self.pos > self.groups()[0].length:
      self.kill()
class Snake(pygame.sprite.Group):
  def __init__(self, pos, vel, color, name):
    super().__init__()
    self.length = 1
    self.pos = pos
    self.velo = vel
    self.color = color
    self.name = name
  def newFrame(self):
    global run
    self.pos[0] += self.velo[0]
    self.pos[1] += self.velo[1]
    self.add(SnakeBox(self.pos, self.color))
    self.update()
    for sprite in self:
      for hit in pygame.sprite.spritecollide(sprite, self, False):
        if not hit == sprite:
          run = False
          print(self.name,f'{curse} died')
          return True
      if sprite.rect.x < 0 or sprite.rect.right > 600 or sprite.rect.y < 0 or sprite.rect.bottom > 600:
        print(self.name,f'{curse} died')
        run = False
        pygame.quit()
        return True
    return False
class Apple(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.Surface((30, 30))
    self.image.fill((255, 0, 0))
    self.rect = self.image.get_rect()
    self.rect.topleft = (random.randrange(0, 570, 30), random.randrange(0, 570, 30))
  def update(self):
    global apples, snake, snake2
    if pygame.sprite.groupcollide(apples, snake, True, False):
      snake.length += 1
      apples.add(Apple())
    # if pygame.sprite.groupcollide(apples, snake2, True, False):
      # snake2.length += 1
      # apples.add(Apple())
apples = pygame.sprite.Group()
apples.add(Apple())
snake = Snake([540, 30], [-30, 0], (200, 200, 200), 'Julian')
# snake2 = Snake([30, 30], [30, 0], (150, 150, 150), 'Josef')
frame = 0
clock = pygame.time.Clock()
run = True
while run:
  clock.tick(40)
  frame += 1
  for event in pygame.event.get():
    if event.type == pygame.QUIT: run = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE: snake.length += 1
      # if event.key == pygame.K_SPACE: snake2.length += 1
      if event.key == pygame.K_LEFT and not snake.velo == [30,0]: snake.velo = [-30,0]
      if event.key == pygame.K_RIGHT and not snake.velo == [-30,0]: snake.velo = [30,0]
      if event.key == pygame.K_UP and not snake.velo == [0,30]: snake.velo = [0,-30]
      if event.key == pygame.K_DOWN and not snake.velo == [0,-30]: snake.velo = [0,30]
      # if event.key == pygame.K_a and not snake2.velo == [30,0]: snake2.velo = [-30,0]
      # if event.key == pygame.K_d and not snake2.velo == [-30,0]: snake2.velo = [30,0]
      # if event.key == pygame.K_w and not snake2.velo == [0,30]: snake2.velo = [0,-30]
      # if event.key == pygame.K_s and not snake2.velo == [0,-30]: snake2.velo = [0,30]
  screen.fill((80, 200, 80))
  if frame%5 == 0:
    if snake.newFrame(): break
    # if snake2.newFrame(): break
  apples.draw(screen)
  apples.update()
  snake.draw(screen)
  # snake2.draw(screen)
  pygame.display.flip()