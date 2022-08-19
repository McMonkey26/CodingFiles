import pygame, random, os
from switch import *
os.chdir('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PythonFiles/pacman')

#initializes pygame, and creates a blank screen surface
pygame.init()
screen = pygame.display.set_mode((1000, 600))
screen.fill((0, 0, 0))

#creates list for the map layout
# 0 = dot
# 1 = wall
# 2 = ghost
# 3 = blank
wallMap = [
  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
  1,0,0,0,0,0,0,2,0,0,0,0,2,0,0,0,0,0,0,1,
  1,0,1,1,1,0,1,0,1,1,1,1,0,1,0,1,1,1,0,1,
  1,0,1,1,1,0,0,2,1,3,3,1,2,0,0,1,1,1,0,1,
  1,0,1,0,0,0,1,1,1,3,3,1,1,1,0,0,0,1,0,1,
  1,0,1,1,1,0,1,0,1,3,3,1,0,1,0,1,1,1,0,1,
  1,0,0,0,1,0,1,0,1,3,3,1,0,1,0,1,0,0,0,1,
  1,0,1,0,1,0,1,0,1,1,1,1,0,1,0,1,0,1,0,1,
  1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,
  1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
  1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1
]
#function to find all the borders for walls
def checkBorders(position, matrixMap):
  pos0 = position//1000 #gets the position for the 2d list
  pos1 = position%1000//50 #gets the position for the 2d list
  borders = [
    [3, 3, 3],
    [3, 3, 3],
    [3, 3, 3]
  ] #creates an effectively blank array
  #next 36 lines are the same loop so im only commenting the first one
  try: #handle the index error
    borders[0][0] = matrixMap[pos0-1][pos1-1] if pos0-1 >= 0 and pos1-1 >= 0 else 2 #checks if the element one above and one to the left of the element ur checking is equal to it, and makes sure the positions don't become negative and warp around the wrong way
  except IndexError: #handles if the position would go out of the matrix
    borders[0][0] = 3 #sets the value to the original placeholder
  try: #top middle
    borders[0][1] = matrixMap[pos0-1][pos1] if pos0-1 >= 0 and pos1 >= 0 else 2
  except IndexError:
    borders[0][1] = 3
  try: #top right
    borders[0][2] = matrixMap[pos0-1][pos1+1] if pos0-1 >= 0 and pos1+1 >= 0 else 2
  except IndexError:
    borders[0][2] = 3
  try: #middle left
    borders[1][0] = matrixMap[pos0][pos1-1] if pos0 >= 0 and pos1-1 >= 0 else 2
  except IndexError:
    borders[1][0] = 3
  try: #middle middle
    borders[1][1] = matrixMap[pos0][pos1] if pos0 >= 0 and pos1 >= 0 else 2
  except IndexError:
    borders[1][1] = 3
  try: #middle right
    borders[1][2] = matrixMap[pos0][pos1+1] if pos0 >= 0 and pos1+1 >= 0 else 2
  except IndexError:
    borders[1][2] = 3
  try: #bottom left
    borders[2][0] = matrixMap[pos0+1][pos1-1] if pos0+1 >= 0 and pos1-1 >= 0 else 2
  except IndexError:
    borders[2][0] = 3
  try: #bottom middle
    borders[2][1] = matrixMap[pos0+1][pos1] if pos0+1 >= 0 and pos1 >= 0 else 2
  except IndexError:
    borders[2][1] = 3
  try: #bottom bottom
    borders[2][2] = matrixMap[pos0+1][pos1+1] if pos0+1 >= 0 and pos1+1 >= 0 else 2
  except IndexError:
    borders[2][2] = 3
  #returns a list that tells you which bordering elements are equal
  switch(borders[1][1])
  returnList = []
  for pos in borders:
    returnList.append([])
    for x in pos:
      returnList[-1].append((case(x) or case(x+2) or case(x-2)))
  return returnList
#function to find if the indexes are true and no other values are true
def only(checkList, *indexes):
  return all([checkList[x] for x in indexes]) and not any([checkList[x] for x in range(len(checkList)) if not x in indexes])
