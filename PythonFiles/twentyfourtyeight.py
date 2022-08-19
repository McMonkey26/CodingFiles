import pygame, random
pygame.init()
screen = pygame.display.set_mode((630, 630))
screen.fill((255, 255, 255))
#violence
#the role of fascism
font = pygame.font.SysFont('Arial', 64)
class Game:
  mode = 'Start'
  def start():
    Game.mode = 'Playing'
  def lose():
    Game.mode = 'Lost'
  def quit():
    Game.mode = 'Start'
  def playing():
    return Game.mode == 'Playing'
  def inMenu():
    return Game.mode == 'Start'
  def lost():
    return Game.mode == 'Lost'
class Number(pygame.sprite.Sprite):
  def __init__(self, pos, num):
    super().__init__()
    self.image = pygame.Surface((150, 150))
    self.image.fill(((num*5//65536), ((num*5%65536)//256), (num*5%256)))
    self.rect = self.image.get_rect()
    self.rect.topleft = (pos[0]*160, pos[1]*160)
    self.text = font.render(str(num), True, (255, 255, 255))
    self.textRect = self.text.get_rect()
    self.textRect.center = (75, 75)
    self.image.blit(self.text, self.textRect)
    self.pos = pos
    self.num = num
    self.vel = [0, 0]
  def move(self, event, group):
    self.wasHit = False
    hasRun = False
    if event.key == pygame.K_UP:
      self.vel = [0, -1]
    elif event.key == pygame.K_DOWN:
      self.vel = [0, 1]
    elif event.key == pygame.K_LEFT:
      self.vel = [-1, 0]
    elif event.key == pygame.K_RIGHT:
      self.vel = [1, 0]
    if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN] and not (self.vel[0] + self.pos[0] in range(4) and self.vel[1] + self.pos[1] in range(4)):
      self.vel = [0, 0]
      return False
    for i in range(1):
      if not (self.vel[0] + self.pos[0] in range(4) and self.vel[1] + self.pos[1] in range(4)):
        self.vel = [0, 0]
        return True
      self.rect.x += self.vel[0]*160
      self.rect.y += self.vel[1]*160
      self.pos[0] += self.vel[0]
      self.pos[1] += self.vel[1]
      for hit in [x for x in pygame.sprite.spritecollide(self, group, False) if x != self]:
        if hit.num == self.num and not hit.wasHit:
          hit.num *= 2
          hit.image.fill(((hit.num*5//65536), ((hit.num*5%65536)//256), (hit.num*5%256)))
          hit.text = font.render(str(hit.num), True, (255, 255, 255))
          hit.textRect = hit.text.get_rect()
          hit.textRect.center = (75, 75)
          hit.image.blit(hit.text, hit.textRect)
          hit.wasHit = True
          self.kill()
          return True
        else:
          self.rect.x -= self.vel[0]*160
          self.rect.y -= self.vel[1]*160
          self.pos[0] -= self.vel[0]
          self.pos[1] -= self.vel[1]
          self.vel = [0, 0]
          return hasRun
      hasRun = True
    return not self.vel == [0, 0]

numbers = pygame.sprite.Group()
field = [
  ['','','',''],
  ['','','',''],
  ['','',2,''],
  ['','',4,'']
]
for layer in range(len(field)):
  for sprite in range(len(field[layer])):
    if type(field[layer][sprite]) == type('string'): continue
    elif type((tempNum:=field[layer][sprite])) == type(1):
      field[layer][sprite] = Number([sprite,layer],tempNum)
    numbers.add(field[layer][sprite])

run = True
moved = True
clock = pygame.time.Clock()
class placeholder:
  key = 0
  def __init__(self, tempKey):
    self.key = tempKey
x, y = 1, 1
frame = 0
autoRunning = True
while run:
  clock.tick(15)
  frame += 1
  moveDirec = placeholder
  if frame % 5 == 0 and all([x.vel == [0, 0] for x in numbers]) and autoRunning:
    testDirec = random.randint(0, 9)
    if testDirec in [0,1,2]:
      print('up')
      x = 1
      y = 1
      moveDirec = placeholder(pygame.K_UP)
    elif testDirec in [3,4]:
      print('down')
      x = -1
      y = 1
      moveDirec = placeholder(pygame.K_DOWN)
    elif testDirec in [5,6,7]:
      print('left')
      x = 1
      y = 1
      moveDirec = placeholder(pygame.K_LEFT)
    else:
      print('right'+str(testDirec))
      x = 1
      y = -1
      moveDirec = placeholder(pygame.K_RIGHT)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_UP and all([x.vel == [0, 0] for x in numbers]):
        x = 1
        y = 1
        moveDirec = event
      elif event.key == pygame.K_DOWN and all([x.vel == [0, 0] for x in numbers]):
        x = -1
        y = 1
        moveDirec = event
      elif event.key == pygame.K_LEFT and all([x.vel == [0, 0] for x in numbers]):
        x = 1
        y = 1
        moveDirec = event
      elif event.key == pygame.K_RIGHT and all([x.vel == [0, 0] for x in numbers]):
        x = 1
        y = -1
        moveDirec = event
      elif event.key == pygame.K_SPACE:
        autoRunning = False
        print('field =',[[x.num if not type(x) == type('string') else x for x in sprite] for sprite in field])
        print('\n'.join([str([x.vel if not type(x) == type('string') else x for x in sprite]) for sprite in field]))
  for layer in field[::x]:
    for sprite in layer[::y]:
      if type(sprite) == type('string'):
        continue
      if sprite.move(moveDirec, numbers): moved = True
  field = [
    ['','','',''],
    ['','','',''],
    ['','','',''],
    ['','','','']
  ]
  for sprite in numbers:
    field[sprite.pos[1]][sprite.pos[0]] = sprite
  if moved and all([x.vel == [0, 0] for x in numbers]):
    if not any('' in x for x in field): break
    pos0 = random.randrange(0, 4)
    pos1 = random.randrange(0, 4)
    while type(field[pos1][pos0]) != type('string'):
      pos0 = random.randrange(0, 4)
      pos1 = random.randrange(0, 4)
    if random.random() >= 0.9:
      field[pos1][pos0] = Number([pos0, pos1], 4)
    else:
      field[pos1][pos0] = Number([pos0, pos1], 2)
    numbers.add(field[pos1][pos0])
    moved = False
  screen.fill((255, 255, 255))
  numbers.draw(screen)
  pygame.display.flip()