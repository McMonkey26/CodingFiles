import pygame
from switch import *

pygame.init()
screen = pygame.display.set_mode((640, 640))

board = [
    ['r','n','b','k','q','b','n','r'],
    ['p','p','p','p','p','p','p','p'],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    [' ',' ',' ',' ',' ',' ',' ',' '],
    ['P','P','P','P','P','P','P','P'],
    ['R','N','B','K','Q','B','N','R']
]
linePrint('hello', end='|\n')
class ChessPiece(Button):
  def __init__(self, piece, pos, team):
    super().__init__(*pos, 60, 60, image=('PythonFiles/chess/'+piece+team.capitalize()+'.png', (0, 0, 60, 60)))
    self.rect.center = (pos[0]*80+40, (7-pos[1])*80+40)
    self.type = piece
    self.x = pos[0]
    self.y = pos[1]
    self.pos = pos
    self.team = team
  def canMove(self):
    checks = lambda x:x[0] <= 7 and x[0] >= 0 and x[1] <= 7 and x[1] >= 0 and x not in [(p.x, p.y) for p in pieces]
    switch(self.type)
    possMoves = []
    if case('rook'):
      for x in range(1, self.x+1):
        if checks((self.x-x, self.y)): possMoves.append((self.x-x, self.y))
        else: break
      for x in range(self.x+1, 8):
        if checks((x, self.y)): possMoves.append((x, self.y))
        else: break
      for y in range(1, self.y+1):
        if checks((self.x, self.y-y)): possMoves.append((self.x, self.y-y))
        else: break
      for y in range(self.y+1, 8):
        if checks((self.x, y)): possMoves.append((self.x, y))
        else: break
    elif case('knight'):
      return [x for x in [(self.x-2,self.y-1), (self.x-1,self.y-2), (self.x+1,self.y-2), (self.x+2,self.y-1), (self.x+2,self.y+1), (self.x+1,self.y+2), (self.x-1,self.y+2), (self.x-2,self.y+1)] if checks(x)]
    elif case('bishop'):
      for x in range(1, min((self.x+1, 8-self.y))):
        if checks((self.x-x, self.y+x)): possMoves.append((self.x-x, self.y+x))
        else: break
      for x in range(1, min((8-self.x, 8-self.y))):
        if checks((self.x+x, self.y+x)): possMoves.append((self.x+x, self.y+x))
        else: break
      for x in range(1, min((self.x+1, self.y+1))):
        if checks((self.x-x, self.y-x)): possMoves.append((self.x-x, self.y-x))
        else: break
      for x in range(1, min((8-self.x, self.y+1))):
        if checks((self.x+x, self.y-x)): possMoves.append((self.x+x, self.y-x))
        else: break
    elif case('king'):
      return [x for x in [(x, y) for x in [self.x-1, self.x, self.x+1] for y in [self.y-1, self.y, self.y+1]] if checks(x)]
    elif case('queen'):
      for x in range(1, self.x+1):
        if checks((self.x-x, self.y)): possMoves.append((self.x-x, self.y))
        else: break
      for x in range(self.x+1, 8):
        if checks((x, self.y)): possMoves.append((x, self.y))
        else: break
      for y in range(1, self.y+1):
        if checks((self.x, self.y-y)): possMoves.append((self.x, self.y-y))
        else: break
      for y in range(self.y+1, 8):
        if checks((self.x, y)): possMoves.append((self.x, y))
        else: break
      for x in range(1, min((self.x+1, 8-self.y))):
        if checks((self.x-x, self.y+x)): possMoves.append((self.x-x, self.y+x))
        else: break
      for x in range(1, min((8-self.x, 8-self.y))):
        if checks((self.x+x, self.y+x)): possMoves.append((self.x+x, self.y+x))
        else: break
      for x in range(1, min((self.x+1, self.y+1))):
        if checks((self.x-x, self.y-x)): possMoves.append((self.x-x, self.y-x))
        else: break
      for x in range(1, min((8-self.x, self.y+1))):
        if checks((self.x+x, self.y-x)): possMoves.append((self.x+x, self.y-x))
        else: break
    elif case('pawn'):
      m = 1 if self.team == 'white' else -1
      possMoves = []
      if checks((self.x, self.y+m)):
        possMoves.append((self.x, self.y+m))
        if self.y in [1, 6]: possMoves.append((self.x, self.y+(2*m)))
      if (self.x-1, self.y+m) in [(p.x, p.y) for p in pieces if p.team != self.team]: possMoves.append((self.x-1, self.y+m))
      if (self.x+1, self.y+m) in [(p.x, p.y) for p in pieces if p.team != self.team]: possMoves.append((self.x+1, self.y+m))
      return [x for x in possMoves if checks(x)]
    return possMoves
  def onButtonClick(self):
    global moveChoices, piece
    piece = self
    moveChoices = [(screen, pygame.Color(120, 120, 0, 120), (pos[0]*80, (7-pos[1])*80, 80, 80)) for pos in self.canMove()]
    for pos in self.canMove():
      tempTile = MoveTile(pos)
      boardTiles.add(tempTile)
      libObjects.add(tempTile)
  # def onButtonRelease(self):
    # global moveChoices
    # moveChoices = []