#turns the 1d list into a 2d list
wallMap2d = [wallMap[x:x+20] for x in range(len(wallMap)) if x%20==0]
intersectionList = {} #creates a dictionary to store places for the ghosts to turn
for point in range(len(wallMap)): #loops through the map list
  if wallMap[point] == 0 or wallMap[point] == 2: #if the current element is a dot or a ghost (so an empty square)
    border = checkBorders(point*50, wallMap2d) #gets the borders of that element
    tempList = [border[1][2], border[1][0], border[0][1], border[2][1]] #lowers it down to only the top middle, middle left, middle right, and bottom middle
    if not (only(tempList, 0, 1) or only(tempList, 2, 3)): #makes sure the tile isn't just a straight line
      intersectionList[((point*50)%1000, (point//20)*50)] = [x for x in range(4) if tempList[x]] #gets all the possible turns for that intersection and puts it to the dictionary, with the key being a tuple position at that location
def getImage(borderMap): #function to get the image for a wall
  tempImage = pygame.Surface((16, 16)) #creates an empty surface
  spriteMap = pygame.image.load('./walls.png') #loads an image with the walls
  borders = [borderMap[0][1], borderMap[1][2], borderMap[2][1], borderMap[1][0]] #gets the top bottom left and right borders
  if only(borders, 0): #all of these elif statements just go through every possible orientation of borders and gets the correct wall
    tempImage.blit(spriteMap, (0, 0), (0, 32, 16, 16)) #blits the image onto the empty surface, cropped to only the image i want
    tempImage = pygame.transform.rotate(tempImage, 0) #rotates the image by the necessary amount
  elif only(borders, 1):
    tempImage.blit(spriteMap, (0, 0), (0, 32, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 270)
  elif only(borders, 2):
    tempImage.blit(spriteMap, (0, 0), (0, 32, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 180)
  elif only(borders, 3):
    tempImage.blit(spriteMap, (0, 0), (0, 32, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 90)
  elif only(borders, 0, 1):
    tempImage.blit(spriteMap, (0, 0), (0, 0, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 90)
  elif only(borders, 1, 2):
    tempImage.blit(spriteMap, (0, 0), (0, 0, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 0)
  elif only(borders, 2, 3):
    tempImage.blit(spriteMap, (0, 0), (0, 0, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 270)
  elif only(borders, 3, 0):
    tempImage.blit(spriteMap, (0, 0), (0, 0, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 180)
  elif only(borders, 0, 2):
    tempImage.blit(spriteMap, (0, 0), (16, 0, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 90)
  elif only(borders, 1, 3):
    tempImage.blit(spriteMap, (0, 0), (16, 0, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 0)
  elif only(borders, 0, 1, 2):
    tempImage.blit(spriteMap, (0, 0), (0, 16, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 0)
  elif only(borders, 1, 2, 3):
    tempImage.blit(spriteMap, (0, 0), (0, 16, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 270)
  elif only(borders, 2, 3, 0):
    tempImage.blit(spriteMap, (0, 0), (0, 16, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 180)
  elif only(borders, 3, 0, 1):
    tempImage.blit(spriteMap, (0, 0), (0, 16, 16, 16))
    tempImage = pygame.transform.rotate(tempImage, 90)
  elif all(borders):
    tempImage.blit(spriteMap, (0, 0), (16, 16, 16, 16))
  else:
    tempImage.blit(spriteMap, (0, 0), (16, 32, 16, 16))
  return pygame.transform.scale(tempImage, (50, 50)) #returns the image, scaled to 50x50
class Wall(pygame.sprite.Sprite): #wall class
  def __init__(self, pos): #creates the sprite
    super().__init__() #initializes the sprite
    self.image = pygame.Surface((50, 50)) #empty 50x50 surface
    self.rect = self.image.get_rect() #gives it a rectangle
    self.rect.topleft = (pos%1000, (pos//1000)*50) #sets the rectangle to specific coords
    border = checkBorders(pos, wallMap2d) #gets its borders
    self.image = getImage(border) #sets its image based on those borders
class Dot(pygame.sprite.Sprite): #dot class
  def __init__(self, pos): #creates the sprite
    super().__init__() #initializes the sprite
    self.image = pygame.Surface((10, 10)) #creates a 10x10 rectangle
    self.image.fill((255, 255, 255)) #makes it white
    self.rect = self.image.get_rect() #gives it a rectangle
    self.rect.center = (pos%1000+25, (pos//1000)*50+25) #sets its center to the center of its coords
  def collide(self, pacman): #checks collision
    if pygame.sprite.collide_rect(self, pacman): #if it is colliding with pacman
      pacman.score += 10 #gives pacman 10 score
      self.kill() #deletes itself
class Ghost(pygame.sprite.Sprite): #ghost class
  def __init__(self, color, pos): #creates sprite
    super().__init__() #initializes sprite
    self.image = pygame.Surface((16, 16)) #empty surface
    self.sprite = pygame.image.load('./pacmanSprites.png').convert_alpha() #loads the sprite sheet
    self.color = color #sets its own color
    self.baseCoords = [3, 64 + 16 * self.color, 16, 16] #list of coordinates to get the image from the sprite sheet
    self.image.blit(self.sprite, (0, 0), self.baseCoords) #blits it onto the sprite surface
    self.image = pygame.transform.scale(self.image, (50, 50)) #makes it 50x50
    self.rect = self.image.get_rect() #gives itself a rectangle
    self.rect.topleft = (pos%1000, (pos//1000)*50) #sets it to the right coords
    self.direction = Dir.RIGHT #sets its direction
    self.frame = 0 #frame variable for animation
    self.velo = [10, 0] #base velocity
  def setImage(self): #used to change direction its facing and frame its on
    self.baseCoords[1] = 64 + 16 * self.color #this sets the y position to whatever line its color is on
    self.baseCoords[0] = 3 + (self.frame//10 % 2) * 16 + (self.direction * 32) #sets the x direction to which frame and which direction its facing
    self.image = pygame.Surface((16, 16)) #clears the image
    self.image.blit(self.sprite, (0, 0), self.baseCoords) #blits the new coords on it
    self.image = pygame.transform.scale(self.image, (50, 50)) #makes it 50x50
  def update(self): #runs every frame
    self.switchDirec() #turn function
    switch(self.direction) #gets the direction
    if case(Dir.LEFT): self.velo = [-10, 0] #sets the velocity based on its direction
    elif case(Dir.RIGHT): self.velo = [10, 0] #sets the velocity based on its direction
    elif case(Dir.UP): self.velo = [0, -10] #sets the velocity based on its direction
    elif case(Dir.DOWN): self.velo = [0, 10] #sets the velocity based on its direction
    self.frame += 1 #goes to the next frame
    self.setImage() #sets its image
    if self.frame%2 == 0: #runs every other frame
      self.rect.x += self.velo[0] #moves right by x velocity
      self.rect.y += self.velo[1] #moves down by y velocity
    screen.blit(self.image, self.rect) #adds itself to the screen
  def switchDirec(self): #function to turn
    if self.rect.topleft in intersectionList.keys(): #checks if its at an intersection
      if self.direction in intersectionList[self.rect.topleft] and random.random() > 0.4: #gives it a 60% chance to keep going forward, if it wont run into a wall
        return None #if it wants to keep going, then the function stops here
      self.direction = random.choice(intersectionList[self.rect.topleft]) #sets it to a random direction based on that intersection
class Direction: #basically an enum
  def __init__(self): #creates the instance
    self.RIGHT = 0 #gives variable
    self.LEFT = 1 #gives variable
    self.UP = 2 #gives variable
    self.DOWN = 3 #gives variable
Dir = Direction() #creates the enum
walls = pygame.sprite.Group() #group to store walls
dots = pygame.sprite.Group() #group to store dots
ghosts = pygame.sprite.Group() #group to store ghosts
color = 0 #variable to change colors
for tile in range(len(wallMap)): #goes through the map list
  if wallMap[tile] == 1: #if there should be a wall
    walls.add(Wall(tile*50)) #creates a wall at that position
  elif wallMap[tile] == 0: #if there should be a dot
    dots.add(Dot(tile*50)) #creates a dot at that position
  elif wallMap[tile] == 2: #if there should be a ghost
    ghosts.add(Ghost(color%4, tile*50)) #creates a ghost at that position and color
    color += 1 #goes to the next color
class Pacman(pygame.sprite.Sprite): #pacman sprite
  def __init__(self): #creates sprite
    super().__init__() #initializes sprite
    self.image = pygame.Surface((16, 16)) #empty surface
    self.sprite = pygame.image.load('./pacmanSprites.png').convert_alpha() #loads the image
    self.image.blit(self.sprite, (0, 0), (0, 0, 16, 16)) #starts out frame 1 facing right
    self.image = pygame.transform.scale(self.image, (50, 50)) #goes to 50x50 square
    self.rect = self.image.get_rect() #creates rectangle
    self.rect.topleft = (450, 400) #sets to starting coords
    self.direction = 'r' #sets direction for getting image
    self.frame = 0 #sets frame for getting image
    self.velo = [0, 0] #creates velocity for moving
    self.dead = False #variable to make sure you can't do things while dieing
    self.died = False #variable to let you restart once you've died
    self.deathFrame = 0 #frame counter for death animation
    self.lives = 3 #life counter for multiple lives
    self.score = 0 #score counter because its required
  def setImage(self): #function to set its image
    global winState #this variable determines which loop gets run, gamescreen/winscreen/losescreen
    spriteCoords = [3, 0, 16, 16] #variable to get image, x starts as 3 because its a bit off
    if (self.frame%20 >= 10): spriteCoords[0] = 19 #if its on frame 2, goes to the frame 2 column
    switch(self.direction) #checks the direction, no right facing because its right by default
    if case(pygame.K_LEFT): spriteCoords[1] = 16 #left facing
    elif case(pygame.K_UP): spriteCoords[1] = 32 #up facing
    elif case(pygame.K_DOWN): spriteCoords[1] = 48 #down facing
    if self.dead: #if pacman just died
      spriteCoords[1] = 0 #ignores the direction stuff and goes to the top
      spriteCoords[0] = 35 + 16 * (self.deathFrame//5) #sets its x coordinate to the start of the death animation, and goes to the next frame every 1/8 of a second
      if self.deathFrame == 70: #once the death animation is finished
        self.lives -= 1 #takes a life
        self.score -= 100 #removes 100 score
        if self.score < 0: #makes sure the score isnt negative
          self.score = 0
        self.died = True #lets you restart the game
        if self.lives == 0: #checks if you have lives left
          winState = 0 #switches to running the loss screen
    self.image = pygame.Surface((16, 16)) #clears the surface
    self.image.blit(self.sprite, (0, 0), spriteCoords) #blits the image onto it
    self.image = pygame.transform.scale(self.image, (50, 50)) #makes it 50x50
  def update(self): #runs every frame
    global winState #determines which screen gets run
    switch(self.velo) #sets direction based off of velocity
    if case([-10, 0]): self.direction = pygame.K_LEFT
    elif case([10, 0]): self.direction = pygame.K_RIGHT
    elif case([0, -10]): self.direction = pygame.K_UP
    elif case([0, 10]): self.direction = pygame.K_DOWN
    self.frame += 1 #goes to the next frame
    if self.dead: self.deathFrame += 1 #if its dead, goes to the next dead frame
    self.setImage() #gets the right image
    self.turn() #function to turn
    #\/\/\/ makes sure pacman doesnt collide with a wall
    if self.velo[0] < 0 and any(list(map(lambda x: pygame.Rect(self.rect.x-1, self.rect.y, self.rect.width, self.rect.height).colliderect(x), walls))): self.velo[0] = 0
    if self.velo[0] > 0 and any(list(map(lambda x: pygame.Rect(self.rect.x+1, self.rect.y, self.rect.width, self.rect.height).colliderect(x), walls))): self.velo[0] = 0
    if self.velo[1] < 0 and any(list(map(lambda x: pygame.Rect(self.rect.x, self.rect.y-1, self.rect.width, self.rect.height).colliderect(x), walls))): self.velo[1] = 0
    if self.velo[1] > 0 and any(list(map(lambda x: pygame.Rect(self.rect.x, self.rect.y+1, self.rect.width, self.rect.height).colliderect(x), walls))): self.velo[1] = 0
    #/\/\/\ makes sure pacman doesnt collide with a wall
    #every other frame moves pacman by velocity
    if self.frame%2 == 0: self.rect.x += self.velo[0]
    if self.frame%2 == 0: self.rect.y += self.velo[1]
    if pygame.sprite.spritecollide(self, ghosts, False): self.die() #checks if it hit a ghost
    if len(dots.sprites()) == 0: #checks if you ate all the dots
      winState = 2 #won
    screen.blit(self.image, self.rect) #blits the sprite to the screen
    # pygame.draw.rect(screen, (180, 180, 180), self.rect)
  def turn(self): #function to turn
    if self.dead: return None #stops the function if pacman is dead
    key = pygame.key.get_pressed() #gets pressed keys
    if key[pygame.K_UP] and not any(list(map(lambda x: pygame.Rect(self.rect.x, self.rect.y-1, self.rect.width, self.rect.height).colliderect(x), walls))): #makes sure theres not a wall above you
      self.velo[0] = 0 #sets x velocity to 0
      self.velo[1] = -10 #sets y velocity to up 10
    elif key[pygame.K_DOWN] and not any(list(map(lambda x: pygame.Rect(self.rect.x, self.rect.y+1, self.rect.width, self.rect.height).colliderect(x), walls))): #see above
      self.velo[0] = 0 #see above
      self.velo[1] = 10 #see above
    elif key[pygame.K_LEFT] and not any(list(map(lambda x: pygame.Rect(self.rect.x-1, self.rect.y, self.rect.width, self.rect.height).colliderect(x), walls))): #see above
      self.velo[0] = -10 #see above
      self.velo[1] = 0 #see above
    elif key[pygame.K_RIGHT] and not any(list(map(lambda x: pygame.Rect(self.rect.x+1, self.rect.y, self.rect.width, self.rect.height).colliderect(x), walls))): #see above
      self.velo[0] = 10 #see above
      self.velo[1] = 0 #see above
  def die(self): #runs when you die
    self.velo = [0, 0] #stops you from moving
    self.dead = True #makes you dead
    for ghost in ghosts: ghost.kill() #removes all ghosts
    
  def start(self): #runs when you restart
    if self.lives == 0: #function doesnt run if you ran out of left
      return None
    self.rect.topleft = (450, 400) #puts you in the middle of the screen
    self.dead = False #makes you not dead
    self.died = False #makes you not died
    self.deathFrame = 0 #resets death animation
    self.setImage() #sets your image
    color = 0 #determines color of ghost
    for tile in range(len(wallMap)): #runs through and spawns all the ghosts again
      if wallMap[tile] == 2:
        ghosts.add(Ghost(color%4, tile*50))
        color += 1


pacman = Pacman() #creates pacman

winState = 1 #creates default gamestate
run = True #variable to stop the program from running
clock = pygame.time.Clock() #makes the game tick consistantly

def gameScreen(): #while game is running
  screen.fill((0, 0, 0)) #clear screen
  pacman.update() #update pacman
  list(map(lambda x:x.collide(pacman), dots)) #check all dot collisions
  walls.draw(screen) #draw walls to screen
  dots.draw(screen) #draw dots to screen
  ghosts.update() #update ghosts
  pygame.display.flip() #update screen
def winScreen(): #once you won
  screen.fill((0, 0, 0)) #clear screen
  font = pygame.font.SysFont('arial', 80, True) #create font variable
  textSprite = font.render('You Win!', True, (255, 255, 255)) #says You Win!
  textRect = textSprite.get_rect()
  textRect.center = (500, 200-textRect.height) #places text at top of screen
  textRect.y = 200 - textRect.height
  textSprite2 = font.render('Score: {}'.format(pacman.score), True, (255, 255, 255)) #shows you your score
  textRect2 = textSprite2.get_rect()
  textRect2.center = (500, 400) #places text at bottom of screen
  screen.blit(textSprite2, textRect2) #adds text to screen
  screen.blit(textSprite, textRect) #adds text to screen
  pygame.display.flip() #updates screen
def loseScreen(): #when you lose
  screen.fill((0, 0, 0)) #clear screen
  font = pygame.font.SysFont('arial', 80, True) #create font variable
  textSprite = font.render('GAME OVER', True, (180, 40, 40)) #says GAME OVER
  textRect = textSprite.get_rect()
  textRect.center = (500, 200-textRect.height) #places text at top of screen
  screen.blit(textSprite, textRect) #adds text to screen
  textSprite2 = font.render('Score: {}'.format(pacman.score), True, (255, 255, 255)) #shows you your score
  textRect2 = textSprite2.get_rect()
  textRect2.center = (500, 400) #places text at bottom of screen
  screen.blit(textSprite2, textRect2) #adds text to screen
  pygame.display.flip() #updates screen
while run: #main loop
  clock.tick(40) #keeps the game at 40fps
  for event in pygame.event.get(): #gets all events
    if event.type == pygame.QUIT: #lets you quit
      run = False
    if event.type == pygame.KEYDOWN: #when you press a key
      if event.key == pygame.K_SPACE: #debug stuff
        print(pacman.lives,'lives')
        print(winState,'win')
      if event.key == pygame.K_SPACE and pacman.died and winState == 1: #lets you restart
        pacman.start()
  if winState == 0: #runs the right screen
    loseScreen()
  elif winState == 1:
    gameScreen()
  elif winState == 2:
    winScreen()