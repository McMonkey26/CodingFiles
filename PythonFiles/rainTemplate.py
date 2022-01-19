#get library for pygame
import pygame
import random
pygame.init()

# Creates a window with variables to store width and height
width = 1080
height = 600
screen = pygame.display.set_mode((width,height))
screen.fill([0,0,0])

class Rain(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self) #Necessary pygame setup line
    self.image = pygame.Surface((50, 50)) #Creates a surface to store the image
    self.image = pygame.image.load('/Users/jpollack/Downloads/raindrop.png').convert_alpha() #Loads an image on that surface
    self.image = pygame.transform.scale(self.image, (50, 50)) #Transforms that image to a specific size
    self.rect = self.image.get_rect() #Creates a hitbox for the image
    self.rect.topleft = (x, y) #Sets the position of the image to the parameters
    self.speed = random.randint(1, 3) #Sets the speed to a random number for some variety
  def update(self): #Runs every frame
    self.rect.y += self.speed #Moves the image down by it's speed
    if self.rect.bottom > height:
      self.rect.top = 0 #Moves the image back to the top if it goes off screen


class Umbrella(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self) #Necessary pygame setup line
    self.image = pygame.Surface((200, 200)) #Creates a surface to store the image
    self.image = pygame.image.load('/Users/jpollack/Downloads/umb.png').convert_alpha() #Loads an image on that surface
    self.image = pygame.transform.scale(self.image, (200, 200)) #Transforms that image to a specific size
    self.rect = self.image.get_rect() #Creates a hitbox for the image
    self.rect.topleft = (x, y) #Sets the position of the image to the parameters
    self.velocity = 0 #Sets the speed to 0, so it can be modified later
  def update(self): #Runs every frame
    self.rect.x += self.velocity #Moves the image right by it's speed (left if it's negative)
    if self.rect.right > width: #\/
      self.rect.right = width #Makes sure the image can't go off the right side of the screen
    if self.rect.left < 0: #\/
      self.rect.left = 0 #Makes sure the image can't go off the left side of the screen

raindrops = pygame.sprite.Group() #Makes a group to store the raindrops
for i in range(100): #Iterates 100 times:
  drop = Rain(random.randint(0, width), random.randint(0, height)) #Creates a Rain object at a random width and height
  raindrops.add(drop) #Adds that object to the group


umbrella = Umbrella(540, 300) #Generates an Umbrella object in the middle of the screen


pygame.display.flip() #Displays the screen

#Main Loop
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: #Lets you quit the program by clicking the x button
      running = False
    if event.type == pygame.KEYDOWN: #On key press
      if event.key == pygame.K_LEFT: #On Left key press
        umbrella.velocity -= 2 #Increase velocity by 2 to the left
      if event.key == pygame.K_RIGHT: #On right key press
        umbrella.velocity += 2 #Increase velocity by 2 to the right
    if event.type == pygame.KEYUP: #On key release
      if event.key == pygame.K_LEFT: #On left key release
        umbrella.velocity += 2 #Decrease velocity by 2 to the left
      if event.key == pygame.K_RIGHT: #On right key release
        umbrella.velocity -= 2 #Decrease velocity by 2 to the right
  
  getHits = pygame.sprite.spritecollide(umbrella, raindrops, False) #gets an iterable of everything in the raindrops group thats colliding with the umbrella
  for hit in getHits: #iterates through the collisions
    hit.rect.y = 0 #brings all collided rain drops back to the top
  screen.fill([0,0,0]) #Fills the screen
  raindrops.draw(screen) #Adds all raindrops to screen
  screen.blit(umbrella.image, umbrella.rect.topleft) #Adds umbrella to screen
  raindrops.update() #Updates all raindrops
  umbrella.update() #Updates umbrella

  pygame.display.flip() #Displays updates screen