class BoardTile(Button):
  def __init__(self, pos, color):
    super().__init__(*pos, 80, 80)
    self.image.fill(color)
    self.rect.topleft = (pos[0]*80, pos[1]*80)
    self.pos = (pos[0], 7-pos[1])
  def onButtonClick(self):
    global moveChoices, piece
    print('tile at {} was clicked'.format(self.pos))
    print(tuple(self.rect))
    print([x[2] for x in moveChoices])
    try:
      print(piece.type, piece.pos)
    except AttributeError:
      print(piece)
    try:
      if self.rect in [x[2] for x in moveChoices] or self.rect.center == piece.rect.center:
        try:
          piece.rect.center = self.rect.center
          piece.pos = self.pos
          piece.x = self.pos[0]
          piece.y = self.pos[1]
          # moveChoices = []
        except AttributeError:
          pass
      else:
        # moveChoices = []
        pass
    except IndexError:
      pass
class MoveTile(Button):
  def __init__(self, pos):
    super().__init__(*pos, 80, 80)
    self.image.fill((120, 120, 0, 120))
    self.rect.topleft = (pos[0]*80, (7-pos[1])*80)
    self.pos = (pos[0], 7-pos[1])
  def onButtonClick(self):
    global moveChoices, piece
    try:
      piece.rect.center = self.rect.center
      piece.pos = self.pos
      piece.x = self.pos[0]
      piece.y = self.pos[1]
      piece = None
      moveChoices = []
      [tile.kill() for tile in boardTiles]
    except AttributeError:
      pass
def drawRectAlpha(surface, color, rect):
  shape_surf = pygame.Surface(pygame.Rect(rect).size, pygame.SRCALPHA)
  pygame.draw.rect(shape_surf, color, shape_surf.get_rect())
  surface.blit(shape_surf, rect)
abrToPiece = {
  'r':'rook',
  'n':'knight',
  'b':'bishop',
  'q':'queen',
  'k':'king',
  'p':'pawn'
}
pieces = pygame.sprite.Group()
for line in range(len(board)):
  for pos in range(len(board[line])):
    try:
      tempPiece = ChessPiece(abrToPiece[board[line][pos].lower()], (pos, 7-line), 'white' if board[line][pos].isupper() else 'black')
      pieces.add(tempPiece)
      libObjects.add(tempPiece)
    except KeyError:
      pass
def coordToBoard(coord, char, board = [[' ' for _ in range(8)] for _ in range(8)]):
  board[7-coord[1]][coord[0]] = char
  return board
def printMoves(piece):
  tempBoard = [[' ' for _ in range(8)] for _ in range(8)]
  for pos in piece.canMove():
    tempBoard = coordToBoard(pos, piece.type[0], tempBoard)
  print('~~~~~')
  print(*coordToBoard(piece.pos, piece.type[0].upper(), tempBoard), sep='\n')
  print('~~~~~')
