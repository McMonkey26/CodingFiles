import pygame, random, os #imports libraries 
from switch import * #imports switch case functions and an overarching button class
os.chdir('/Users/jpollack/Desktop/CodingFiles/CodingFiles/PythonFiles/flappyBird') #comment this out if you're not using my computer, just sets the directory to the folder this is in
pygame.init() #initializes pygame
screen = pygame.display.set_mode((1080, 600)) #create screen
class Game: #class to store various variables
  score = 0.0 #stores the player's score
  level = 0 #stores what level the player is on
  best = score #stores the player's best score this run
  section = 'Start' #stores what section the player is on
  posSections = ['Menu', 'Start', 'Game', 'Pause', 'Win', 'Lose'] #holds all possible sections, technically unnecessary but it makes it easier to know exactly what string I used for each section
  def inMenu(): #checks if the game is on the level select screen
    return Game.section == 'Menu'
  def starting(): #checks if the game is on the start screen
    return Game.section == 'Start'
  def playing(): #checks if the game is in the middle of a level
    return Game.section == 'Game'
  def paused(): #checks if the game is in the pause screen
    return Game.section == 'Pause'
  def won(): #checks if the game is on the win screen
    return Game.section == 'Win'
  def lost(): #checks if the player is on the loss screen
    return Game.section == 'Lose'
class Background(pygame.sprite.Sprite): #sprite class to display the background
  def __init__(self, x, speed): #runs on instance creation
    super().__init__() #initializes sprite class
    self.image = pygame.Surface((144, 256)) #creates blank surface
    self.image.blit(pygame.image.load('./backgrounds.png'), (0, 0), ((Game.level*146) if Game.level >= 0 else 0, 0, 144, 256)) #blits the surface with background depending on the level
    self.image = pygame.transform.scale(self.image, (400, 600)) #scales the image to 400x600
    self.rect = self.image.get_rect() #gives the sprite a rectangle
    self.rect.topleft = (x, 0) #puts the sprite at the top of the screen with a variable x position
    self.speed = speed #stores sprite speed
  def update(self): #update function runs every frame
    if Game.playing(): #checks if the game is in a level
      self.rect.x -= self.speed #moves the sprite to the left
    if self.rect.right <= 8: #checks if the right side of the sprite is almost off the screen
      self.rect.x = 1176 #moves the sprite to the other side of the screen
class Bird(pygame.sprite.Sprite): #sprite class to display the bird
  def __init__(self, x, y): #runs on instance creation
    super().__init__() #initializes sprite class
    self.image = pygame.Surface((17, 12)) #creates blank surface
    self.image.blit(pygame.image.load('./birds.png'), (0, 0), (0, 0, 17, 12)) #blits the surface with a default bird
    self.image = pygame.transform.scale(self.image, (40, 30)).convert_alpha() #scales the image to 40x30 with a transparent background
    self.rect = self.image.get_rect() #gives the sprite a rectangle
    self.rect.topleft = (x, y) #puts the sprite at coords (x, y)
    self.velo = -7.0 #stores bird y velocity, x velocity is always 0
    self.lastVelo = 0 #stores the bird's last velocity, used for pausing
    self.color = 0 #stores the color of the bird
  def getImage(self): #function to change the bird's image depending on color/velocity
    self.image = pygame.Surface((17, 12)) #makes the sprite's image blank
    if self.velo <= -0.6: #checks if the bird is moving up
      self.image.blit(pygame.image.load('./birds.png'), (0, 0), (self.color*21, 28, 17, 12)) #gives the bird an upward flying image
    elif self.velo >= 0.6: #checks if the bird is moving down
      self.image.blit(pygame.image.load('./birds.png'), (0, 0), (self.color*21, 0, 17, 12)) #gives the bird a downward flying image
    else: #if the bird is relatively static
      self.image.blit(pygame.image.load('./birds.png'), (0, 0), (self.color*21, 14, 17, 12)) #makes the bird look like it's halfway through a flap
    self.image = pygame.transform.scale(self.image, (40, 30)).convert_alpha() #scales the image to 40x30 with a transparent background
  def update(self): #update function runs every frame
    if Game.paused(): #checks if the game is paused
      self.getImage() #sets the birds image to let you change colors in pause menu
      screen.blit(self.image, self.rect) #blits the bird onto the screen
    if Game.playing(): #checks if the game is in a level
      self.getImage() #sets the birds image
      self.velo += 0.2 #gives the bird a constant downward force (gravity)
      self.rect.y += self.velo #moves the bird according to its velocity
      screen.blit(self.image, self.rect) #blits the bird on the screen
