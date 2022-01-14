import tkinter as tk
import pokemonInput as pi
import playerData as pD
from tkinter import ttk
from switch import switch, case
import os, random
os.chdir('/Users/jpollack/Desktop/CodingFiles/PokemonWorld')
colors = {'Normal' : '#A8A77A', 'Fire' : '#EE8130', 'Water' : '#6390F0', 'Electric' : '#F7D02C', 'Grass' : '#7AC74C', 'Ice' : '#96D9D6', 'Fighting' : '#C22E28', 'Poison' : '#A33EA1', 'Ground' : '#E2BF65', 'Flying' : '#A98FF3', 'Psychic' : '#F95587', 'Bug' : '#A6B91A', 'Rock' : '#B6A136', 'Ghost' : '#735797', 'Dragon' : '#5F35FC', 'Dark' : '#705746', 'Steel' : '#B7B7CE', 'Fairy' : '#D684AD'}
def changeDict(dictionary, variable, value):
  print(variable+' was',dictionary[variable])
  dictionary[variable] = value
  print(variable+' is now',dictionary[variable])
  dictionary.update()
def print(*args, **kwargs):
  import os, inspect, builtins
  builtins.print('{:20}'.format(lineFile:=f'{os.path.basename(__file__)}:{inspect.currentframe().f_back.f_lineno}')+' '.join(list(map(lambda x:str(x).replace('\n', '\n{:20}'.format(lineFile)), args))))
def name(pokemon):
  return pokemon.id if pokemon.name == None else pokemon.name
def printstats(poke1, poke2):
  tempRoot = tk.Toplevel()
  im1 = tk.Label(tempRoot, text=name(poke1)).grid(row=0, column=0, sticky='we', columnspan=3)
  cHp1 = tk.Label(tempRoot, text=poke1.cHp).grid(row=1, column=0)
  slash1 = tk.Label(tempRoot, text='/').grid(row=1, column=1, sticky='ew')
  tHp1 = tk.Label(tempRoot, text=poke1.tHp).grid(row=1, column=2)
  tAtk1 = tk.Label(tempRoot, text=poke1.tAtk).grid(row=2, column=0)
  atkM1 = tk.Label(tempRoot, text=poke1.atkM).grid(row=2, column=1, sticky='ew')
  mAtk1 = tk.Label(tempRoot, text=poke1.mAtk).grid(row=2, column=2)
  tDef1 = tk.Label(tempRoot, text=poke1.tDef).grid(row=3, column=0)
  defM1 = tk.Label(tempRoot, text=poke1.defM).grid(row=3, column=1, sticky='ew')
  mDef1 = tk.Label(tempRoot, text=poke1.mDef).grid(row=3, column=2)
  tSpa1 = tk.Label(tempRoot, text=poke1.tSpa).grid(row=4, column=0)
  spaM1 = tk.Label(tempRoot, text=poke1.spaM).grid(row=4, column=1, sticky='ew')
  mSpa1 = tk.Label(tempRoot, text=poke1.mSpa).grid(row=4, column=2)
  tSpd1 = tk.Label(tempRoot, text=poke1.tSpd).grid(row=5, column=0)
  spdM1 = tk.Label(tempRoot, text=poke1.spdM).grid(row=5, column=1, sticky='ew')
  mSpd1 = tk.Label(tempRoot, text=poke1.mSpd).grid(row=5, column=2)
  tSpe1 = tk.Label(tempRoot, text=poke1.tSpe).grid(row=6, column=0)
  speM1 = tk.Label(tempRoot, text=poke1.speM).grid(row=6, column=1, sticky='ew')
  mSpe1 = tk.Label(tempRoot, text=poke1.mSpe).grid(row=6, column=2)
  im2 = tk.Label(tempRoot, text=name(poke2)).grid(row=0, column=3, sticky='we',columnspan=3)
  cHp2 = tk.Label(tempRoot, text=poke2.cHp).grid(row=1, column=3)
  slash2 = tk.Label(tempRoot, text='/').grid(row=1, column=4, sticky='ew')
  tHp2 = tk.Label(tempRoot, text=poke2.tHp).grid(row=1, column=5)
  tAtk2 = tk.Label(tempRoot, text=poke2.tAtk).grid(row=2, column=3)
  atkM2 = tk.Label(tempRoot, text=poke2.atkM).grid(row=2, column=4, sticky='ew')
  mAtk2 = tk.Label(tempRoot, text=poke2.mAtk).grid(row=2, column=5)
  tDef2 = tk.Label(tempRoot, text=poke2.tDef).grid(row=3, column=3)
  defM2 = tk.Label(tempRoot, text=poke2.defM).grid(row=3, column=4, sticky='ew')
  mDef2 = tk.Label(tempRoot, text=poke2.mDef).grid(row=3, column=5)
  tSpa2 = tk.Label(tempRoot, text=poke2.tSpa).grid(row=4, column=3)
  spaM2 = tk.Label(tempRoot, text=poke2.spaM).grid(row=4, column=4, sticky='ew')
  mSpa2 = tk.Label(tempRoot, text=poke2.mSpa).grid(row=4, column=5)
  tSpd2 = tk.Label(tempRoot, text=poke2.tSpd).grid(row=5, column=3)
  spdM2 = tk.Label(tempRoot, text=poke2.spdM).grid(row=5, column=4, sticky='ew')
  mSpd2 = tk.Label(tempRoot, text=poke2.mSpd).grid(row=5, column=5)
  tSpe2 = tk.Label(tempRoot, text=poke2.tSpe).grid(row=6, column=3)
  speM2 = tk.Label(tempRoot, text=poke2.speM).grid(row=6, column=4, sticky='ew')
  mSpe2 = tk.Label(tempRoot, text=poke2.mSpe).grid(row=6, column=5)
  tempRoot.mainloop()
