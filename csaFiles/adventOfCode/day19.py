debug = False
def debugPrint(*args, **kwargs):
  if debug: print(*args, **kwargs)

blueprints = []
with open('csaFiles/adventOfCode/day19.txt') as inp:
  for line in inp.readlines():
    blueprint = line.split()
    blueprints.append([
      int(blueprint[6]),
      int(blueprint[12]),
      int(blueprint[18]),
      int(blueprint[21]),
      int(blueprint[27]),
      int(blueprint[30])
    ])
#ore robot -> [0] ore
#clay robot -> [1] ore
#obsidian robot -> [2] ore and [3] clay
#geode robot -> [4] ore and [5] obsidian