class StartButton(Button): #sprite class to display/handle start button calculations, extends another button class I made
  def __init__(self, x, y, width, height): #runs on instance creation
    super().__init__(x, y, width, height, image=('./buttons.png', (0, 0, 52, 29))) #initializes inner button class with its size, coords, and image
  def update(self): #update function runs every frame
    if Game.starting(): screen.blit(self.image, self.rect) #checks if the game is in the start menu, and blits itself to the screen
  def onButtonClick(self): #runs every time the user clicks on an overlapping coordinate with the button
    if Game.starting(): start(0) #checks if the game is in the start menu, and starts the game at the first level
class LevelSelectButton(Button): #sprite class to display/handle level select button calculations, extends another button class I made
  def __init__(self, x, y, width, height): #runs on instance creation
    super().__init__(x, y, width, height, image=('./buttons.png', (54, 0, 52, 29))) #initializes inner button class with its size, coords, and image
  def update(self): #update function runs every frame
    if Game.starting(): screen.blit(self.image, self.rect) #checks if the game is in the start menu, and blits itself to the screen
  def onButtonClick(self): #runs every time the user clicks on an overlapping coordinate with the button
    if Game.starting(): Game.section = 'Menu' #checks if the game is in the start menu, and makes the game go to the level select menu
class InfButton(Button): #sprite class to display/handle infinite mode button calculations
  def __init__(self, x, y, width, height): #runs on instance creation
    super().__init__(x, y, width, height, image=('./buttons.png', (54, 30, 52, 29))) #initializes inner button class with its size, coords, and image
  def update(self): #update function runs every frame
    if Game.starting(): screen.blit(self.image, self.rect) #checks if the game is in the start menu, and blits itself to the screen
  def onButtonClick(self): #runs every time the user clicks on an overlapping coordinate with the button
    if Game.starting(): start(-1) #checks if the game is in the start menu, and starts the game on infinite mode
class LevelButton(Button): #sprite class to display/handle level select button calculations
  def __init__(self, x, y, width, height, level, section): #runs on instance creation
    super().__init__(x, y, width, height, image=('./buttons.png', (0, 30+15*level, 40, 14))) #initializes inner button class with its size, coords, and image
    self.level = level #stores the level this button leads to
    self.section = section #stores which section it should display on
  def update(self): #update function runs every frame
    if self.section(): screen.blit(self.image, self.rect) #checks if the game is in the right section to show on, and blits itself to the screen
  def onButtonClick(self): #runs every time the user clicks on an overlapping coordinate with the button
    if self.section(): start(self.level) #checks if the game is in the right section to show on, and starts the game at its level
class NextLevelButton(Button): #sprite class to display/handle next level button calculations
  def __init__(self, x, y, width, height, level, section): #runs on instance creation
    super().__init__(x, y, width, height, image=('./buttons.png', (0, 30+15*level, 40, 14))) #initializes inner button class with its size, coords, and image
    self.level = level #stores the level this button leads to
    self.section = section #stores which section and which level it should display on
  def update(self): #update function runs every frame
    if self.section[0]() and Game.level == self.section[1]: screen.blit(self.image, self.rect) #checks if the game is on the right section and on the right level, and blits itself to the screen
  def onButtonClick(self): #runs every time the user clicks on an overlapping coordinate with the button
    if self.section[0]() and Game.level == self.section[1]: start(self.level) #checks if the game is on the right section and on the right level, and starts the game at its level