def testMove(player, move, opp):
  global playerHp, oppPokeHp
  print(f'\n\nUsing move {move["name"]} against {name(opp)}')
  testList = [player, opp]
  print(f'Made list of {name(player)} and {name(opp)}')
  compMove = random.choice([opp.move1, opp.move2, opp.move3, opp.move4])
  print(f'Chose move {compMove["name"]} for {name(opp)}')
  player.getStats()
  player.modifyStats()
  print('Got stats for player')
  opp.getStats()
  opp.modifyStats()
  print('Got stats for opponent')
  if player.mSpe > opp.mSpe:
    print(f'{name(player)} with speed {player.mSpe} outspeeds {name(opp)} with speed {opp.mSpe}')
    pi.testAttack(player, move, testList[move['target'] % 2])
    print(f'{name(player)} used {move["name"]} on {name(opp)}')
    if player.cHp > 0 and opp.cHp > 0:
      print(f'Both {name(player)} ({player.cHp}) and {name(opp)} ({opp.cHp}) have more than 0 hp')
      pi.testAttack(opp, compMove, testList[(compMove['target'] + 1) % 2])
      print(f'{name(opp)} used {compMove["name"]} on {name(player)}')
  else:
    print(f'{name(opp)} with speed {opp.mSpe} outspeeds {name(player)} with speed {player.mSpe}')
    pi.testAttack(opp, compMove, testList[(compMove['target'] + 1) % 2])
    print(f'{name(opp)} used {compMove["name"]} on {name(player)}')
    if player.cHp > 0 and opp.cHp > 0:
      print(f'Both {name(player)} ({player.cHp}) and {name(opp)} ({opp.cHp}) have more than 0 hp')
      pi.testAttack(player, move, testList[move['target'] % 2])
      print(f'{name(player)} used {move["name"]} on {name(opp)}')
  printstats(player, opp)
  updateHp(playerHp, player)
  updateHp(oppPokeHp, opp)



