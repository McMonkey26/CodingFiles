#gets the pygame library
import pygame

#initializes the program
pygame.init()

#sets up the stage of size width, height
screen = pygame.display.set_mode((1080, 600))

#changes the color of the stage, this one will be red RGB
screen.fill([255, 0, 0])

#Shows the screen to the user
pygame.display.flip()

#control variable for main loop
run = True

#main loop
while run:
  #allows you to press the x in the top corner of pygame window and close it
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    #allows for movement with arrow keys
    print(event.type)
  #updates the screen for the user with anything that happened in the evnets
  pygame.display.flip()