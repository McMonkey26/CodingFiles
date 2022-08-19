import pygame, math

pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill((0, 0, 0))
def slope(angle, x):
  return(300-(math.tan(angle) * x))
def polarToCartesian(coords):
  return [300+coords[1]*math.cos(coords[0]), 300-coords[1]*math.sin(coords[0])]
run = True
def circleAnim(dist):
  num = 0
  while True:
    yield polarToCartesian([(num%628)/100, dist])
    num += 1
clock = pygame.time.Clock()
anim180 = circleAnim(180)
def circleAndLines(point):
  pygame.draw.circle(screen, (200, 200, 200), point, 5)
  pygame.draw.line(screen, (255, 0, 0), (300, point[1]), point)
  pygame.draw.line(screen, (0, 255, 0), (point[0], 300), point)
  pygame.draw.line(screen, (0, 0, 255), (300, 300), point)
while run:
  clock.tick(120)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  screen.fill((0, 0, 0))
  for i in range(10, 0, -1):
    pygame.draw.circle(screen, (100, 100, 100), (300, 300), i*60)
    pygame.draw.circle(screen, (0, 0, 0), (300, 300), i*60-1)
  for i in range(10):
    pygame.draw.rect(screen, (100, 100, 100), (0, i*60, 600, 1))
    pygame.draw.rect(screen, (100, 100, 100), (i*60, 0, 1, 600))
  circleAndLines(next(anim180))
  pygame.display.flip()