class Pipe(pygame.sprite.Sprite): #sprite class to display/handle pipe calculations
  def __init__(self, height, speed, top, x): #runs on instance creation
    super().__init__() #initializes inner sprite class
    self.image = pygame.Surface((28, 160)) #creates blank surface
    if top: #checks if the pipe is supposed to be the top pipe
      self.image.blit(pygame.image.load('./pipes.png'), (0, 0), (56, 0, 28, 160)) #blits a pipe image onto the sprite
      self.image = pygame.transform.scale(self.image, (84, 480)) #scales the sprite to 84x480
      self.image = self.image.convert_alpha() #makes the sprite transparent
      self.rect = self.image.get_rect() #creates a rectangle at the sprite
      self.rect.topleft = (x, 450-self.rect.height-height) #moves the sprite to its position
      self.height = 450-self.rect.height-height #stores the rectangle's base height to determine how far up and down it can go
      self.down = False #stores which direction the pipe is going
    else: #if the pipe is supposed to be the bottom pipe
      self.image.blit(pygame.image.load('./pipes.png'), (0, 0), (84, 0, 28, 160)) #blits a pipe image onto the sprite
      self.image = pygame.transform.scale(self.image, (84, 480)) #scales the sprite to 84x480
      self.image = self.image.convert_alpha() #makes the sprite transparent
      self.rect = self.image.get_rect() #creates a rectangle at the sprite
      self.rect.topleft = (x, 600-height) #moves the sprite to its position
      self.height = 600-height+50 #stores the rectangle's base height to determine how far up and down it can go
      self.down = True #stores which direction the pipe is going
    self.speed = speed #stores how quickly the pipe moves across the screen
    self.done = False #stores whether or not the pipe has created a second pipe
  def update(self): #update function runs every frame
    if Game.playing(): #checks if the game is in a level
      if Game.level == 2: #checks if the game is on the third level
        if self.down: #checks if the pipe should be moving down
          self.rect.y += 1 #moves the pipe down by one pixel
          if self.rect.y >= self.height: #checks if the pipe is at the bottom of its height
            self.down = False #makes the pipe start moving back up
        else: #if the pipe should be moving up
          self.rect.y -= 1 #moves the pipe up by one pixel
          if self.rect.y <= self.height-50: #checks if the pipe is at the top of its height
            self.down = True #makes the pipe start moving back down
      self.rect.x -= self.speed #moves the pipe to the left by its speed
      screen.blit(self.image, self.rect) #blits the pipe to the screen
    if Game.paused(): #checks if the game is paused
      screen.blit(self.image, self.rect) #blits the pipe to the screen
    if self.rect.right <= 800 and not self.done and Game.level == -1: #checks if the game is in infinite mode, the pipe hasn't created another pipe yet, and the pipe is a certain amount across the screen
      newPipe(pipes, random.randint(100, 300), self.speed, 1200) #creates a new pipe at a random height with its own speed
      self.done = True #makes sure it cant create any more pipes
    if self.rect.right <= 0: #checks if the pipe is all the way off the screen
      Game.score += 0.5 #gives the player half a point
      self.kill() #removes itself to not kill the game at high points
class LoseText(pygame.sprite.Sprite): #sprite class to display win/lose text background
  def __init__(self, x, y): #runs on instance creation
    super().__init__() #initializes inner sprite class
    self.image = pygame.Surface((113, 57)) #creates an empty surface
    self.image.blit(pygame.image.load('./displays.png'), (0, 0), (0, 0, 113, 57)) #blits the image onto itself
    self.image = pygame.transform.scale(self.image, (452, 228)).convert_alpha() #scales the image to 452x228 and makes it transparent
    self.rect = self.image.get_rect() #gives the sprite a rectangle
    self.rect.topleft = (x, y) #moves the sprite to position (x, y)
  def update(self): #update function runs every frame
    if Game.lost() or Game.won(): #checks if the player died or finished a level
      screen.blit(self.image, self.rect) #blits itself to the screen
class NumberSprite(pygame.sprite.Sprite): #sprite class to display numbers
  def __init__(self, section, num, size, scale, pos): #runs on instance creation
    super().__init__() #initializes inner sprite class
    imPath = '' #creates a variable to store the image path
    switch(size) #checks what size it should be
    if case(0): #if it should be size 0
      charSize = (6, 7) #variable to store dimensions of the number
      imPath = './smallNumbers.png' #path to smallest numbers
    if case(1): #if it should be size 1
      charSize = (7, 10) #variable to store dimensions of the number
      imPath = './score.png' #path to medium numbers
    if case(2): #if it should be size 2
      charSize = (12, 18) #variable to store dimensions of the number
      imPath = './bigNumbers.png' #path to biggest numbers
    self.image = pygame.Surface(charSize) #creates an empty surface with dimensions of it immage
    self.image.blit(pygame.image.load(imPath), (0, 0), (14*num, 0, charSize[0], charSize[1])) #blits the number at its size onto the image
    self.image = pygame.transform.scale(self.image, (charSize[0]*scale, charSize[1]*scale)).convert_alpha() #scales the sprite up by its scale
    self.rect = self.image.get_rect() #creates a rectangle for the sprite
    self.rect.topleft = pos #moves the sprite to position pos
    self.num = num #variable to store what number the sprite has
    self.section = section #variable to store what section the sprite should be displayed on
  def update(self): #update function runs every frame
    if self.section(): screen.blit(self.image, self.rect) #checks if the game is on the right section and blits itself to the screen
