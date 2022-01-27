#gets the pygame library
import pygame, sys, random

#initializes the program
pygame.init()

width = 1080
height = 600
#sets up the stage of size width, height
screen = pygame.display.set_mode((width, height))

#changes the color of the stage, this one will be red RGB
screen.fill([0, 0, 0])


class Paddle(pygame.sprite.Sprite): #class to hold the paddles
  def __init__(self, player, x, y): #initializes the class
    super().__init__() #necessary sprite setup line
    self.image = pygame.Surface((20, 100)) #creates a surface for the paddle
    self.image.fill((255, 255, 255)) #fills it with white
    self.rect = self.image.get_rect() #creates a hitbox
    self.rect.topleft = (x, y) #moves the paddle to the inputted position
    self.player = player #adds a variable player to check controls
    self.velo = 0 #adds a variable for velocity
  def update(self, upKey, downKey): #runs every frame
    key = pygame.key.get_pressed() #gets all buttons pressed
    # adds up/down controls \/\/\/
    if key[upKey]:
      self.velo = -2
    elif key[downKey]:
      self.velo = 2
    else:
      self.velo = 0
    # adds down/up controls /\/\/\
    #moves the paddle by its velocity
    self.rect.y += self.velo
    #makes sure the paddle isn't out of bounds
    if self.rect.y < 20:
      self.rect.y = 20
    if self.rect.y > height-self.rect.height-20:
      self.rect.y = height-self.rect.height - 20
    #shows the paddle to the screen
    screen.blit(self.image, self.rect.topleft)

class Ball(pygame.sprite.Sprite): #class to hold the ball(s)
  def __init__(self): #initializes the class
    super().__init__() #necessary sprite setup line
    self.image = pygame.Surface((20, 20)) #creates a surface for the ball
    self.image.fill((255, 255, 255)) #fills it with white
    self.rect = self.image.get_rect() #gives it a hitbox
    self.rect.center = (width/2, height/2) #moves it to the center of the screen
    self.velo = [random.choice([-4, -3, -2, -1, 1, 2, 3, 4]), random.choice([-4, -3, -2, -1, 1, 2, 3, 4])] #gives it a random velocity from [-4, -4] to [4, 4]
  def update(self): #runs every frame
    global p1scoreSprite, p2scoreSprite #global modifier to change score sprites
    self.collision(players) #checks for collision with paddles
    if self.rect.y < 20 or self.rect.y > height-20-self.rect.height: #checks if out of vertical bounds
      self.velo[1] = -self.velo[1] #reverses y velocity
    if self.rect.x <= 0: #checks if out of left bounds
      score[1] += 1 #adds one score to player 2
      p2scoreSprite = scoreFont.render(str(score[1]), 1, (255, 255, 255)) #updates player 2 score sprite
      self.rect.center = (width/2, height/2) #resets the ball to the center
      self.velo = [random.choice([-4, -3, -2, -1, 1, 2, 3, 4]), random.choice([-4, -3, -2, -1, 1, 2, 3, 4])] #gives it a new random velocity [-4,-4] to [4,4]
    if self.rect.x >= width-self.rect.width: #checks if out of right bounds
      score[0] += 1 #adds one score to player 1
      p1scoreSprite = scoreFont.render(str(score[0]), 1, (255, 255, 255)) #updates player 1 score sprite
      self.rect.center = (width/2, height/2) #resets the ball to the center
      self.velo = [random.choice([-4, -3, -2, -1, 1, 2, 3, 4]), random.choice([-4, -3, -2, -1, 1, 2, 3, 4])] #gives it a new random velocity [-4,-4] to [4,4]
    self.rect.x += self.velo[0] #moves it by its x velocity
    self.rect.y += self.velo[1] #moves it by its y velocity
    screen.blit(self.image, self.rect.topleft) #shows it to the screen
  def collision(self, group): #checks for collision
    self.horizontalCollision(group) #checks for horizontal collision
    self.verticalCollision(group) #checks for vertical collison
  def horizontalCollision(self, group): #checks for horizontal collision
    self.rect.x += self.velo[0] #goes towards its x velocity
    if pygame.sprite.spritecollide(self, group, False): #checks if its colliding with a sprite in the group
      self.velo[0] = -self.velo[0] #reverses its x velocity
      self.rect.x += self.velo[0] #brings it back to the position it was in before
    else: #if it isnt colliding with anything
      self.rect.x -= self.velo[0] #brings it back to the position it was in before
  def verticalCollision(self, group): #checks for vertical collision
    self.rect.y += self.velo[1] #goes towards its y velocity
    if pygame.sprite.spritecollide(self, group, False): #checks if its colliding with a sprite in the group
      self.velo[1] = -self.velo[1] #reverses its y velocity
      self.rect.y += self.velo[1] #brings it back to the position it was in before
    else: #if it isnt colliding with anything
      self.rect.y -= self.velo[1] #brings it back to the position it was in before

