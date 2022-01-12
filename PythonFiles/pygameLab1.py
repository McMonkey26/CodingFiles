#gets the pygame library
import pygame, os
os.chdir('/Users/jpollack/Desktop/CodingFiles/PythonFiles')

#initializes the program
pygame.init()

#sets up the stage of size width, height
screen = pygame.display.set_mode((1080, 600))

#changes the color of the stage, this one will be red RGB
screen.fill([255, 0, 0])

#Shows the screen to the user
pygame.display.flip()

#load an image
circleImage = pygame.image.load('/Users/jpollack/Desktop/CodingFiles/PokemonWorld/images/tree.png').convert_alpha()
circleImage = pygame.transform.scale(circleImage, (300, 300))

p1 = pygame.Rect(100, 100, 100, 100)
p2 = pygame.Rect(880, 100, 100, 100)
rectangle = pygame.Rect(100, 100, 100, 100)
circle = ((800, 100), 50)
polygon = ((400, 100), (500, 200), (400, 300), (300, 200))
#control variable for main loop
run = True
x, y = (540, 300)
speed = 1
#main loop
while run:
  key = pygame.key.get_pressed()
  if key[pygame.K_LEFT]:
    if x >= speed:
      x -= speed
    else:
      x = 0
  if key[pygame.K_RIGHT]:
    if x <= 780-speed:
      x += speed
    else:
      x = 780
  if key[pygame.K_DOWN]:
    if y <= 300-speed:
      y += speed
    else:
      y = 300
  if key[pygame.K_UP]:
    if y >= speed:
      y -= speed
    else:
      y = 0
  #allows you to press the x in the top corner of pygame window and close it
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.K_ESCAPE:
      x = 1080
    #allows for movement with arrow keys
  screen.fill([255, 0, 0])
  # pygame.draw.rect(screen, (0, 255, 0), rectangle)
  # pygame.draw.circle(screen, (0, 0, 255), circle[0], circle[1])
  # pygame.draw.polygon(screen, (0, 125, 125), polygon)
  # pygame.draw.rect(screen, (0, 255, 0), p1)
  # pygame.draw.rect(screen, (0, 0, 255), p2)
  screen.blit(circleImage, (x, y))
  #updates the screen for the user with anything that happened in the evnets
  pygame.display.flip()