class Medal(pygame.sprite.Sprite): #class to display medals
  def __init__(self, x, y, type, level): #runs on instance creation
    super().__init__() #initializes inner sprite class
    self.image = pygame.Surface((22, 22)) #creates an empty surface
    self.image.blit(pygame.image.load('./medals.png'), (0, 0), (type*24, 0, 22, 22)) #blits the correct medal onto the surface
    self.image = pygame.transform.scale(self.image, (88, 88)).convert_alpha() #scales the image up to 88x88 and makes it transparent
    self.rect = self.image.get_rect() #gives the image a rectangle
    self.rect.topleft = (x, y) #moves the sprite to position (x, y)
    self.level = level #determines what level the medal should be displayed on
  def update(self): #update function runs every frame
    if Game.won() and Game.level == self.level: #checks if the game is on the win screen of the correct level
      screen.blit(self.image, self.rect) #blits itself to the screen
class PauseButton(Button): #class to display/handle pause button calculations
  def __init__(self, x, y, width, height): #runs on instance creation
    super().__init__(x, y, width, height, image=('./buttons.png', (150, 0, 13, 14))) #initializes inner button class with its size, coords, and image
  def update(self): #update function runs every frame
    self.image = pygame.Surface((13, 14)) #sets its image to an empty surface
    if Game.paused(): #checks if the game is in the pause menu
      self.image.blit(pygame.image.load('./buttons.png'), (0, 0), (150, 0, 13, 14)) #blits the play button onto its image
      self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height)) #scales the image to its previous size
      screen.blit(self.image, self.rect) #blits itself onto the screen
    elif Game.playing(): #checks if the game is in a level
      self.image.blit(pygame.image.load('./buttons.png'), (0, 0), (150, 15, 13, 14)) #blits the pause button onto its image
      self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height)) #scales the image to its previous size
      screen.blit(self.image, self.rect) #blits itself onto the screen
  def onButtonClick(self): #runs every time the user clicks on an overlapping coordinate with the button
    if Game.paused(): #checks if the game is paused
      Game.section = 'Game' #makes the game go back to the level
      flap.velo = flap.lastVelo #set the birds velocity to its previous velocity
    elif Game.playing(): #checks if the game is in a level
      Game.section = 'Pause' #pauses the game
class ContinueButton(Button): #sprite class to display/handle continue button calculations
  def __init__(self, x, y, width, height): #runs on instance creation
    super().__init__(x, y, width, height, image=('./buttons.png', (108, 15, 40, 14))) #initializes inner button class with its size, coords, and image
  def update(self): #update function runs every frame
    if Game.paused(): #checks if the game is paused
      screen.blit(self.image, self.rect) #blits itself onto the screen
  def onButtonClick(self): #runs every time the user clicks on an overlapping coordinate with the button
    if Game.paused(): #checks if the game is paused
      Game.section = 'Game' #makes the game go back to the level
      flap.velo = flap.lastVelo #sets the birds velocity to its previous velocities
class MenuButton(Button): #sprite class to display/handle menu button calculations
  def __init__(self, x, y, width, height, section): #runs on instance creation
    super().__init__(x, y, width, height, image=('./buttons.png', (108, 0, 40, 14))) #initializes inner button class with its size, coords, and image
    self.section = section #stores which section the button should be displayed on
  def update(self): #update function runs every frame
    if self.section(): #checks if the game is on the right section
      screen.blit(self.image, self.rect) #blits itself to the screen
  def onButtonClick(self): #runs every time the user clicks on an overlapping coordinate with the button
    if self.section(): #checks if the game is on the right section
      Game.section = 'Start' #makes the game go back to the start screen
class ColorSelectButton(Button): #sprite class to display/handle color select button calculations
  def __init__(self, x, y, width, height, color): #runs on instance creation
    super().__init__(x, y, width, height, image=('./birds.png', (color*21, 28, 17, 12))) #initializes inner button class with its size, coords, and image
    self.color = color #stores what color the button is
  def update(self): #update function runs every frame
    if Game.paused(): #checks if the game is paused
      screen.blit(self.image, self.rect) #blits itself to the screen
  def onButtonClick(self): #runs every time the user clicks on an overlapping coordinate with the button
    if Game.paused(): #checks if the game is paused
      flap.color = self.color #sets the birds color to its color
