#Map Key:
#T -> Tree
#E -> Ground
#U -> Ledge (walk down from up)
#D -> Ledge (walk down from down)
#L -> Ledge (walk down from left)
#R -> Ledge (walk down from right)
#G -> Grass
#P -> Path

#NPC Key
#N -> NPC
#0 -> No NPC

#Level Key:
#0-9 -> Level
#Level difference of 1 is a ledge
#Level difference of 0.5 doesn't show

#20x20 window size

import os, random
from switch import switch, case
import battleGUI as battle
import startGUI as start
import tkinter as tk
from playerData import *
from PIL import ImageTk, Image
os.chdir('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PokemonWorld')
def print(*args, **kwargs):
  import os, inspect, builtins
  builtins.print('{:20}'.format(lineFile:=f'{os.path.basename(__file__)}:{inspect.currentframe().f_back.f_lineno}')+' '.join(list(map(lambda x:str(x).replace('\n', '\n{:20}'.format(lineFile)), args))))
data = []
with open('worldData.txt', 'r') as file:
  for line in file:
    data.append(line.rstrip('\n'))
map = []
for y in range(len(data)):
  map.append([])
  for x in data[y]:
    map[y].append(x)
root = tk.Tk()
root.geometry('640x640')
can = tk.Canvas(root, width=640, height=640, scrollregion=(0, 0, 32*len(map[0]), 32*len(map)), highlightthickness=0)
class player:
  def __init__(self, *, pos=[0, 10], master=can, direc = 'r', width=32, color='black'):
    self.pos = pos
    self.map = master
    self.direc = direc
    self.color = 'black'
    self.width = width
  def draw(self):
    # self.map.create_rectangle(self.pos[0]*32, self.pos[1]*32, self.pos[0]*32+self.width, self.pos[1]*32+self.width, fill=self.color)
    root.testing = testing = ImageTk.PhotoImage(Image.open('./images/playerDown.png').convert('RGBA'))
    self.map.create_image(self.pos[0]*32, self.pos[1]*32, anchor='nw', image=testing)
me = player()
def tick():
  me.draw()
  can.after(10, tick)
grass = '#52C720'
ledge = '#6A443F'
x = 0
y = 0
lastX = 0
lastY = 0
def toBox(x, y):
  return (x*32, y*32, x*32+32, y*32+32)