score = [0, 0] #variable to store scores
scoreFont = pygame.font.SysFont('arial', 20) #variable to store font
p1scoreSprite = scoreFont.render(str(score[0]), 1, (255, 255, 255)) #sprite to show player 1's score
p2scoreSprite = scoreFont.render(str(score[1]), 1, (255, 255, 255)) #sprite to show player 2's score
player1 = Paddle(1, 20, 250) #instance of the paddle class, player 1, 20 away from the left wall
player2 = Paddle(2, 1040, 250) #instance of the paddle class, player 2, 20 away from the right wall
players = pygame.sprite.Group() #creates a group to store paddles
players.add(player1) #adds paddle 1 to the group
players.add(player2) #adds paddle 2 to the group
balls = pygame.sprite.Group() #creates a group to store balls, so more can be added later
balls.add(Ball()) #creates an instance of the ball class and adds it to the group
# for i in range(200): #ignore this
  # balls.add(Ball())
#Shows the screen to the user
pygame.display.flip()

#control variable for main loop
run = True

def gameScreen():
  #clears the screen
  screen.fill((0, 0, 0))
  #shows player 1's score
  screen.blit(p1scoreSprite, (5, 10))
  #shows player 2's score
  screen.blit(p2scoreSprite, (width-5-scoreFont.size(str(score[1]))[0], 10))
  #updates the paddles
  player1.update(pygame.K_w, pygame.K_s)
  player2.update(pygame.K_UP, pygame.K_DOWN)
  #updates the ball(s)
  balls.update()
def winScreen(player):
  global score, p1scoreSprite, p2scoreSprite
  screen.fill((0,0,0)) #clears the screen
  winFont = pygame.font.SysFont('arial', 40) #creates a font for the win text
  winText = f'Player {player} Wins!' #text to show the player
  winSprite = winFont.render(winText, 1, (255, 255, 255)) #makes a sprite to display
  subFont = pygame.font.SysFont('arial', 20) #creates a font for the sub text
  subText = 'Nice Job!' #text to show the player
  subSprite = subFont.render(subText, 1, (255, 255, 255)) #makes a sprite to display
  run = True #win loop variable
  while run: #win loop
    for event in pygame.event.get(): #gets all events
      if event.type == pygame.QUIT: #lets the player press the x button to quit the game
        run = False
        pygame.quit()
      if event.type == pygame.KEYDOWN: #lets the player press space to restart the game
        if event.key == pygame.K_SPACE:
          score = [0, 0] #resets the score
          p1scoreSprite = scoreFont.render(str(score[0]), 1, (255, 255, 255)) #updates player 1 score sprite
          p2scoreSprite = scoreFont.render(str(score[1]), 1, (255, 255, 255)) #updates player 2 score sprite
          run = False #quits the loop
    screen.blit(winSprite, ((width-winFont.size(winText)[0])/2, 270)) #adds the win text to the screen
    screen.blit(subSprite, ((width-subFont.size(subText)[0])/2, 320)) #adds the sub text to the screen
    pygame.display.flip() #updates the screen
#main loop
while run:
  #allows you to press the x in the top corner of pygame window and close it
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  gameScreen() #runs when the game is running
  if score[0] >= 5: # \/ \/ \/
    winScreen(1) # runs when someone wins
  elif score[1] >= 5:
    winScreen(2) # /\ /\ /\
  #updates the screen for the user with anything that happened in the evnets
  pygame.display.flip()