def start(level): #function to start each level
  Game.level = level #sets the game level to its level
  Game.section = 'Game' #sets the game to the playing section
  Game.score = 0 #sets the score to 0
  for sprite in pipes: sprite.kill() #deletes every pipe
  for sprite in bg: sprite.kill() #clears the background
  for sprite in text: sprite.kill() #clears all text
  bg.add(Background(000, 1)) #creates a background sprite
  bg.add(Background(392, 1)) #creates a background sprite
  bg.add(Background(784, 1)) #creates a background sprite
  bg.add(Background(1176,1)) #creates a background sprite
  flap.rect.y = 280 #sets the birds y position to the middle
  flap.velo = -7 #starts the bird out moving up
  if Game.level == -1: #if the game is in infinite mode
    newPipe(pipes, random.randint(100, 300), 6, 1200) #creates a pipe on the right side of the screen
    newPipe(pipes, random.randint(100, 300), 6, 1200) #creates a pipe on the right side of the screen
    return None #ends the function
  for i in range(5*sum(range(Game.level+2))): #creates a 5/15/30 long loop depending on the level
    tempInt = random.randint(100, 300) #stores the height difference of the pipes for debug purposes
    print(tempInt) #prints the height difference of the pipes for debug purposes
    newPipe(pipes, tempInt, 6, 1200+(400*i)) #creates a pipe off the right side of the screen depending on which pipe it is
    newPipe(pipes, tempInt, 6, 1200+(400*i)) #creates a pipe off the right side of the screen depending on which pipe it is
def newPipe(group, height, speed, x): #function to create 2 new pipes at once
  global pipeCounter #global variable to store how many pipes have been created
  pipeCounter += 1 #increments the counter by 1
  if pipeCounter%2 == 1: #makes sure the overall function only runs every other time its called
    return None #quit the function
  group.add(Pipe(height, speed, True, x)) #creates a top pipe at a specific height, speed, and x position
  group.add(Pipe(height, speed, False, x)) #creates a bottom pipe at a specific height, speed, and x position
