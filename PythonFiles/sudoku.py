import pygame
board = [
  '000000000',
  '000000000',
  '000000000',
  '000000000',
  '000000000',
  '000000000',
  '000000000',
  '000000000',
  '000000000'
]
def pBoard(sBoard):
  for line in range(len(sBoard)):
    print(sBoard[line][:3]+'|'+sBoard[line][3:6]+'|'+sBoard[line][6:])
    if line in [2, 5]:
      print('---┼---┼---')
pBoard(board)
pygame.init()
screen = pygame.display.set_mode((676, 676))
numFont = pygame.font.SysFont('arial', 64)
class Number(pygame.sprite.Sprite):
  def __init__(self, pos, num):
    super().__init__()
    self.image = pygame.Surface((64, 64))
    self.image.fill((222, 222, 222))
    self.rect = self.image.get_rect()
    self.rect.topleft = pos
    self.num = numFont.render(str(num), False, (0, 0, 0))
    self.numRect = self.num.get_rect()
    self.numRect.center = (pos[0]+32, pos[1]+32)
    self.image.blit(self.num, self.numRect.topleft)
screenBoard = pygame.sprite.Group()
screenBoard.add(Number((0, 0), 1))
screenBoard.add(Number((74, 0), 1))
while True:
  if any(list(map(lambda x:x.type==pygame.QUIT, pygame.event.get()))): break
  screen.fill((0, 0, 0))
  screenBoard.draw(screen)
  pygame.display.flip()