def move(event):
  global x, y, lastX, lastY
  lastX = me.pos[0]
  lastY = me.pos[1]
  tempCoords = (me.pos[0], me.pos[1])
  switch(event.keysym)
  if case('Up'):
    me.pos[1] -= 1
    me.direc = 'u'
  elif case('Down'):
    me.pos[1] += 1
    me.direc = 'd'
  elif case('Left'):
    me.pos[0] -= 1
    me.direc = 'l'
  elif case('Right'):
    me.pos[0] += 1
    me.direc = 'r'
  if me.pos[0] > len(map[0])-1:
    me.pos[0] = len(map[0])-1
  if me.pos[1] > len(map)-1:
    me.pos[1] = len(map)-1
  if me.pos[0] < 0:
    me.pos[0] = 0
  if me.pos[1] < 0:
    me.pos[1] = 0
  if not (map[me.pos[1]][me.pos[0]] == 'E' or map[me.pos[1]][me.pos[0]] == 'G' or (map[me.pos[1]][me.pos[0]] == 'U' and me.direc == 'd') or (map[me.pos[1]][me.pos[0]] == 'D' and me.direc == 'u') or (map[me.pos[1]][me.pos[0]] == 'L' and me.direc == 'r') or (map[me.pos[1]][me.pos[0]] == 'R' and me.direc == 'l')):
    me.pos[0] = tempCoords[0]
    me.pos[1] = tempCoords[1]
  if (map[me.pos[1]][me.pos[0]] == 'U' and me.direc == 'd'):
    me.pos[1] += 1
  if (map[me.pos[1]][me.pos[0]] == 'D' and me.direc == 'u'):
    me.pos[1] -= 1
  if (map[me.pos[1]][me.pos[0]] == 'L' and me.direc == 'r'):
    me.pos[0] += 1
  if (map[me.pos[1]][me.pos[0]] == 'R' and me.direc == 'l'):
    me.pos[0] -= 1
  x = me.pos[0] - 10
  y = me.pos[1] - 10
  if x > len(map[0])-20:
    x = len(map[0])-20
  if y > len(map)-20:
    y = len(map)-20
  if x < 0:
    x = 0
  if y < 0:
    y = 0
  can.xview('moveto', x/len(map[0]))
  can.yview('moveto', y/len(map))
  # can.create_rectangle(lastX*32, lastY*32, lastX*32+32, lastY*32+32, fill=tileMap[lastY][lastX])
  if map[me.pos[1]][me.pos[0]] == 'E' and random.randint(0, 255) < 20:
    bulbasaur = pokemon('Garchomp', 78, ivs=[24,12,30,16,23,5], evs=[74,190,91,48,84,23], nature='Adamant')
    bulbasaur.move1 = moveDict['Swords Dance']
    bulbasaur.move2 = moveDict['Earthquake']
    bulbasaur.move3 = moveDict['Outrage']
    bulbasaur.move4 = moveDict['Dragon Ascent']
    opp = pokemon('Entei', 100, evs=[0, 252, 0, 4, 0, 252], ivs=[31,31,31,31,31,31])
    opp.move1 = moveDict['Earthquake']
    opp.move2 = moveDict['Flamethrower']
    opp.move3 = moveDict['Swords Dance']
    opp.move4 = moveDict['Sacred Sword']
    battle.soloBattle(root, bulbasaur, opp)
  # print('({},{})'.format(me.pos[0],me.pos[1]))
  # print('{}x{}'.format(len(map[0]),len(map)))
  # print('{}x{}'.format(len(tileMap[0]),len(tileMap)))
  # print('Player: {} ({},{}) Tile:{} Color:{}'.format(event.keysym, me.pos[0], me.pos[1], map[me.pos[1]][me.pos[0]], tileMap[me.pos[1]][me.pos[0]]))
root.bind('<Down>', move)
root.bind('<Up>', move)
root.bind('<Left>', move)
root.bind('<Right>', move)
root.withdraw()
root.deiconify()
tileMap = []
trees = []
ground = []
grass = []
ledges = []
for row in range(len(map)):
  tileMap.append([])
  # imageMap.append([])
  for tile in range(len(map[row])):
    ground.append(ImageTk.PhotoImage(Image.open('./images/grass.png').convert('RGBA')))
    can.create_image(tile*32, row*32, anchor='nw', image=ground[-1])
for row in range(len(map)):
  # tileMap.append([])
  # imageMap.append([])
  for tile in range(len(map[row])):
    switch(map[row][tile].lower())
    if case('t'):
      testImage = Image.open('./images/tree.png').convert('RGBA')
      testImage2 = testImage.resize((128, 160))
      test = ImageTk.PhotoImage(testImage2)
      trees.append(test)
      map[row][tile+1] = ''
      map[row+1][tile] = ''
      map[row+1][tile+1] = ''
      can.create_image(tile*32-32, row*32-64, anchor='nw', image=trees[-1])
    elif case('g'):
      grass.append(ImageTk.PhotoImage(Image.open('./images/tall_grass.png').convert('RGBA')))
      can.create_image(tile*32, row*32, anchor='nw', image=grass[-1])
    #   can.create_rectangle(tile*32, row*32, tile*32+32, row*32+32, fill=grass)
    #   tileMap[-1].append(grass)
    elif case('u'):
      ledges.append(ImageTk.PhotoImage(Image.open('./images/upLedgeMid.png').convert('RGBA')))
      can.create_image(tile*32, row*32, anchor='nw', image=ledges[-1])
    elif case('u') or case('d') or case('l') or case('r'):
      pass
    #   can.create_rectangle(tile*32, row*32, tile*32+32, row*32+32, fill=ledge)
    #   tileMap[-1].append(ledge)
me.draw()
tick()
can.pack()
root.after(1, root.withdraw)
start.start(root)
root.mainloop()