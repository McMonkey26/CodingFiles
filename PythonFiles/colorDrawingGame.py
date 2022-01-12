#gets the pygame library
import pygame, random

#initializes the program
pygame.init()

#sets up the stage of size width, height
screen = pygame.display.set_mode((1080, 600))

#changes the color of the stage, this one will be red RGB
screen.fill([0, 0, 0])

#Shows the screen to the user
pygame.display.flip()

#control variable for main loop
run = True
pos = (540, 300)
rad = 50
color = [255, 255, 255]
shape = 0
#main loop
while run:
  pos = pygame.mouse.get_pos()
  key = pygame.key.get_pressed()
  if key[pygame.K_UP]:
    rad += 1
    print('up')
  if key[pygame.K_DOWN]:
    rad -= 1
  #allows you to press the x in the top corner of pygame window and close it
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      shape += 1
    try:
      if event.key == pygame.K_ESCAPE:
        screen.fill([0, 0, 0])
      if event.key == pygame.K_SPACE:
        color[0] = random.randint(0, 255)
        color[1] = random.randint(0, 255)
        color[2] = random.randint(0, 255)
      if event.key == pygame.K_b:
        color = [0, 0, 0]
    except AttributeError:
      pass
    #allows for movement with arrow keys
    if shape%2 == 0:
      pygame.draw.circle(screen, color, pos, rad)
    elif shape%2 == 1:
      pygame.draw.rect(screen, color, (pos[0]-rad, pos[1]-rad, 2*rad, 2*rad))
  #updates the screen for the user with anything that happened in the evnets
  pygame.display.flip()