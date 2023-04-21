debug = False
def debugPrint(*args, **kwargs):
  if debug: print(*args, **kwargs)

with open('csaFiles/adventOfCode/day18.txt') as inp:
  cubes = [list(map(int, i.strip().split(','))) for i in inp.readlines()]
totalSA = 0
for i in range(len(cubes)):
  cube = cubes[i]
  sides = 6
  cubeSides = [[],[],[],[],[],[]]
  for j in range(10):
    cubeSides[0].append([cube[0]+j, cube[1], cube[2]])
    cubeSides[1].append([cube[0]-j, cube[1], cube[2]])
    cubeSides[2].append([cube[0], cube[1]+j, cube[2]])
    cubeSides[3].append([cube[0], cube[1]-j, cube[2]])
    cubeSides[4].append([cube[0], cube[1], cube[2]+j])
    cubeSides[5].append([cube[0], cube[1], cube[2]-j])
  for side in cubeSides:
    if any([x in cubes[:i] or x in cubes[i+1:] for x in side]):
      sides -= 1
  totalSA += sides
print(totalSA)