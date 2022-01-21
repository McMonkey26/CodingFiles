import random, os
from switch import switch, case
import PySimpleGUI as sg
os.chdir('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PokemonWorld')
def print(*args, **kwargs):
  import os, inspect, builtins
  builtins.print('{:20}'.format(lineFile:=f'{os.path.basename(__file__)}:{inspect.currentframe().f_back.f_lineno}')+' '.join(list(map(lambda x:str(x).replace('\n', '\n{:20}'.format(lineFile)), args))))
debug = False
colors = {'Normal' : '#A8A77A', 'Fire' : '#EE8130', 'Water' : '#6390F0', 'Electric' : '#F7D02C', 'Grass' : '#7AC74C', 'Ice' : '#96D9D6', 'Fighting' : '#C22E28', 'Poison' : '#A33EA1', 'Ground' : '#E2BF65', 'Flying' : '#A98FF3', 'Psychic' : '#F95587', 'Bug' : '#A6B91A', 'Rock' : '#B6A136', 'Ghost' : '#735797', 'Dragon' : '#5F35FC', 'Dark' : '#705746', 'Steel' : '#B7B7CE', 'Fairy' : '#D684AD'}
types = ["Normal","Fighting","Flying","Poison","Ground","Rock","Bug","Ghost","Steel","Fire","Water","Grass","Electric","Psychic","Ice","Dragon","Dark","Fairy", None]
typeBonus = [
[  1,  1,  1,  1,  1,0.5,  1,  0,0.5,  1,  1,  1,  1,  1,  1,  1,  1,  1, 1], #Normal
[  2,  1,0.5,0.5,  1,  2,0.5,  0,  2,  1,  1,  1,  1,0.5,  2,  1,  2,0.5, 1], #Fighting
[  1,  2,  1,  1,  1,0.5,  2,  1,0.5,  1,  1,  2,0.5,  1,  1,  1,  1,  1, 1], #Flying
[  1,  1,  1,0.5,0.5,0.5,  1,0.5,  0,  1,  1,  2,  1,  1,  1,  1,  1,  2, 1], #Poison
[  1,  1,  0,  2,  1,  2,0.5,  1,  2,  2,  1,0.5,  2,  1,  1,  1,  1,  1, 1], #Ground
[  1,0.5,  2,  1,0.5,  1,  2,  1,0.5,  2,  1,  1,  1,  1,  2,  1,  1,  1, 1], #Rock
[  1,0.5,0.5,0.5,  1,  1,  1,0.5,0.5,0.5,  1,  2,  1,  2,  1,  1,  2,0.5, 1], #Bug
[  0,  1,  1,  1,  1,  1,  1,  2,  1,  1,  1,  1,  1,  2,  1,  1,0.5,  1, 1], #Ghost
[  1,  1,  1,  1,  1,  2,  1,  1,0.5,0.5,0.5,  1,0.5,  1,  2,  1,  1,  2, 1], #Steel
[  1,  1,  1,  1,  1,0.5,  2,  1,  2,0.5,0.5,  2,  1,  1,  2,0.5,  1,  1, 1], #Fire
[  1,  1,  1,  1,  2,  2,  1,  1,  1,  2,0.5,0.5,  1,  1,  1,0.5,  1,  1, 1], #Water
[  1,  1,0.5,0.5,  2,  2,0.5,  1,0.5,0.5,  2,0.5,  1,  1,  1,0.5,  1,  1, 1], #Grass
[  1,  1,  2,  1,  0,  1,  1,  1,  1,  1,  2,0.5,0.5,  1,  1,0.5,  1,  1, 1], #Electric
[  1,  2,  1,  2,  1,  1,  1,  1,0.5,  1,  1,  1,  1,0.5,  1,  1,  0,  1, 1], #Psychic
[  1,  1,  2,  1,  2,  1,  1,  1,0.5,0.5,0.5,  2,  1,  1,0.5,  2,  1,  1, 1], #Ice
[  1,  1,  1,  1,  1,  1,  1,  1,0.5,  1,  1,  1,  1,  1,  1,  2,  1,  0, 1], #Dragon
[  1,0.5,  1,  1,  1,  1,  1,  2,  1,  1,  1,  1,  1,  2,  1,  1,0.5,0.5, 1], #Dark
[  1,  2,  1,0.5,  1,  1,  1,  1,0.5,0.5,  1,  1,  1,  1,  1,  2,  2,  1, 1]  #Fairy
]
def name(pokemon):
  return pokemon.id if pokemon.name == None else pokemon.name
