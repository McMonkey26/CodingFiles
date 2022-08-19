import pygame, random
from switch import *
filePath = './PythonFiles/finalProject2048/'
sM = 0.3
fieldDim = 6
slow = True
pygame.init()
screen = pygame.display.set_mode((int(160*sM*fieldDim), int((160*fieldDim+105)*sM)))
screen.fill((255, 255, 255))
scoreFont = pygame.font.SysFont('Arial', int(32*sM))
numFont = pygame.font.SysFont('Arial', int(64*sM))
buttonFont = pygame.font.SysFont('Arial', int(96*sM))#(sM+1)/2))
titleFont = pygame.font.SysFont('Arial', int(128*(2*sM+1)/3))
class Game:
  mode = 'Start'
  score = 0
  best = 0
  maxField = [[]]
  def start():
    global moved, moves, field
    Game.mode = 'Playing'
    field = [['' for _ in range(fieldDim)] for _ in range(fieldDim)]
    Numbers.empty()
    Game.score = 0
    moves = 0
    moved = True
  def lose():
    global loseFrame, frame, field
    if sum([sum([x.num if x != '' else 0 for x in y]) for y in field]) >= sum([sum([x if x != '' else 0 for x in y]) for y in Game.maxField]):
      Game.maxField = [[x.num if x != '' else '' for x in y] for y in field]
      print('New Best!')
    print('Best Game:')
    print('\n'.join([str(y) for y in Game.maxField]))
    print('Score:',Game.best)
    print('Sum:',end=' ')
    print(sum([sum([x if x != '' else 0 for x in y]) for y in Game.maxField]))
    print('Current Game:')
    print('\n'.join([str([x.num if x != '' else '' for x in y]) for y in field]))
    print('Score:',Game.score)
    print('Sum:',end=' ')
    print(sum([sum([x.num if x != '' else 0 for x in y]) for y in field]))
    print(moves, 'Moves')
    loseScreen.frame = frame
    loseFrame = frame
    Game.mode = 'Lost'
  def quit():
    Game.mode = 'Start'
  def playing():
    return Game.mode == 'Playing'
  def inMenu():
    return Game.mode == 'Start'
  def lost():
    return Game.mode == 'Lost'
  def getScore():
    return Game.score
  def getBest():
    return Game.best
  def update():
    global field, frame, loseFrame
    if Game.best < Game.score:
      Game.best = Game.score
    if (not canMove(field)) and Game.playing():
      Game.lose()
class Number(pygame.sprite.Sprite):
  def __init__(self, pos, num):
    super().__init__()
    self.image = pygame.Surface((int(150*sM), int(150*sM)))
    self.image.fill(colorList3[num*5%len(colorList3)])
    self.rect = self.image.get_rect()
    self.rect.topleft = (int((pos[0]*160+5)*sM), int((pos[1]*160+110)*sM))
    self.text = numFont.render(str(num), True, (255, 255, 255))
    self.textRect = self.text.get_rect()
    self.textRect.center = (int(75*sM), int(75*sM))
    self.image.blit(self.text, self.textRect)
    self.pos = pos
    self.num = num
    self.vel = [0, 0]
    self.wasHit = False
  def move(self, event, group):
    self.wasHit = False if all([x.vel == [0,0] for x in group]) else self.wasHit
    hasRun = False
    if event.key == pygame.K_UP:
      self.vel = [0, -1]
    elif event.key == pygame.K_DOWN:
      self.vel = [0, 1]
    elif event.key == pygame.K_LEFT:
      self.vel = [-1, 0]
    elif event.key == pygame.K_RIGHT:
      self.vel = [1, 0]
    if event.key in [pygame.K_RIGHT, pygame.K_LEFT, pygame.K_UP, pygame.K_DOWN] and not (self.vel[0] + self.pos[0] in range(fieldDim) and self.vel[1] + self.pos[1] in range(fieldDim)):
      self.vel = [0, 0]
      return False
    for i in range(1 if slow else fieldDim):
      if not (self.vel[0] + self.pos[0] in range(fieldDim) and self.vel[1] + self.pos[1] in range(fieldDim)):
        self.vel = [0, 0]
        return True
      self.rect.x += int(self.vel[0]*160*sM)
      self.rect.y += int(self.vel[1]*160*sM)
      self.pos[0] += self.vel[0]
      self.pos[1] += self.vel[1]
      for hit in [x for x in pygame.sprite.spritecollide(self, group, False) if x != self]:
        if hit.num == self.num and not hit.wasHit:
          hit.num *= 2
          hit.image.fill(colorList3[hit.num*5%len(colorList3)])
          hit.text = numFont.render(str(hit.num), True, (255, 255, 255))
          hit.textRect = hit.text.get_rect()
          hit.textRect.center = (int(75*sM), int(75*sM))
          hit.image.blit(hit.text, hit.textRect)
          hit.wasHit = True
          Game.score += hit.num
          self.kill()
          return True
        else:
          self.rect.x -= int(self.vel[0]*160*sM)
          self.rect.y -= int(self.vel[1]*160*sM)
          self.pos[0] -= self.vel[0]
          self.pos[1] -= self.vel[1]
          self.vel = [0, 0]
          return hasRun
      hasRun = True
    return not self.vel == [0, 0]
  def update(self):
    if Game.playing() or Game.lost():
      screen.blit(self.image, self.rect)
    if Game.lost():
      self.image.fill(colorList3[self.num*5%len(colorList3)])
      self.image.blit(self.text, self.textRect)
      self.image.set_alpha((loseFrame - frame + 255) if (loseFrame - frame + 255) >= 90 else 90)
      screen.blit(self.image, self.rect)
class Title(pygame.sprite.Sprite):
  def __init__(self, pos, font, section, text='65536'):
    super().__init__()
    self.image = font.render(text, True, (80, 80, 80))
    self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*sM), int(self.image.get_height()*sM)))
    self.rect = self.image.get_rect()
    self.rect.topleft = pos
    self.section = section
  def update(self):
    if self.section():
      screen.blit(self.image, self.rect)
