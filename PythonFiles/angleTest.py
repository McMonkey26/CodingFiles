import pygame, math

pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill((0, 0, 0))

polarCoords = [math.pi, 180]
cartesianCoords = [polarCoords[1]*math.cos(polarCoords[0]), polarCoords[1]*math.sin(polarCoords[0])]
cartesianCoords[0] = 300+cartesianCoords[0]
cartesianCoords[1] = 300-cartesianCoords[1]
def slope(angle, x):
  return(300-(math.tan(angle) * x))
run = True
while run:
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
  pygame.draw.circle(screen, (200, 200, 200), cartesianCoords, 5)
  pygame.display.flip()