def dmgModifier(atkPoke, move, defPoke):
    atkTypeIndex1 = types.index(move['type']) - 1
    if defPoke['types'][0] in types:
        defTypeIndex1 = types.index(defPoke['types'][0]) - 1
        defTypeIndex2 = types.index(defPoke['types'][1]) - 1
    else:
        defTypeIndex1 = types.index(defPoke['types'][1]) - 1
        defTypeIndex2 = 'no'
    type = 1
    STAB = 1
    rand = 1
    crit = 1
    burn = 1
    para = 1
    froz = 1
    slep = 1
    type = typeBonus[atkTypeIndex1][defTypeIndex1]
    if defTypeIndex2 != 'no':
        type *= typeBonus[atkTypeIndex1][defTypeIndex2]
    if(random.random() < 0.0625):
        crit = 2
    rand = 0.85 + (0.15 * random.random())
    if move['type'] in atkPoke['types']:
        STAB = 1.5
    if(atkPoke['statuses'][0] and move['category'] == 'Physical'):
        burn = 0.5
    if(atkPoke['statuses'][1]):
        froz = 0
    if(atkPoke['statuses'][2] and random.random() < 0.25):
        para = 0
    if(atkPoke['statuses'][5]):
        slep = 0
    dmgChange = type * STAB * rand * crit * burn * para * froz * slep
    if debug:
        print("Attacking Pokemon Type:",atkPoke['types'][0],atkPoke['types'][1])
        print("Defending Pokemon Type:",defPoke['types'][0],defPoke['types'][1])
        print("Move Type:",move['type'])
        print("Random:",rand)
        print("STAB:",STAB)
        print("Type Bonus:",type)
        print("Crit:",crit)
        print("Burn:",burn)
        print("Paralyze:",para)
        print("Freeze:",froz)
        print("Sleep:",slep)
        print("Total Modifier:",dmgChange)
    return dmgChange

def testModifier(atkPoke, move, defPoke):
  atkTypeIndex = types.index(move['type'])
  defTypeIndex1 = types.index(defPoke.typeMain)
  defTypeIndex2 = types.index(defPoke.typeSub)
  type = 1
  STAB = 1
  rand = 1
  crit = 1
  burn = 1
  para = 1
  froz = 1
  slep = 1
  type = typeBonus[atkTypeIndex][defTypeIndex1] * typeBonus[atkTypeIndex][defTypeIndex2]
  if random.random() < 0.0625:
    crit = 2
  rand = 0.85 + (0.15 * random.random())
  if move['type'] in [atkPoke.typeMain, atkPoke.typeSub]:
    STAB = 1.5
  if atkPoke.status.brn and move['category'] == 'Physical':
    burn = 0.5
  if atkPoke.status.frz:
    froz = 0
  if atkPoke.status.par and random.random() < 0.25:
    para = 0
  if atkPoke.status.slp:
    slep = 0
  dmgChange = type * STAB * rand * crit * burn * para * froz * slep
  if debug:
    print("Attacking Pokemon Type:",atkPoke.typeMain, atkPoke.typeSub)
    print("Defending Pokemon Type:",defPoke.typeMain, defPoke.typeSub)
    print("Move Type:",move['type'])
    print("Random:",rand)
    print("STAB:",STAB)
    print("Type Bonus:",type)
    print("Crit:",crit)
    print("Burn:",burn)
    print("Paralyze:",para)
    print("Freeze:",froz)
    print("Sleep:",slep)
    print("Total Modifier:",dmgChange)
  return dmgChange


def changeStat(baseStat, statChange):
    statReturned = baseStat
    if statChange == 0:
        return statReturned
    elif statChange < 0:
        statReturned = (baseStat * 2 / (2 - statChange))
        return statReturned
    else:
        statReturned = (baseStat * (2 + statChange) / 2)
        return statReturned