class NumBackground(pygame.sprite.Sprite):
  def __init__(self, pos):
    super().__init__()
    self.image = pygame.Surface((int(160*fieldDim*sM), int(160*fieldDim*sM)))
    self.image.fill((187, 173, 161))
    self.rect = self.image.get_rect()
    self.rect.topleft = pos
    for x in range(fieldDim):
      for y in range(fieldDim):
        tempImage = pygame.Surface((int(150*sM), int(150*sM)))
        tempImage.fill((204, 192, 180))
        self.image.blit(tempImage, (int((x*160+5)*sM), int((y*160+5)*sM)))
    self.image.set_alpha(200)
  def update(self):
    if Game.playing():
      screen.blit(self.image, self.rect)
    if Game.lost():
      self.image.set_alpha((loseFrame - frame + 255) if (loseFrame - frame + 255) >= 90 else 90)
      screen.blit(self.image, self.rect)
class StartButton(Button):
  def __init__(self, pos, size, gameMode):
    super().__init__(*pos, *size, image=(filePath+'buttonBg.png', (0, 0, 320, 160)))
    text = buttonFont.render('Start', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (int(40*fieldDim*sM), int(20*fieldDim*sM))
    self.image.blit(text, textRect)
    self.gameMode = gameMode
  def onButtonClick(self):
    if self.gameMode():
      Game.start()
  def update(self): #Runs every frame
    if self.gameMode(): #Checks if the game is on the right section
      screen.blit(self.image, self.rect) #Blits itself to the screen
class MenuButton(Button):
  def __init__(self, pos, size, gameMode):
    super().__init__(*pos, *size, image=(filePath+'buttonBg.png', (0, 0, 320, 160)))
    text = buttonFont.render('Menu', True, (255, 255, 255))
    textRect = text.get_rect()
    textRect.center = (int(40*fieldDim*sM), int(20*fieldDim*sM))
    self.image.blit(text, textRect)
    self.gameMode = gameMode
  def onButtonClick(self):
    if self.gameMode():
      Game.quit()
  def update(self): #Runs every frame
    if self.gameMode(): #Checks if the game is on the right section
      screen.blit(self.image, self.rect) #Blits itself to the screen
class ScoreText(pygame.sprite.Sprite): #Sprite to display Current/Best Score
  def __init__(self, pos, text, num, section): #Initialization function, takes in position on the screen, text to display above the score, function to get the score, and section to display on
    super().__init__() #Initializes inner Sprite class
    self.image = pygame.image.load(filePath+'scoreBg.png').convert_alpha() #Creates a curved rectangle background image
    self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*sM), int(self.image.get_height()*sM))) #Scales the image by the global size multiplier
    self.rect = self.image.get_rect(center = pos) #Sets the center of the sprite to the inputted position
    self.text = scoreFont.render(text, True, (255, 255, 255)) #Creates a Surface to display a caption for the score
    self.textRect = self.text.get_rect(center = (int(75*sM), int(20*sM))) #Sets the center of the score caption to the top of the sprite
    self.score = num #Stores the function to get the score
    self.scoreText = scoreFont.render(str(self.score()), True, (255, 255, 255)) #Creates a Surface to display the score
    self.scoreRect = self.scoreText.get_rect(center = (int(75*sM), int(60*sM))) #Sets the center of the score display to the bottom of the sprite
    self.image.blit(self.text, self.textRect) #Blits the score caption to the sprite
    self.image.blit(self.scoreText, self.scoreRect) #Blits the score to the sprite
    self.section = section #Stores the section the sprite should display on
  def update(self): #Runs every frame
    self.image = pygame.image.load(filePath+'scoreBg.png').convert_alpha() #Clears the image to a blank curved rectangle
    self.image = pygame.transform.scale(self.image, (int(self.image.get_width()*sM), int(self.image.get_height()*sM))) #Scales the image by the global size multiplier
    self.scoreText = scoreFont.render(str(self.score()), True, (255, 255, 255)) #Updates the score text Surface
    self.scoreRect = self.scoreText.get_rect(center = (int(75*sM), int(60*sM))) #Sets the center of the score text to the bottom of the sprite
    self.image.blit(self.text, self.textRect) #Blits the score caption to the sprite
    self.image.blit(self.scoreText, self.scoreRect) #Blits the score to the sprite
    if self.section(): #Checks if the game is on the right section
      screen.blit(self.image, self.rect) #Blits itself to the screen
class LoseText(pygame.sprite.Sprite): #Text sprite for the Lose screen
  def __init__(self, pos, font, section, text = 'Game Over'): #Initialization function, takes in position on the screen, font for the text, and section to display on
    super().__init__() #Initializes inner Sprite class
    self.image = font.render(text, True, (80, 80, 80)) #Creates a Surface with the text parameter
    self.rect = self.image.get_rect(center = pos) #Sets the center of the sprite to the inputted position
    self.section = section #Sets the section the text should display on
  def update(self): #Runs every frame
    if self.section(): #Checks if the game is on the right section
      screen.blit(self.image, self.rect) #Blits itself to the screen
class LoseOverlay(pygame.sprite.Sprite): #Overlay to cover the screen when you lose
  def __init__(self, pos): #Initialization function, takes in position to place on the screen
    super().__init__() #Initializes inner Sprite class
    self.image = pygame.Surface((int(160*fieldDim*sM), int(160*fieldDim*sM))) #Creates a square Surface the size of the field
    self.image.fill((237, 227, 219)) #Fills the image
    self.rect = self.image.get_rect(topleft = pos) #Sets the center of the sprite to the inputted position
  def update(self): #Runs every frame
    if Game.lost(): #Checks if the game is in the lose screen
      screen.blit(self.image, self.rect) #Blits itself to the screen
