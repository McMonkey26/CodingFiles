import math, pygame

class Car(pygame.sprite.Sprite):
  def __init__(self, x, y):
    self.image = pygame.Surface((100, 50))
    self.image = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PythonFiles/carGame/carImage.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (100, 50))
    self.rotImage = self.image
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.pos = [x, y]
    self.velo = 1
    self.angle = 0
  def turn(self, angle):
    self.angle += angle
    center = rot_center(self.image, self.angle, self.rect.x, self.rect.y)
    self.rotImage = center[0]
    self.rotRect = center[1]
    print(self.rect.center)
    print(self.rotRect.center)
  def move(self):
    self.pos[0] += self.velo * math.cos(math.radians(self.angle))
    self.pos[1] -= self.velo * math.sin(math.radians(self.angle))
    self.rect.topleft = self.pos
print(math.cos(math.radians(90)))
def rot_center(image, angle, x, y):
  rotated_image = pygame.transform.rotate(image, angle)
  new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)
  return rotated_image, new_rect
pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((0, 0, 0))

car = Car(100, 300)

run = True
while run:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  key = pygame.key.get_pressed()
  if key[pygame.K_d]:
    car.turn(-1)
  elif key[pygame.K_a]:
    car.turn(1)
  if key[pygame.K_w]:
    car.move()
  screen.fill((0, 0, 0))
  screen.blit(car.rotImage, car.rect.topleft)
  pygame.display.flip()