# [printMoves(piece) for piece in pieces]
def getIndex(coord):
  letters = ['a','b','c','d','e','f','g','h']
  x = letters.index(coord[0])
  y = 8-int(coord[1])
  return (y, int(x))
def getPossMoves(piece, x, y):
    print(piece)
    x += 1
    y = 8 - y
    print(x)
    print(y)
    if piece == 'p':
        if y == 7:
            return [(x, y-1),(x, y-2)]
        elif y-2 in range(8):
            return [(x, y-1)]
        else:
            return []
    elif piece == 'P':
        if y == 2:
            return [(x, y+1),(x, y+2)]
        elif y in range(8):
            return [(x, y+1)]
        else:
            return []
    elif piece.lower() == 'r':
        tempMoves = []
        for i in range(1,8):
            if i != x:
                tempMoves.append((i, y))
            if i != y:
                tempMoves.append((x, i))
        return tempMoves
    elif piece.lower() == 'n':
        tempMoves = []
        if x-3 in range(8):
            if y-2 in range(8):
                tempMoves.append((x-2, y-1))
            if y in range(8):
                tempMoves.append((x-2, y+1))
        if x-2 in range(8):
            if y-3 in range(8):
                tempMoves.append((x-1, y-2))
            if y+1 in range(8):
                tempMoves.append((x-1, y+2))
        if x in range(8):
            if y-3 in range(8):
                tempMoves.append((x+1, y-2))
            if y+1 in range(8):
                tempMoves.append((x+1, y+2))
        if x+1 in range(8):
            if y-2 in range(8):
                tempMoves.append((x+2, y-1))
            if y in range(8):
                tempMoves.append((x+2, y+1))
        return tempMoves
    elif piece.lower() == 'b':
        tempMoves = []
        for i in range(1-x, 9-x):
            if y+i-1 in range(8):
                tempMoves.append((x+i, y+i))
            if y-i-1 in range(8):
                tempMoves.append((x+i, y-i))
        return tempMoves
    elif piece.lower() == 'k':
        tempMoves = []
        if x-2 in range(8):
            if y-2 in range(8):
                tempMoves.append((x-1, y-1))
            if y-1 in range(8):
                tempMoves.append((x-1, y))
            if y in range(8):
                tempMoves.append((x-1, y+1))
        if x-1 in range(8):
            if y-2 in range(8):
                tempMoves.append((x, y-1))
            if y in range(8):
                tempMoves.append((x, y+1))
        if x in range(8):
            if y-2 in range(8):
                tempMoves.append((x+1, y-1))
            if y-1 in range(8):
                tempMoves.append((x+1, y))
            if y in range(8):
                tempMoves.append((x+1, y+1))
        return tempMoves
    elif piece.lower() == 'q':
        tempMoves = []
        for i in range(1-x, 9-x):
            if y+i-1 in range(8):
                tempMoves.append((x+i, y+i))
            if y-i-i in range(8):
                tempMoves.append((x+i, y-i))
        for i in range(1,8):
            if i != x:
                tempMoves.append((i, y))
            if i != y:
                tempMoves.append((x, i))
        return tempMoves
def toIndex(coords):
  print(coords)
  tempValues = []
  for value in coords:
    x = 8-value[1]
    y = value[0]-1
    tempValues.append((x, y))
  return tempValues
running = True
frame = 0
moveChoices = []
piece = None
boardTiles = pygame.sprite.Group()
for i in range(8):
  for j in range(8):
    break
    tempTile = BoardTile((i, j), (205, 205, 205) if i%2 != j%2 else (50,50,50))
    boardTiles.add(tempTile)
    libObjects.add(tempTile)
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False
    libObjects.event(event)
  frame += 1
  screen.fill((50, 50, 50))
  [pygame.draw.rect(screen, (205, 205, 205), (i*80, (2*j+i%2)*80, 80, 80)) for i in range(8) for j in range(4)]
  boardTiles.draw(screen)
  # for choice in moveChoices: drawRectAlpha(*choice)
  pieces.draw(screen)
  pygame.display.flip()