class ExampleScreen(pygame.sprite.Sprite): #Example Game animation for a better looking title screen
  def __init__(self, pos): #Initialization function, takes in position to place on the screen
    super().__init__() #Initializes inner Sprite class
    self.image = pygame.Surface((screen.get_width() // 2, screen.get_width() // 2)) #Creates a square Surface at half the width of the screen
    self.image.fill((187, 173, 161)) #Fills the image
    self.rect = self.image.get_rect(center = pos) #Sets the center of the sprite to the inputted position
    for x in range(4): #Loops through numbers 0-4, to place the example number pieces
      for y in range(4): #Loops through numbers 0-4, to place the example number pieces
        #Draws a square with the background color at the given position
        pygame.draw.rect(self.image, (204, 192, 180), pygame.Rect(x*self.image.get_width()/4, y*self.image.get_height()/4, self.image.get_width()/4, self.image.get_height()/4))
    self.frame = 0 #Specific frame counter, to loop through the example game animation
    #Field list to store the numbers on each frame of the animation
    self.sheetList = [
      [['', '', '', 2], ['', '', '', ''], ['', '', '', ''], ['', '', '', '']],
      [[2, '', '', ''], ['', '', '', ''], ['', '', '', ''], [2, '', '', '']],
      [[4, '', '', ''], ['', 2, '', ''], ['', '', '', ''], ['', '', '', '']],
      [['', '', '', ''], ['', '', '', 2], ['', '', '', ''], [4, 2, '', '']],
      [['', '', '', ''], ['', '', 2, ''], ['', '', '', ''], [4, 2, '', 2]],
      [['', '', '', 2], [2, '', '', ''], ['', '', '', ''], [4, 4, '', '']],
      [[2, '', '', ''], [2, '', 2, ''], ['', '', '', ''], [8, '', '', '']],
      [[4, '', 2, ''], [8, '', '', ''], [2, '', '', ''], ['', '', '', '']],
      [[4, 2, '', 2], [8, '', '', ''], [2, '', '', ''], ['', '', '', '']],
      [['', '', '', ''], [4, 2, '', ''], [8, '', '', ''], [2, 2, '', 2]],
      [[4, 4, '', 2], [8, '', '', ''], [2, '', '', ''], [2, '', '', '']],
      [['', '', 2, ''], [4, '', '', ''], [8, '', '', ''], [4, 4, '', 2]],
      [['', '', '', 2], [4, '', '', ''], [8, '', '', ''], [4, 4, 2, 2]],
      [['', '', '', 2], ['', '', '', 4], ['', '', '', 8], ['', 2, 8, 4]],
      [['', 2, 8, 2], [2, '', '', 4], ['', '', '', 8], ['', '', '', 4]],
      [[2, 2, 8, 2], ['', '', '', 4], [4, '', '', 8], ['', '', '', 4]],
      [[4, 8, 2, ''], [4, '', '', ''], [4, 8, '', ''], [4, '', 2, '']],
      [['', 4, 8, 2], ['', 2, '', 4], ['', '', 4, 8], ['', '', 4, 2]],
      [['', 4, 8, 2], ['', 2, 2, 4], ['', '', 4, 8], ['', '', 4, 2]],
      [[4, 8, 2, 2], [4, 4, '', ''], [4, 8, '', ''], [4, 2, '', '']],
      [['', 8, '', ''], ['', 4, 2, ''], [8, 8, '', ''], [8, 2, 2, 2]],
      [[16, 8, 4, 2], ['', 4, '', ''], ['', 8, '', ''], [2, 2, '', '']],
      [['', 8, '', ''], ['', 4, '', ''], [16, 8, '', 2], [2, 2, 4, 2]],
      [['', 8, '', ''], ['', 4, '', ''], [16, 8, 2, ''], [2, 2, 4, 4]],
      [[16, 8, 2, 4], [2, 4, 4, ''], ['', 8, '', 2], ['', 2, '', '']],
      [[16, 8, 2, 4], [2, 4, 4, 2], ['', 8, '', ''], [2, 2, '', '']],
      [[16, 8, 2, 4], [4, 4, 4, 2], [4, 8, '', ''], ['', 2, '', '']],
      [[16, 8, 2, 4], [8, 4, 2, ''], [4, 8, '', ''], [2, '', '', 2]],
      [[16, '', 2, ''], [8, 8, '', ''], [4, 4, '', 4], [2, 8, 4, 2]],
      [[16, '', '', 2], [8, 8, '', ''], [4, 4, 2, 4], [2, 8, 4, 2]],
      [[16, 2, '', ''], [16, '', '', ''], [8, 2, 4, 2], [2, 8, 4, 2]],
      [[32, 4, 8, 4], [8, 8, '', ''], [2, '', '', 2], ['', '', '', '']],
      [[32, 4, 8, 4], [8, 8, '', 2], [2, '', '', ''], [2, '', '', '']],
      [[32, 4, 8, 4], ['', '', 16, 2], ['', 2, '', 2], ['', '', '', 2]],
      [[32, 4, 8, 4], ['', '', 16, 2], ['', '', '', 4], ['', '', 2, 2]],
      [['', '', '', 4], ['', 2, 8, 2], ['', '', 16, 4], [32, 4, 2, 2]],
      [[4, '', '', ''], [2, 8, 2, ''], [16, 4, '', ''], [32, 4, 4, 4]],
      [[4, 8, 2, 4], [2, 8, 4, 2], [16, '', '', ''], [32, '', '', '']],
      [[4, 16, 2, 4], [2, '', 4, 2], [16, '', '', ''], [32, '', '', 2]],
      [[4, '', '', 2], [2, '', '', ''], [16, '', 2, 4], [32, 16, 4, 4]],
      [[4, '', '', ''], [2, '', '', ''], [16, 2, 2, 2], [32, 16, 4, 8]],
      [[4, 2, 2, 2], [2, 16, 4, 8], [16, '', 2, ''], [32, '', '', '']],
      [['', 4, 2, 4], [2, 16, 4, 8], ['', 2, 16, 2], ['', '', '', 32]],
      [['', '', 2, 4], ['', 4, 2, 8], ['', 16, 4, 2], [2, 2, 16, 32]],
      [[2, 4, 4, 4], ['', 16, 4, 8], [2, 2, 16, 2], ['', '', '', 32]],
      [['', 2, 4, 8], ['', 16, 4, 8], ['', 4, 16, 2], [2, '', '', 32]],
      [['', 2, '', ''], ['', 2, '', 16], ['', 16, 8, 2], [2, 4, 16, 32]],
      [[2, 4, 8, 16], [2, 16, 16, 2], ['', 4, '', 32], ['', '', '', '']],
      [[4, 4, 8, 16], ['', 16, 16, 2], ['', 4, '', 32], ['', '', 2, '']],
      [[8, 8, 16, ''], [32, 2, '', ''], [4, 32, '', 2], [2, '', '', '']],
      [[8, '', '', 2], [32, 8, '', ''], [4, 2, '', ''], [2, 32, 16, 2]],
      [[8, 2, '', 4], [32, 8, '', ''], [4, 2, '', ''], [2, 32, 16, 2]],
      [[8, 2, '', ''], [32, 8, '', ''], [4, 2, 2, 4], [2, 32, 16, 2]],
      [[2, '', 8, 2], ['', '', 32, 8], ['', 4, 4, 4], [2, 32, 16, 2]],
      [['', 2, 8, 2], ['', '', 32, 8], [2, '', 4, 8], [2, 32, 16, 2]],
      [['', 2, 8, 2], ['', 2, 32, 8], ['', 2, 4, 8], [2, 32, 16, 2]],
      [[2, 8, 2, 2], [2, 32, 8, ''], [2, 4, 8, ''], [2, 32, 16, 2]],
      [['', 8, '', ''], ['', 32, 2, 2], [4, 4, 16, ''], [4, 32, 16, 4]],
      [['', '', 2, 8], ['', '', 32, 4], ['', '', 8, 16], [4, 32, 16, 4]],
      [[2, 8, '', ''], [32, 4, '', 2], [8, 16, '', ''], [4, 32, 16, 4]],
      [[2, 8, '', ''], [32, 4, 2, ''], [8, 16, 2, ''], [4, 32, 16, 4]],
      [[2, 8, 4, 4], [32, 4, 16, ''], [8, 16, '', ''], [4, 32, '', 2]],
      [['', 2, 8, 8], ['', 32, 4, 16], [2, '', 8, 16], ['', 4, 32, 2]],
      [['', 2, 2, 16], ['', 32, 4, 16], ['', 2, 8, 16], ['', 4, 32, 2]],
      [['', 2, 2, ''], ['', 32, 4, 16], [2, 2, 8, 32], ['', 4, 32, 2]],
      [[2, 2, 2, 16], ['', 32, 4, 32], ['', 2, 8, 2], [2, 4, 32, '']],
      [['', 2, 4, 16], ['', 32, 4, 32], [4, 2, 8, 2], ['', 2, 4, 32]],
      [[2, 4, 16, ''], [32, 4, 32, ''], [4, 2, 8, 2], [2, 4, 32, 2]],
      [['', 2, 4, 16], [2, 32, 4, 32], [4, 2, 8, 2], [2, 4, 32, 2]],
      [['', 2, '', 2], [2, 32, 8, 16], [4, 2, 8, 32], [2, 4, 32, 4]],
      [[2, 2, 16, 2], [4, 32, 32, 16], [2, 2, '', 32], [4, 4, '', 4]],
      [[4, 16, 2, ''], [4, 64, 16, ''], [4, 32, '', ''], [8, 4, 2, '']],
      [['', 4, 16, 2], ['', 4, 64, 16], ['', 2, 4, 32], ['', 8, 4, 2]],
      [[2, '', '', 2], ['', 8, 16, 16], ['', 2, 64, 32], ['', 8, 8, 2]],
      [[4, '', 2, ''], [8, 32, '', ''], [2, 64, 32, ''], [16, 2, '', '']],
      [[4, '', '', 2], [8, 32, '', ''], [2, 64, 2, ''], [16, 2, 32, '']],
      [[4, 2, '', 2], [8, 32, '', ''], [2, 64, 2, ''], [16, 2, 32, '']],
      [[4, 2, '', ''], [8, 32, '', 2], [2, 64, 2, ''], [16, 2, 32, 2]],
      [[4, 2, 2, ''], [8, 32, 2, ''], [2, 64, 2, ''], [16, 2, 32, 2]],
      [[4, 2, '', ''], [8, 32, 2, 2], [2, 64, 4, ''], [16, 2, 32, 2]],
      [[4, 2, '', 2], [8, 32, 2, ''], [2, 64, 4, ''], [16, 2, 32, 4]],
      [[4, 2, 2, 2], [8, 32, 4, 4], [2, 64, 32, ''], [16, 2, '', 2]],
      [[4, 2, 2, 2], [8, 32, 4, 4], [2, 64, 32, 2], [16, 2, 2, '']],
      [[4, 2, 2, 2], [8, 32, 4, 2], [2, 64, 32, 4], [16, 2, 2, 2]],
      [[4, 2, 2, 2], [8, 32, 4, 4], [2, 64, 32, 4], [16, 2, 2, 2]],
      [[4, 2, 2, 2], [8, 32, 4, 8], [2, 64, 32, 2], [16, 2, 2, 2]],
      [[4, 4, 2, 2], [8, 32, 4, 8], [2, 64, 32, 2], [16, 4, 2, '']],
      [[8, 4, '', ''], [8, 32, 4, 8], [2, 64, 32, 2], [16, 4, 2, 2]],
      [[16, 4, 4, 8], [2, 32, 32, 4], [16, 64, 2, ''], ['', 4, '', 2]],
      [['', 16, 8, 8], [2, 2, 64, 4], ['', 16, 64, 2], ['', '', 4, 2]],
      [['', '', '', ''], ['', 16, 8, 8], [4, 2, 128, 4], [2, 16, 4, 4]],
      [['', '', '', ''], ['', '', 16, 16], [4, 2, 128, 4], [2, 2, 16, 8]],
      [['', '', 4, ''], [32, '', '', ''], [4, 2, 128, 4], [4, 16, 8, '']],
      [[32, 2, 4, 4], [8, 16, 128, ''], ['', '', 8, ''], [2, '', '', '']],
      [[2, '', '', ''], [32, '', 4, ''], [8, 2, 128, ''], [2, 16, 8, 4]],
      [['', '', '', 2], ['', 2, 32, 4], ['', 8, 2, 128], [2, 16, 8, 4]],
      [[2, 2, 32, 2], ['', 8, 2, 4], ['', 16, 8, 128], ['', '', 2, 4]],
      [[4, 32, 2, ''], [8, 2, 4, ''], [16, 8, 128, 2], [2, 4, '', '']],
      [[2, 4, 32, 2], ['', 8, 2, 4], [16, 8, 128, 2], ['', '', 2, 4]],
      [[2, 4, 32, 2], [16, 16, 2, 4], [2, '', 128, 2], ['', '', 2, 4]],
      [[2, '', 32, 2], [2, '', 2, 4], [16, 4, 128, 2], [2, 16, 2, 4]],
      [['', '', 32, 2], [4, 2, 2, 4], [16, 4, 128, 2], [2, 16, 2, 4]],
      [[4, 2, 32, 2], [16, 4, 2, 4], [2, 16, 128, 2], [4, '', 2, 4]],
      [[4, 2, 32, 2], [16, 2, 2, 4], [2, 4, 128, 2], [4, 16, 2, 4]],
      [[4, 4, 32, 2], [16, 4, 2, 4], [2, 16, 128, 2], [4, 4, 2, 4]],
      [[2, 8, 32, 2], [16, 4, 2, 4], [2, 16, 128, 2], ['', 8, 2, 4]],
      [[4, 8, 32, 2], [2, 4, 2, 4], [16, 16, 128, 2], [2, 8, 2, 4]],
      [[4, 8, 32, 2], [2, 4, 2, 4], [2, 32, 128, 2], [2, 8, 2, 4]],
      [[4, 8, 32, 2], [4, 4, 2, 4], [2, 32, 128, 2], [2, 8, 2, 4]],
      [['', 8, 32, 2], [4, 4, 2, 4], [8, 32, 128, 2], [4, 8, 2, 4]],
      [[4, 8, 32, 2], [8, 4, 2, 4], [4, 32, 128, 2], [4, 8, 2, 4]],
      [[2, 8, 32, 2], [4, 4, 2, 4], [8, 32, 128, 2], [8, 8, 2, 4]],
      [[2, 8, 32, 2], [8, 2, 4, ''], [8, 32, 128, 2], [16, 2, 4, 2]],
      [['', 8, 32, 2], [2, 2, 4, ''], [16, 32, 128, 2], [16, 2, 4, 4]],
      [[8, 32, 2, ''], [4, 4, '', ''], [16, 32, 128, 2], [16, 2, 8, 2]],
      [['', 8, 32, 2], [2, '', '', 8], [16, 32, 128, 2], [16, 2, 8, 2]],
      [[2, 8, 32, 2], [32, 32, 128, 8], ['', 2, 8, 4], ['', 2, '', '']],
      [[2, 8, 32, 2], [32, 32, 128, 8], [2, 4, 8, 4], ['', '', '', '']],
      [[2, 8, 32, 2], [64, 128, 8, ''], [2, 4, 8, 4], [2, '', '', '']],
      [[2, 8, 32, 2], ['', 64, 128, 8], [2, 4, 8, 4], ['', 2, '', 2]],
      [[2, 8, 32, 2], [64, 128, 8, ''], [2, 4, 8, 4], [4, 2, '', '']],
      [[2, 8, 2, ''], [64, 128, '', ''], [2, 4, 32, 2], [4, 2, 16, 4]],
      [['', 2, 8, 2], [2, '', 64, 128], [2, 4, 32, 2], [4, 2, 16, 4]],
      [['', 2, 8, 2], [2, 2, 64, 128], [2, 4, 32, 2], [4, 2, 16, 4]],
      [[4, 4, 8, 2], [4, 4, 64, 128], ['', 2, 32, 2], [2, '', 16, 4]],
      [['', 2, 8, 2], ['', '', 64, 128], [8, 8, 32, 2], [2, 2, 16, 4]],
      [[8, 2, 8, 2], [2, 8, 64, 128], ['', 2, 32, 2], [2, '', 16, 4]],
      [[4, '', 8, 2], ['', 2, 64, 128], [8, 8, 32, 2], [4, 2, 16, 4]],
      [['', 4, 8, 2], [2, 2, 64, 128], ['', 16, 32, 2], [4, 2, 16, 4]],
      [[2, 4, 8, 2], ['', 2, 64, 128], [2, 16, 32, 2], [4, 2, 16, 4]],
      [[2, 4, 8, 2], ['', 2, 64, 128], [4, 16, 32, 2], [4, 2, 16, 4]],
      [['', 4, 8, 2], [2, 2, 64, 128], [2, 16, 32, 2], [8, 2, 16, 4]],
      [[4, 4, 8, 2], [8, 2, 64, 128], ['', 16, 32, 2], [2, 2, 16, 4]],
      [[4, 4, 8, 2], [8, 2, 64, 128], [2, 16, 32, 2], [2, 2, 16, 4]]
    ]
  def update(self): #Runs every frame
    self.image.fill((187, 173, 161)) #Blanks out the image
    self.frame += 1 #Increments the frame counter
    for x in range(4): #Loops through numbers 0-4, to place the example number pieces
      for y in range(4): #Loops through numbers 0-4, to place the example number pieces
        #Draws a square with the background color, or the specific number's color, at the given position
        pygame.draw.rect(self.image, (204, 192, 180) if self.sheetList[(self.frame//8)%len(self.sheetList)][y][x] == '' else colorList3[self.sheetList[(self.frame//8)%len(self.sheetList)][y][x] * 5 % len(colorList3)], pygame.Rect(x*self.image.get_width()/4, y*self.image.get_height()/4, self.image.get_width()/4, self.image.get_height()/4))
    if Game.inMenu(): #Checks if the game is in the menu
      screen.blit(self.image, self.rect) #Blits itself to the screens
class ArrowDisplay(pygame.sprite.Sprite):
  def __init__(self, pos, section, anim):
    super().__init__()
    self.image = pygame.Surface((96, 64))
    self.image.blit(self.getImage(pygame.K_UP), (32, 0))
    self.image.blit(self.getImage(pygame.K_DOWN), (32, 32))
    self.image.blit(self.getImage(pygame.K_LEFT), (0, 32))
    self.image.blit(self.getImage(pygame.K_RIGHT), (64, 32))
    self.image = pygame.transform.scale(self.image, (36*sM*fieldDim, 24*sM*fieldDim)).convert_alpha()
    self.rect = self.image.get_rect(center = pos)
    self.direcList = [
      {'u': False, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': False, 'l': True, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': False, 'l': False, 'r': True},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': False, 'd': True, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False},
      {'u': True, 'd': False, 'l': False, 'r': False}
    ]
    self.frame = 0
    self.anim = anim
    self.section = section
  def getImage(self, direc, pressed=False):
    image = pygame.Surface((32, 32))
    imPos = [0, 0, 32, 32]
    switch(direc)
    if case(pygame.K_UP): imPos[0] = 0
    elif case(pygame.K_DOWN): imPos[0] = 32
    elif case(pygame.K_LEFT): imPos[0] = 64
    elif case(pygame.K_RIGHT): imPos[0] = 96
    imPos[1] = 32 if pressed else 0
    image.blit(pygame.image.load(filePath+'arrowPics.png'), (0, 0), imPos)
    return image
  def setImage(self, anim):
    self.image = pygame.Surface((96, 64))
    if anim:
      self.image.blit(self.getImage(pygame.K_UP, self.direcList[self.frame//8]['u']), (32, 0))
      self.image.blit(self.getImage(pygame.K_DOWN, self.direcList[self.frame//8]['d']), (32, 32))
      self.image.blit(self.getImage(pygame.K_LEFT, self.direcList[self.frame//8]['l']), (0, 32))
      self.image.blit(self.getImage(pygame.K_RIGHT, self.direcList[self.frame//8]['r']), (64, 32))
    else:
      key = pygame.key.get_pressed()
      self.image.blit(self.getImage(pygame.K_UP, key[pygame.K_UP]), (32, 0))
      self.image.blit(self.getImage(pygame.K_DOWN, key[pygame.K_DOWN]), (32, 32))
      self.image.blit(self.getImage(pygame.K_LEFT, key[pygame.K_LEFT]), (0, 32))
      self.image.blit(self.getImage(pygame.K_RIGHT, key[pygame.K_RIGHT]), (64, 32))
    self.image = pygame.transform.scale(self.image, (36*sM*fieldDim, 24*sM*fieldDim)).convert_alpha()
  def update(self):
    self.frame += 1
    self.frame = self.frame % (8*len(self.direcList))
    self.setImage(self.anim)
    if self.section():
      screen.blit(self.image, self.rect)
class DimSlider(Slider): #Slider to control field dimensions
  def __init__(self, x, y, width, height, section, min=4, max=12, margin=5, thickness=5, value=fieldDim, bg=(180, 180, 180), mg=(255, 255, 255), fg=(0, 0, 0), int=True):
    #Takes in position, size, and section to display on, with default values for more readability later on in the code, while allowing modifications for testing
    #Initializes inner Slider class
    super().__init__(x, y, width, height, min=min, max=max, margin=margin, thickness=thickness, value=value, bg=bg, mg=mg, fg=fg, int=int)
    self.section = section #Sets the section the slider should display on
  def onRelease(self): #Runs when the user releases click on the slider
    global screen, fieldDim, field #Global variables to reset screen/field
    fieldDim = self.getValue() #Sets the new field dimension to the slider's value
    #Sets the new size of the screen based on the new field dimension
    screen = pygame.display.set_mode((int(160*sM*fieldDim), int((160*fieldDim+105)*sM)))
    #Sets the new size of the field based on the new field dimension
    field = [['' for _ in range(fieldDim)] for _ in range(fieldDim)]
    for group in spriteGroups: #Iterates through every group
      group.empty() #Clears the group
    createObjects() #Fills the groups with all of the static sprites
  def update(self): #Runs every frame
    if self.section(): #Checks if the game is on the right section
      screen.blit(self.image, self.rect) #Blits itself to the screen
class SizeSlider(Slider): #Slider to control size multiplier
  def __init__(self, x, y, width, height, section, min=0.0001, max=1, margin=5, thickness=5, value=sM, bg=(180, 180, 180), mg=(255, 255, 255), fg=(0, 0, 0), int=False):
    #Takes in position, size, and section to display on, with default values for more readability later  on in the code, while allowing modifications for testing
    #Initializes inner Slider class
    super().__init__(x, y, width, height, min=min, max=max, margin=margin, thickness=thickness, value=value, bg=bg, mg=mg, fg=fg, int=int)
    self.section = section #Sets the section the slider should display on
  def onRelease(self): #Runs when the user releases click on the slider
    global screen, sM #Global variables to reset screen
    sM = self.getValue() #Sets the new size multiplier to the slider's value
    #Sets the new size of the screen based on the new size multiplier
    screen = pygame.display.set_mode((int(160*sM*fieldDim), int((160*fieldDim+105)*sM)))
    for group in spriteGroups: #Iterates through every group
      group.empty() #Clears the group
    createObjects() #Fills the groups with all of the static sprites
  def update(self): #Runs every frame
    if self.section(): #Checks if the game is on the right section
      screen.blit(self.image, self.rect) #Blits itself to the screen
class TempEvent: #Class to check instead of a pygame event
  key = 0 #Default key variable, keeps other functions from weird behaviors or throwing errors
  def __init__(self, tempKey): #Allows the automatic mode to create its own 'events'
    self.key = tempKey #Stores the inputted key, so other functions can check it later
Numbers = pygame.sprite.Group() #Sprite group to organize display order
Displays = pygame.sprite.Group() #Sprite group to organize display order
ScoreDisplays = pygame.sprite.Group() #Sprite group to organize display order
Overlays = pygame.sprite.Group() #Sprite group to organize display order
spriteGroups = [Numbers, Displays, ScoreDisplays, Overlays, libObjects] #Stores all sprite groups, to iterate through later
def createObjects(): #Resets all sprites in the program
  # global field, scoreFont, numFont, buttonFont, titleFont, loseScreen #Global variables to control fonts and field
  global field, scoreFont, numFont, buttonFont, titleFont, loseScreen #Global variables to control fonts and field
  scoreFont = pygame.font.SysFont('Arial', int(32*sM)) #Sets the font size for Score text
  numFont = pygame.font.SysFont('Arial', int(64*sM)) #Sets the font size for Number text
  buttonFont = pygame.font.SysFont('Arial', int(96*sM)) #Sets the font size for Button text
  titleFont = pygame.font.SysFont('Arial', int(128*(2*sM+1)/3)) #Sets the font size for Title text
  libObjects.add(DimSlider(20*sM*fieldDim, 150*sM*fieldDim+10, 120*sM*fieldDim, 8*sM*fieldDim, Game.inMenu, value=fieldDim)) #Adds a slider to control the field dimensions to the libObjects group
  libObjects.add(SizeSlider(20*sM*fieldDim, 160*sM*fieldDim+10, 120*sM*fieldDim, 8*sM*fieldDim, Game.inMenu, value=sM)) #Adds a slider to control the size multiplier to the libObjects group
  libObjects.add(StartButton((int(40*fieldDim*sM), int(110*fieldDim*sM)), (int(80*fieldDim*sM), int(40*fieldDim*sM)), Game.inMenu)) #Adds a Start button to the libObjects group
  libObjects.add(StartButton((int(40*fieldDim*sM), int(110*fieldDim*sM)), (int(80*fieldDim*sM), int(40*fieldDim*sM)), Game.lost)) #Adds a Start button to the libObjects group
  libObjects.add(MenuButton((int(40*fieldDim*sM), int(60*fieldDim*sM)), (int(80*fieldDim*sM), int(40*fieldDim*sM)), Game.lost)) #Adds a Menu button to the libObjects group
  Displays.add(Title((int(16*sM), int(8*sM)), titleFont, Game.inMenu)) #Adds a Title text sprite to the Displays group
  Displays.add(Title((int(16*sM), 0), titleFont, Game.playing)) #Adds a Title text sprite to the Displays group
  Displays.add(LoseText((int(screen.get_width()/2), 50*sM), buttonFont, Game.lost)) #Adds a Lose text sprite to the Displays group
  Displays.add(NumBackground((0, int(105*sM)))) #Adds a background screen to the Displays group
  Displays.add(ExampleScreen((int(80*sM*fieldDim), int(70*sM*fieldDim)))) #Adds an example game animation to the Displays group
  Displays.add(ArrowDisplay((int(140*sM*fieldDim), int(90*sM*fieldDim)), Game.inMenu, True)) #Adds an arrow key display to the Displays group
  # Displays.add(ArrowDisplay((int(140*sM*fieldDim), int(90*sM*fieldDim)), Game.playing, False)) #Adds an arrow key display to the Displays group
  loseScreen = LoseOverlay((0, int(105*sM))) #Creates a lose screen overlay
  Overlays.add(loseScreen) #Adds the lose screen overlay to the Overlays group
  ScoreDisplays.add(ScoreText((int((100*fieldDim)*sM), int(50*sM)), 'Score', Game.getScore, Game.playing)) #Adds a Current Score display to the ScoreDisplays group
  ScoreDisplays.add(ScoreText((int((140*fieldDim)*sM), int(50*sM)), 'Best', Game.getBest, Game.playing)) #Adds a Best Score display to the ScoreDisplays group
  field = [['' for _ in range(fieldDim)] for _ in range(fieldDim)] #Creates a 2d list of strings, with the same dimensions as the board, to store each sprite in order
def canMoveUp(field, pos0, pos1): #Determines if a given position in the field can move [direc]
  try: #Prevents an AttributeError from checking a string
    num = field[pos0][pos1].num #Stores the given position's value to check later
  except AttributeError: #If the given position is a string, returns False
    return False
  if pos0 >= 1: #Makes sure the position is not on the [direc] side of the list
    if field[pos0-1][pos1] == '': return True #Returns true if the value to the [direc] of the current position is a string
    if field[pos0-1][pos1].num == num: return True #Returns true if the value to the [direc] of the current position has the same value as the current position
  return False #Otherwise, returns False
def canMoveDown(field, pos0, pos1): #Determines if a given position in the field can move [direc]
  try: #Prevents an AttributeError from checking a string
    num = field[pos0][pos1].num #Stores the given position's value to check later
  except AttributeError: #If the given position is a string, returns False
    return False
  if pos0 <= len(field)-2: #Makes sure the position is not on the [direc] side of the list
    if field[pos0+1][pos1] == '': return True #Returns true if the value to the [direc] of the current position is a string
    if field[pos0+1][pos1].num == num: return True #Returns true if the value to the [direc] of the current position has the same value as the current position
  return False #Otherwise, returns False
def canMoveLeft(field, pos0, pos1): #Determines if a given position in the field can move [direc]
  try: #Prevents an AttributeError from checking a string
    num = field[pos0][pos1].num #Stores the given position's value to check later
  except AttributeError: #If the given position is a string, returns False
    return False
  if pos1 >= 1: #Makes sure the position is not on the [direc] side of the list
    if field[pos0][pos1-1] == '': return True #Returns true if the value to the [direc] of the current position is a string
    if field[pos0][pos1-1].num == num: return True #Returns true if the value to the [direc] of the current position has the same value as the current position
  return False #Otherwise, returns False
def canMoveRight(field, pos0, pos1): #Determines if a given position in the field can move right
  try: #Preventsan Attribute error from checking a string
    num = field[pos0][pos1].num #Stores the given position's value to check later
  except AttributeError: #If the given position is a string, returns False
    return False
  if pos1 <= len(field[pos0])-2: #Makes sure the position is not on the right side of the list
    if field[pos0][pos1+1] == '': return True #Returns true if the value to the right of the current position is a string
    if field[pos0][pos1+1].num == num: return True #Returns true if the value to the right of the current position has the same value as the current position
  return False #Otherwise, returns False
def canMove(field, direct=None): #Determines if the field can move in a given direction, or if it can move at all
  if direct == 'u': return any([any([canMoveUp(field, i, j) for j in range(len(field[i]))]) for i in range(len(field))]) #Checks if any index in the field can move up using list comprehension
  elif direct == 'd': return any([any([canMoveDown(field, i, j) for j in range(len(field[i]))]) for i in range(len(field))]) #Checks if any index in the field can move down using list comprehension
  elif direct == 'l': return any([any([canMoveLeft(field, i, j) for j in range(len(field[i]))]) for i in range(len(field))]) #Checks if any index in the field can move left using list comprehension
  elif direct == 'r': return any([any([canMoveRight(field, i, j) for j in range(len(field[i]))]) for i in range(len(field))]) #Checks if any index in the field can move right using list comprehension
  else: return any([any([any([canMoveUp(*(args:=(field, i, j))), canMoveDown(*args), canMoveLeft(*args), canMoveRight(*args)]) for j in range(len(field[i]))]) for i in range(len(field))])
createObjects() #Creates all the static sprites and adds them to their respective groups
run = True #Conditional to toggle the Game Loop
moved = True #Stores whether or not the player has moved
clock = pygame.time.Clock() #Used for keeping a consistent 30 fps when on slow mode
x, y = 1, 1 #Stores the order each dimension of the field list will loop through
frame = 0 #Stores the current frame
moves = 0 #Stores the amount of successful moves in each game
shouldAuto = False #Stores whether or not the game should run automatically
#List of colors, sorted by hue
colorList3 = [[[255, i, 0], [255-i, 255, 0], [0, 255, i], [0, 255-i, 255], [i, 0, 255], [255, 0, 255-i]][j] for j in range(6) for i in range(255)]
while run: #Game Loop
  if slow: clock.tick(30) #If the game is running on slow mode, keeps the game at 30 fps
  frame += 1 #Increments a frame counter
  moveDirec = TempEvent #Sets the movement direction to a placeholder int, to make sure pieces don't move when the user isn't pressing a key
  if frame% 100000 == 0: #Runs every 100k frames, used to keep track of the board when a large field is running on auto over long periods of time
    print('frame',frame,moves,'moves') #Prints out the current frame, and how many moves have happened
    print('field =', ',\n'.join([str([x.num if x != '' else x for x in sprite]) for sprite in field])) #Prints out the field
  for event in pygame.event.get(): #Event Loop
    if event.type == pygame.QUIT: #When the user clicks the (X) Button
      run = False #Toggles the Game Loop conditional, to quit out of the loop after this frame
      print('field =',[[x.num if not type(x) == type('string') else x for x in sprite] for sprite in field]) #Prints out the final field
      print('frame',frame,moves,'moves') #Prints the current frame and the final game's move counter
    libObjects.event(event) #Updates the imported group
    if event.type == pygame.KEYDOWN: #Debug keybinds to allow me to switch between:
      if event.key == pygame.K_i: Game.quit() #Going to menu
      if event.key == pygame.K_o: Game.start() #Going to the game screen
      if event.key == pygame.K_p: Game.lose() #Going to the lose screen
      #Without needing to worry about playing for trillions of years
    if event.type == pygame.KEYDOWN and Game.playing(): #In-Game Keybinds
      if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT] and all([x.vel == [0, 0] for x in Numbers]): #Checks if you're trying to move, and every piece is stopped
        moveDirec = event #sets the move direction variable to the movement event
        if event.key == pygame.K_UP: x, y = 1, 1 #Sets the order the field will loop through to update each piece
        elif event.key == pygame.K_DOWN: x, y = -1, 1 #Sets the order the field will loop through to update each piece
        elif event.key == pygame.K_LEFT: x, y = 1, 1 #Sets the order the field will loop through to update each piece
        elif event.key == pygame.K_RIGHT: x, y = 1, -1 #Sets the order the field will loop through to update each piece
      elif event.key == pygame.K_w: #Debug keybind to make sure movement direction functions are working correctly
        #Loops through each direction checking function using list comprehension, and prints a string of every direction the field can move
        print(''.join(['udlr'[i] for i in range(4) if [canMove(field, 'u'), canMove(field, 'd'), canMove(field, 'l'), canMove(field, 'r')][i]]))
      elif event.key == pygame.K_SPACE: #Debug/auto toggle
        #if you press shift+space, it prints out the field
        if event.mod & pygame.KMOD_SHIFT:
          field = [
            ['' for i in range(6)],
            ['' for i in range(6)],
            ['' for i in range(6)],
            ['' for i in range(6)],
            ['' for i in range(6)],
            ['' for i in range(6)]
          ]
          field[(pos1:=random.randint(0,5))][(pos0:=random.randint(0,5))] = Number([pos0, pos1], 2 if random.random() < 0.9 else 4)
          Numbers.empty()
          for layer in field:
            for sprite in layer:
              if sprite != '':
                Numbers.add(sprite)
          slow = not slow
          print('field =',[[x.num if not x == '' else x for x in sprite] for sprite in field])
        #if you just press space, it toggles automatic movement
        else: shouldAuto = not shouldAuto
      elif event.key == pygame.K_ESCAPE: #if you press escape
        Game.lose() #Sends the game through the lose sequence
  if Game.playing(): #Segment for anything that should only run while the game is playing, not in menu or in the lose screen
    #Automatic Play: Checks if the game is on a frame it should move, checks if every piece is stopped, and checks if automatic mode is toggled on
    if frame % (5 if slow else 1) == 0 and all([x.vel == [0, 0] for x in Numbers]) and shouldAuto:
      #Creates a list of every direction the field can currently move, plus a placeholder value to prevent the random selector from throwing an error
      moveDirecs = [[pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, 0][i] for i in range(5) if [canMove(field, 'u'), canMove(field, 'd'), canMove(field, 'l'), canMove(field, 'r'), not canMove(field)][i]]
      #Selects a random direction from the list of possible directions
      moveDirec = TempEvent(random.choice(moveDirecs))
      if moveDirec.key == pygame.K_UP: x, y = 1, 1 #Sets the order the field will loop through to update each piece
      elif moveDirec.key == pygame.K_DOWN: x, y = -1, 1 #Sets the order the field will loop through to update each piece
      elif moveDirec.key == pygame.K_LEFT: x, y = 1, 1 #Sets the order the field will loop through to update each piece
      elif moveDirec.key == pygame.K_RIGHT: x, y = 1, -1 #Sets the order the field will loop through to update each piece
    for layer in field[::x]: #Loops through the field in the order the previous segments set
      for sprite in layer[::y]: #Loops through each line on the field in the order the previous segments set
        if sprite == '': continue #Skips to the next value in the loop if the current value is a placeholder string, to prevent attribute errors
        if sprite.move(moveDirec, Numbers): moved = True #Moves the selected piece in the selected direction, and sets a variable to store if any piece moved this frame
    field = [['' for _ in range(fieldDim)] for _ in range(fieldDim)] #Clears the field list, to prevent repeated values
    for sprite in Numbers: field[sprite.pos[1]][sprite.pos[0]] = sprite #Places each piece into its position in the field
    if moved and all([x.vel == [0, 0] for x in Numbers]): #Checks if the player has successfully moved, and that every piece has since stopped moving
      # if not any('' in x for x in field): break #Previously, this determined losing the game, and would quit the program
      moves += 1 #Increments a movement counter, for diagnostics, or if it's just something you find interesting
      pos0 = random.randrange(0, fieldDim) #Picks a random index on the field list
      pos1 = random.randrange(0, fieldDim) #Picks a random index on the field list
      while field[pos1][pos0] != '': #Ensures the randomly picked position is empty
        pos0 = random.randrange(0, fieldDim) #Picks a new random index on the field list
        pos1 = random.randrange(0, fieldDim) #Picks a new random index on the field list
      if random.random() >= 0.9: #Random check, with a 10% chance to return true
        field[pos1][pos0] = Number([pos0, pos1], 4) #Sets the random index on the field to a 4
      else: #90% Chance to occur
        field[pos1][pos0] = Number([pos0, pos1], 2) #Sets the random index on the field to a 2
      Numbers.add(field[pos1][pos0]) #Adds the piece that was just spawned to the Number group
      moved = False #Stops the program from creating new pieces until the player moves again
  screen.fill(colorList3[frame%len(colorList3)]) #Fills the screen with an RGB value from colorList3 by frame
  Game.update() #Updates the Game class
  Overlays.update() #Updates/draws the Overlay sprites
  Displays.update() #Updates/draws the Display sprites
  ScoreDisplays.update() #Updates/draws the ScoreDisplay sprites
  Numbers.update() #Updates/draws the Number sprites
  libObjects.update() #Updates/draws the sprites created from my library (Sliders/Buttons)
  pygame.display.flip() #Displays the new screen to the user