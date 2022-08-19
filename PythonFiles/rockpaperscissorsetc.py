import random
moves = [
  'rock',
  'gun',
  'lightning',
  'devil',
  'dragon',
  'water',
  'air',
  'paper',
  'sponge',
  'wolf',
  'tree',
  'human',
  'snake',
  'scissors',
  'fire',
  'rock',
  'gun',
  'lightning',
  'devil',
  'dragon',
  'water',
  'air',
  'paper',
  'sponge',
  'wolf',
  'tree',
  'human',
  'snake',
  'scissors',
  'fire'
]
def matchUp(move):
  return moves[moves.index(move)+8:moves.index(move)+15]
matchUpDict = {move:matchUp(move) for move in moves[:15]}
for move, matches in matchUpDict.items():
  print('{:9}|{}'.format(move,matches))
wins = [0,0]
while max(wins) < 5:
  compMove = random.choice(moves)
  while (playerMove:=input()) not in moves:
    print('Pick a move out of',moves[:15])
  if compMove in matchUpDict[playerMove]:
    wins[0] += 1
    print(playerMove.capitalize()+'>'+compMove.capitalize())
  elif playerMove in matchUpDict[compMove]:
    wins[1] += 1
    print(playerMove.capitalize()+'<'+compMove.capitalize())
  print(wins,'\r')