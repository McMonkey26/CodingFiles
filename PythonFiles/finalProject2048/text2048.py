from switch import *
import random
board = [
  [0,0,0,0],
  [0,0,0,0],
  [4,0,0,0],
  [0,0,0,0]
]
def move(field, direc):
  # loop1 = [1, len(field), 1] | loop2 = [len(field)]       | nC1, nC2 = -1, 0  up
  # loop1 = [len(field)-1]     | loop2 = [len(field)]       | nC1, nC2 = 1, 0   down
  # loop1 = [len(field)]       | loop2 = [1, len(field), 1] | nC1, nC2 = 0, -1  left
  # loop1 = [len(field)]       | loop2 = [len(field)-1]     | nC1, nC2 = 0, 1   right
  switch(direc)
  collided = [[False for j in range(len(field[i]))] for i in range(len(field))]
  if case('u'):
    loop1 = [1, len(field), 1]
    loop2 = [len(field)]
    nC1, nC2 = -1, 0
  elif case('d'):
    loop1 = [len(field)-1]
    loop2 = [len(field)]
    nC1, nC2 = 1, 0
  elif case('l'):
    loop1 = [len(field)]
    loop2 = [1, len(field), 1]
    nC1, nC2 = 0, -1
  elif case('r'):
    loop1 = [len(field)]
    loop2 = [len(field)-1]
    nC1, nC2 = 0, 1
  for _ in range(4):
    for line in range(*loop1):
      for num in range(*loop2):
        if field[line+nC1][num+nC2] == 0 or field[line+nC1][num+nC2] == field[line][num] and not collided[line][num]:
          if field[line+nC1][num+nC2] != 0:
            collided[line+nC1][num+nC2] = True
          field[line+nC1][num+nC2] += field[line][num]
          field[line][num] = 0
    # print(*collided, sep='\n')
  return field
def canMove(field, direc=None):
  # loop1 = [1, len(field), 1] | loop2 = [len(field)]       | nC1, nC2 = -1, 0  up
  # loop1 = [len(field)-1]     | loop2 = [len(field)]       | nC1, nC2 = 1, 0   down
  # loop1 = [len(field)]       | loop2 = [1, len(field), 1] | nC1, nC2 = 0, -1  left
  # loop1 = [len(field)]       | loop2 = [len(field)-1]     | nC1, nC2 = 0, 1   right
  switch(direc)
  if case('u'):
    loop1 = [1, len(field), 1]
    loop2 = [len(field)]
    nC1, nC2 = -1, 0
  elif case('d'):
    loop1 = [len(field)-1]
    loop2 = [len(field)]
    nC1, nC2 = 1, 0
  elif case('l'):
    loop1 = [len(field)]
    loop2 = [1, len(field), 1]
    nC1, nC2 = 0, -1
  elif case('r'):
    loop1 = [len(field)]
    loop2 = [len(field)-1]
    nC1, nC2 = 0, 1
  else:
    return any([canMove(field, 'u'), canMove(field, 'd'), canMove(field, 'l'), canMove(field, 'r')])
  # for line in range(*loop1):
  #   for num in range(*loop2):
  #     print(field[line][num],'|',field[line+nC1][num+nC2],':',(field[line+nC1][num+nC2] == 0 or field[line+nC1][num+nC2] == field[line][num]) and field[line][num] != 0)
  return any([any([(field[line+nC1][num+nC2] == 0 or field[line+nC1][num+nC2] == field[line][num]) and field[line][num] != 0 for num in range(*loop2)]) for line in range(*loop1)])
manual = True
while canMove(board) if manual else True:
  if not manual and not canMove(board):
    print('~~')
    print(*board, sep='\n')
    board = [[0 for _ in range(4)] for _ in range(4)]
    board[random.randint(0, 3)][random.randint(0, 3)] = 2 if random.random() < 0.9 else 4
  if manual:
    print('~~~~~')
    print(*board, sep='\n')
    print('~~~~~')
  inp = input() if manual else random.choice('udlr')
  while not inp.lower() in ['u','d','l','r']:
    if inp == 'stop':
      board = [[1,2,3],[4,5,6]]
      break
    else:
      inp = input('Please type u,d,l,r')
  if canMove(board, inp):
    move(board, inp)
    while board[(x:=random.randint(0, 3))][(y:=random.randint(0, 3))] != 0:
      x = random.randint(0, 3)
      y = random.randint(0, 3)
    board[x][y] = 2 if random.random() < 0.9 else 4