flap = Bird(100, 280) #creates an instance of the bird class
bg = pygame.sprite.Group() #creates a group to store the backgrounds
bg.add(Background(000, 4)) #adds an instance of the background class to the background group
bg.add(Background(392, 4)) #adds an instance of the background class to the background group
bg.add(Background(784, 4)) #adds an instance of the background class to the background group
bg.add(Background(1176,4)) #adds an instance of the background class to the background group
pipeCounter = 0 #creates the variable for the newPipe function
pipes = pygame.sprite.Group() #creates a group to store the pipes
buttons = pygame.sprite.Group() #creates a group to store the buttons
buttons.add(StartButton(364, 271, 104, 58)) #adds a StartButton to the button group
buttons.add(LevelSelectButton(612, 271, 104, 58)) #adds a level select button to the button group
buttons.add(InfButton(488, 271, 104, 58)) #adds an infinite mode button to the button group
buttons.add(LevelButton(460, 128, 160, 56, 0, Game.inMenu)) #adds a level button to the button group
buttons.add(LevelButton(460, 192, 160, 56, 1, Game.inMenu)) #adds a level button to the button group
buttons.add(LevelButton(460, 256, 160, 56, 2, Game.inMenu)) #adds a level button to the button group
buttons.add(PauseButton(1028, 0, 52, 56)) #adds a pause button to the button group
buttons.add(MenuButton(460, 320, 160, 56, Game.inMenu)) #adds a menu button to the button group
buttons.add(MenuButton(460, 360, 160, 56, Game.paused)) #adds a menu button to the button group
buttons.add(MenuButton(320, 444, 160, 56, Game.lost)) #adds a menu button to the button group
buttons.add(MenuButton(320, 444, 160, 56, Game.won)) #adds a menu button to the button group
buttons.add(NextLevelButton(600, 444, 160, 56, 1, (Game.won, 0))) #adds a next level button to the button group
buttons.add(NextLevelButton(600, 444, 160, 56, 2, (Game.won, 1))) #adds a next level button to the button group
buttons.add(NextLevelButton(600, 444, 160, 56, 3, (Game.won, 2))) #adds a next level button to the button group
buttons.add(NextLevelButton(600, 444, 160, 56, -1, (Game.won, 3))) #adds a next level button to the button group
buttons.add(NextLevelButton(600, 444, 160, 56, 0, (Game.lost, 0))) #adds a next level button to the button group
buttons.add(NextLevelButton(600, 444, 160, 56, 1, (Game.lost, 1))) #adds a next level button to the button group
buttons.add(NextLevelButton(600, 444, 160, 56, 2, (Game.lost, 2))) #adds a next level button to the button group
buttons.add(NextLevelButton(600, 444, 160, 56, 3, (Game.lost, 3))) #adds a next level button to the button group
buttons.add(ContinueButton(460, 280, 160, 56)) #adds a continue button to the button group
buttons.add(ColorSelectButton(430, 200, 60, 45, 0)) #adds a color select button to the button group
buttons.add(ColorSelectButton(510, 200, 60, 45, 1)) #adds a color select button to the button group
buttons.add(ColorSelectButton(590, 200, 60, 45, 2)) #adds a color select button to the button group
permDisplay = pygame.sprite.Group() #creates a group to store permanent displays
permDisplay.add(LoseText(314, 186)) #adds a win/lose background to the display background group
permDisplay.add(Medal(366, 270, 0, 0)) #adds a medal to the display background group
permDisplay.add(Medal(366, 270, 1, 1)) #adds a medal to the display background group
permDisplay.add(Medal(366, 270, 2, 2)) #adds a medal to the display background group
permDisplay.add(Medal(366, 270, 3, 3)) #adds a medal to the display background group
text = pygame.sprite.Group() #creates a group to store text
def longScore(group, score, section, size, scale, width, topright): #function to create multiple digit number sprites
  for char in str(score)[::-1]: #loops through the digits of the number in reverse
    group.add(NumberSprite(section, int(char), size, scale, (topright[0]-width, topright[1]))) #creates a sprite at a certain position and adds it to the group
    topright[0] -= (width + 4) #moves the position of the sprite to the left so the next sprite can be created

def level1(): #function to check if the player won
  if Game.score >= (5*sum(range(Game.level+2))) and Game.playing() and not Game.level == -1: #checks if the player has a high enough score, is in a level, and is not in infinite mode
    longScore(text, int(Game.score), Game.won, 0, 4, 24, [718, 254]) #adds a sprite of the player's score to the win screen
    Game.section = 'Win' #goes to the win screen
clock = pygame.time.Clock() #clock to keep a consistent frame rate
running = True #variable to end main loop
while running: #main loop
  clock.tick(60) #keeps the game at 60 fps
  for event in pygame.event.get(): #runs through events
    if event.type == pygame.QUIT: running = False #lets you x out of the game
    if event.type == pygame.MOUSEBUTTONDOWN and Game.playing(): #when you click and are in a level
      flap.lastVelo = flap.velo #stores the last velocity the player was at, for pausing/unpausing
      flap.velo = -7 #makes the player start miving upwards
    for button in buttons: button.onEvent(event) #checks to see if you clicked any button
  key = pygame.key.get_pressed() #gets all held keys
  screen.fill((255, 255, 255)) #clears the screen
  bg.draw(screen) #displays the background
  if ((pygame.sprite.spritecollide(flap, pipes, False) and not key[pygame.K_SPACE]) or (flap.rect.y < 0 or flap.rect.bottom > 600)) and Game.playing(): #checks if you are colliding with a pipe (and not holding space) or hit the ground/ceiling, and you are in a level
    Game.section = 'Lose' #goes to the lose screen
    if Game.best < Game.score: Game.best = Game.score #gives yourself a new best
    longScore(text, int(Game.score), Game.lost, 0, 4, 24, [718, 254]) #creates a sprite of your current score on the lose screen
    longScore(text, int(Game.best), Game.lost, 0, 4, 24, [718, 338]) #creates a sprite of your best score on the lose screen
    longScore(text, int(Game.best), Game.won, 0, 4, 24, [718, 338]) #creates a sprite of your best score on the win screen
  pipes.update() #updates all pipes
  buttons.update() #updates all buttons
  bg.update() #updates background
  flap.update() #updates bird
  permDisplay.update() #updates all displays
  text.update() #updates all text
  level1() #checks if the player won
  pygame.display.flip() #displays the new screen to the user