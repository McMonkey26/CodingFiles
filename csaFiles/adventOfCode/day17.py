debug = True
def debugPrint(*args):
  if debug: print(*args)

with open('csaFiles/adventOfCode/day17.txt', 'r') as inp:
  direcs = [1 if i == '>' else -1 for i in inp.readlines()[0]]

pos = 0
rockShapes = '-+L|o'
placedRocks = []
class Rock:
  def __init__(self, shape):
    self.pos = []
    if shape == '-':
      self.pos = [
        [2,Rock.getMaxPos()+3],
        [3,Rock.getMaxPos()+3],
        [4,Rock.getMaxPos()+3],
        [5,Rock.getMaxPos()+3]
      ]
    elif shape == '+':
      self.pos = [
        [3,Rock.getMaxPos()+5],
        [2,Rock.getMaxPos()+4],
        [3,Rock.getMaxPos()+4],
        [4,Rock.getMaxPos()+4],
        [3,Rock.getMaxPos()+3]
      ]
    elif shape == 'L':
      self.pos = [
        [4,Rock.getMaxPos()+5],
        [4,Rock.getMaxPos()+4],
        [2,Rock.getMaxPos()+3],
        [3,Rock.getMaxPos()+3],
        [4,Rock.getMaxPos()+3],
      ]
    elif shape == '|':
      self.pos = [
        [2,Rock.getMaxPos()+6],
        [2,Rock.getMaxPos()+5],
        [2,Rock.getMaxPos()+4],
        [2,Rock.getMaxPos()+3]
      ]
    elif shape == 'o':
      self.pos = [
        [2,Rock.getMaxPos()+4],
        [3,Rock.getMaxPos()+4],
        [2,Rock.getMaxPos()+3],
        [3,Rock.getMaxPos()+3],
      ]
    debugPrint(str(len(placedRocks)) + 'max' + str(Rock.getMaxPos()))
    debugPrint(str(len(placedRocks)) + '\nnew rock :)' + str(self.pos))
  def getMaxPos():
    try:
      return max([max([i[1] for i in j.pos]) for j in placedRocks])
    except ValueError:
      return 0
  def move(self):
    global pos
    debugPrint(str(len(placedRocks)) + 'moving' + str(direcs[pos]))
    for i in range(len(self.pos)):
      self.pos[i][0] += direcs[pos]
    if any([i[0] > 6 or i[0] < 0 for i in self.pos]):
      debugPrint(str(len(placedRocks)) + 'hit a wall, going back')
      for i in range(len(self.pos)):
        self.pos[i][0] -= direcs[pos]
    pos += 1
    pos %= len(direcs)
    debugPrint(str(len(placedRocks)) + 'move pos ' + str(pos))
    for i in range(len(self.pos)):
      self.pos[i][1] -= 1
      if any([self.touching(rock) for rock in placedRocks]) or any([pos[1] < 0 for pos in self.pos]):
        debugPrint(str(len(placedRocks)) + 'hitGround')
        for i in range(len(self.pos)):
          self.pos[i][1] += 1
        placedRocks.append(self)
        break
  def touching(self, rock):
    return any([pos in self.pos for pos in rock.pos])
while len(placedRocks) < 2022:
  debugPrint(str(len(placedRocks)) + ' rocks')
  newRock = Rock(rockShapes[len(placedRocks)%len(rockShapes)])
  while not newRock in placedRocks:
    newRock.move()
print(Rock.getMaxPos())