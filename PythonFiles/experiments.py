import pygame, random
from switch import *

pygame.init()
screen = pygame.display.set_mode((320, 256))

class Cronomotron:
  score = 0
  pos = 0
  path = []
  def getPath():
    return [random.randint(0, 9) for i in range(Cronomotron.score+1)]
Cronomotron.path = Cronomotron.getPath()
print(Cronomotron.path)
class CronoButton(Button):
  def __init__(self, pos, piece, color):
    super().__init__(*pos, 64, 128)
    self.image.fill(iTC(piece))
    self.piece = piece
  def onButtonClick(self):
    global running
    try:
      if Cronomotron.path[Cronomotron.pos] == self.piece:
        Cronomotron.pos += 1
        if Cronomotron.pos >= len(Cronomotron.path):
          Cronomotron.score += 1
          Cronomotron.pos = 0
          Cronomotron.path = Cronomotron.getPath()
          print(Cronomotron.path)
      else:
        print('Final Score:',Cronomotron.score)
        running = False
    except IndexError:
      pass
  def update(self):
    screen.blit(self.image, self.rect)
def iTC(value):
  return (25*value, 25*value, 25*value)
libObjects.add(CronoButton((0,0), 0, (255, 255, 255)))
libObjects.add(CronoButton((64,0), 1, (255, 255, 255)))
libObjects.add(CronoButton((128,0), 2, (255, 255, 255)))
libObjects.add(CronoButton((192,0), 3, (255, 255, 255)))
libObjects.add(CronoButton((256,0), 4, (255, 255, 255)))
libObjects.add(CronoButton((0,128), 5, (255, 255, 255)))
libObjects.add(CronoButton((64,128), 6, (255, 255, 255)))
libObjects.add(CronoButton((128,128), 7, (255, 255, 255)))
libObjects.add(CronoButton((192,128), 8, (255, 255, 255)))
libObjects.add(CronoButton((256,128), 9, (255, 255, 255)))

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
    libObjects.event(event)
  libObjects.update()
  pygame.display.flip()