def soloBattle(root, playerPoke, oppPoke):
  global playerHp, oppPokeHp, battleWindow
  playerPoke.getStats()
  oppPoke.getStats()
  print(f'Entering battle with {oppPoke.id if oppPoke.name == None else oppPoke.name} as {playerPoke.id if playerPoke.name == None else playerPoke.name}')
  battleWindow = tk.Toplevel(root, width=640, height=640)
  battleWindow.geometry('+{}+{}'.format(root.winfo_x(), root.winfo_y()))
  print('Created window')
  playerPokeCan = tk.Canvas(battleWindow, width=150, height=150, highlightthickness=0)
  print('Created player canvas')
  playerPokeCan.create_text(75, 75, text=playerPoke.name if not playerPoke.name == None else playerPoke.id)
  print('Added player name text')
  playerPokeCan.grid(row=0, column=0)
  print('Added player canvas to frame')
  playerHp = ttk.Progressbar(battleWindow, maximum=playerPoke.tHp, variable=playerPoke.cHp)
  playerHp.grid(row=1, column=0, sticky='ew')
  sep = tk.Label(battleWindow, text=' ', width=32)
  sep.grid(row=0, column=1, rowspan=5)
  print('Created and added separator')
  try:
    playerMove1 = tk.Button(battleWindow, text=playerPoke.move1['name'], width=16, height=2, command=lambda:testMove(playerPoke, playerPoke.move1, oppPoke))
    print('Created move 1 button')
    playerMove1.grid(row=2, column=0)
    print('Added move 1 button')
  except AttributeError:
    print('No move 1')
  try:
    playerMove2 = tk.Button(battleWindow, text=playerPoke.move2['name'], width=16, height=2, command=lambda:testMove(playerPoke, playerPoke.move2, oppPoke))
    print('Created move 2 button')
    playerMove2.grid(row=3, column=0)
    print('Added move 2 button')
  except AttributeError:
    print('No move 2')
  try:
    playerMove3 = tk.Button(battleWindow, text=playerPoke.move3['name'], width=16, height=2, command=lambda:testMove(playerPoke, playerPoke.move3, oppPoke))
    print('Created move 3 button')
    playerMove3.grid(row=4, column=0)
    print('Added move 3 button')
  except AttributeError:
    print('No move 3')
  try:
    playerMove4 = tk.Button(battleWindow, text=playerPoke.move4['name'], width=16, height=2, command=lambda:testMove(playerPoke, playerPoke.move4, oppPoke))
    print('Created move 4 button')
    playerMove4.grid(row=5, column=0)
    print('Added move 4 button')
  except AttributeError:
    print('No move 4')
  oppPokeCan = tk.Canvas(battleWindow, width=150, height=150, highlightthickness=0)
  print('Created opponent canvas')
  oppPokeCan.create_text(75, 75, text=oppPoke.id if oppPoke.name == None else oppPoke.name)
  print('Added opponent name text')
  oppPokeCan.grid(row=0, column=2)
  print('Added opponent canvas to frame')
  oppPokeHp = ttk.Progressbar(battleWindow, maximum=oppPoke.tHp, variable=oppPoke.cHp)
  oppPokeHp.grid(row=1, column=2, sticky='ew')
  pokeball = tk.Button(battleWindow, text='PokeBall', width=16, height=2)
  print('Created pokeball button')
  openBag = tk.Button(battleWindow, text='Bag', width=16, height=2)
  print('Created bag button')
  pokemon = tk.Button(battleWindow, text='Pokemon', width=16, height=2)
  print('Created switch pokemon button')
  runAway = tk.Button(battleWindow, text='Run', width=16, height=2)
  print('Created run button')
  pokeball.grid(row=2, column=2)
  print('Added pokeball button to frame')
  openBag.grid(row=3, column=2)
  print('Added bag button to frame')
  pokemon.grid(row=4, column=2)
  print('Added switch pokemon button to frame')
  runAway.grid(row=5, column=2)
  print('Added run button to grid')
  battleWindow.after(1, lambda:print('Started battle window'))
  battleWindow.after(1, lambda:updateHp(playerHp, playerPoke))
  battleWindow.after(1, lambda:updateHp(oppPokeHp, oppPoke))
  battleWindow.mainloop()
def updateHp(playerHp, playerPoke):
  global battleWindow
  playerHp['value'] = playerPoke.cHp
  battleWindow.update_idletasks()