def testAttack(atkPoke, move, defPoke):
  print(f'\n\n{name(atkPoke)} used {move["name"]} on {name(defPoke)}')
  # print(move)
  if (move['acc'] <= 100 and random.randint(0, 100) < move['acc']) or move['acc'] > 100:
    print('The move hit')
    if move['category'] == 'Physical':
      print('Physical')
      defPoke.cHp -= (damage:=int(((2 * atkPoke.level // 5 + 2) * move['power'] * atkPoke.mAtk // defPoke.mDef) // 50 + 2 * testModifier(atkPoke, move, defPoke)))
      print('Health:{}, dealt {} damage'.format(defPoke.cHp, damage))
    elif move['category'] == 'Special':
      print('Special')
      defPoke.cHp -= (damage:=int(((2 * atkPoke.level // 5 + 2) * move['power'] * atkPoke.mSpa // defPoke.mSpd) // 50 + 2 * testModifier(atkPoke, move, defPoke)))
      print('Health:{}, dealt {} damage'.format(defPoke.cHp, damage))
    for i in range(len(move['targetBuffs'])):
      # print(f'Trying to buff {name(defPoke)}')
      switch(i)
      # if case(0):
        # print('Attack stat')
      # elif case(1):
        # print('Defense stat')
      # elif case(2):
        # print('Special Attack stat')
      # elif case(3):
        # print('Special Defense stat')
      # elif case(4):
        # print('Speed stat')
      buffChance = move['targetBuffs'][i] % 100
      # print(f'{buffChance}% chance to buff')
      if move['targetBuffs'][i] >= 0:
        statChance = move['targetBuffs'][i] + 99
      else:
        statChance = move['targetBuffs'][i]
      buffAmt = statChance // 100
      # print(f'Buffing by {buffAmt}')
      # print(f'Trying to buff {name(defPoke)} with a {buffChance}% chance to buff by {buffAmt}')
      if (debugRand:=random.randint(0, 100)) < buffChance:
        print(f'Buffed {name(defPoke)}', end='')
        switch(i)
        if case(0):
          defPoke.atkM += buffAmt
          # print('\'s attack stat')
        elif case(1):
          defPoke.defM += buffAmt
          # print('\'s defense stat')
        elif case(2):
          defPoke.spaM += buffAmt
          # print('\'s special attack stat')
        elif case(3):
          defPoke.spdM += buffAmt
          # print('\'s special defense stat')
        elif case(4):
          defPoke.speM += buffAmt
          # print('\'s speed stat')
    for i in range(len(move['selfBuffs'])):
      # print(f'Trying to buff {name(atkPoke)}', end='')
      switch(i)
      # if case(0):
        # print('\'s attack stat', end='')
      # elif case(1):
        # print('\'s defense stat', end='')
      # elif case(2):
        # print('\'s special attack stat', end='')
      # elif case(3):
        # print('\'s special defense stat', end='')
      # elif case(4):
        # print('\'s speed stat', end='')
        
      buffChance = move['selfBuffs'][i] % 100
      if move['selfBuffs'][i] % 100 == 0 and not move['selfBuffs'][i] == 0:
        buffChance = 100
      # print(f', {buffChance}% chance to buff', end='')
      if move['selfBuffs'][i] >= 0:
        statChance = move['selfBuffs'][i] + 99
      else:
        statChance = move['selfBuffs'][i]
      buffAmt = statChance // 100
      # print(f' by {buffAmt}')
      # print(f'test buff amt = {((test:=move["selfBuffs"][i]) + (99 if test >= 0 else 0)) // 100}')
      if random.randint(0, 100) < buffChance:
        # print(f'Buffed {name(atkPoke)}', end='')
        switch(i)
        if case(0):
          atkPoke.atkM += buffAmt
          # print('\'s attack stat')
        elif case(1):
          atkPoke.defM += buffAmt
          # print('\'s defense stat')
        elif case(2):
          atkPoke.spaM += buffAmt
          # print('\'s special attack stat')
        elif case(3):
          atkPoke.spdM += buffAmt
          # print('\'s special defense stat')
        elif case(4):
          atkPoke.speM += buffAmt
          # print('\'s speed stat')
    if not any(vars(defPoke.status).values()):
      statusCheck = random.randint(0, 100)
      for i in range(len(move['statuses'])):
        if statusCheck < move['statuses'][i]:
          switch(i)
          if case(0):
            defPoke.status.brn = True
          elif case(1):
            defPoke.status.frz = True
          elif case(2):
            defPoke.status.par = True
          elif case(3):
            defPoke.status.pos = True
          elif case(4):
            defPoke.status.tox = True
          elif case(5):
            defPoke.status.slp = True
def attack(atkPoke, move, defPoke):
    atk = changeStat(atkPoke['finalStats']['atk'], atkPoke['modifiers'][0])
    defence = changeStat(defPoke['finalStats']['def'], defPoke['modifiers'][1])
    spa = changeStat(atkPoke['finalStats']['spa'], atkPoke['modifiers'][2])
    spd = changeStat(defPoke['finalStats']['spd'], defPoke['modifiers'][3])
    if(move['acc'] <= 100 and random.randint(0,100) < move['acc']):
        if(move['category'] == "Physical"):
            defPoke['finalStats']['hp'] -= (((2 * atkPoke['lvl'] // 5 + 2) * move['power'] * atk // defence) // 50 + 2) * dmgModifier(atkPoke, move, defPoke)
        elif(move['category'] == "Special"):
            defPoke['finalStats']['hp'] -= (((2 * atkPoke['lvl'] // 5 + 2) * move['power'] * spa // spd) // 50 + 2) * dmgModifier(atkPoke, move, defPoke)
        for i in range(len(move['targetBuffs'])):
            buffChance = move['targetBuffs'][i] % 100
            if move['targetBuffs'][i] >= 0:
                statChance = move['targetBuffs'][i] + 99
            else:
                statChance = move['targetBuffs'][i]
            buffAmt = statChance // 100
            if random.randint(0,100) < buffChance:
                defPoke['modifiers'][i] += buffAmt
        for i in range(len(move['selfBuffs'])):
            buffChance = move['selfBuffs'][i] % 100
            if move['selfBuffs'][i] >= 0:
                statChance = move['selfBuffs'][i] + 99
            else:
                statChance = move['selfBuffs'][i]
            buffAmt = statChance // 100
            if random.randint(0,100) < buffChance:
                atkPoke['modifiers'][i] += buffAmt
        if(not any(defPoke['statuses'])):
            statusCheck = random.randint(0,100)
            for i in range(len(move['statuses'])):
                if(statusCheck < move['statuses'][i]):
                    defPoke['statuses'][i] = True

    elif(move['acc'] > 100):
        if(move['category'] == "Physical"):
            defPoke['finalStats']['hp'] -= (((2 * atkPoke['lvl'] // 5 + 2) * move['power'] * atk // defence) // 50 + 2) * dmgModifier(atkPoke, move, defPoke)
        elif(move['category'] == "Special"):
            defPoke['finalStats']['hp'] -= (((2 * atkPoke['lvl'] // 5 + 2) * move['power'] * spa // spd) // 50 + 2) * dmgModifier(atkPoke, move, defPoke)
        for i in range(len(move['targetBuffs'])):
            buffChance = move['targetBuffs'][i] % 100
            if move['targetBuffs'][i] >= 0:
                statChance = move['targetBuffs'][i] + 99
            else:
                statChance = move['targetBuffs'][i]
            buffAmt = statChance // 100
            if random.randint(0,100) < buffChance:
                defPoke['modifiers'][i] += move['targetBuffs'][i]
        for i in range(len(move['selfBuffs'])):
            buffChance = move['selfBuffs'][i] % 100
            if move['selfBuffs'][i] >= 0:
                statChance = move['selfBuffs'][i] + 99
            else:
                statCHance = move['selfBuffs'][i]
            buffAmt = statChance // 100
            if random.randint(0,100) < buffChance:
                atkPoke['modifiers'][i] += buffAmt
        if(not any(defPoke['statuses'])):
            statusCheck = random.randint(0,100)
            for i in range(len(move['statuses'])):
                if(statusCheck < move['statuses'][i]):
                    defPoke['statuses'][i] = True
