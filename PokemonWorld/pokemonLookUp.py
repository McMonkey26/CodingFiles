import random, os, sys
os.chdir('/Users/jpollack/Desktop/CodingFiles/pokemonWorld')
def print(*args, **kwargs):
  import os, inspect, builtins
  builtins.print('{:20}'.format(lineFile:=f'{os.path.basename(__file__)}:{inspect.currentframe().f_back.f_lineno}')+' '.join(list(map(lambda x:str(x).replace('\n', '\n{:20}'.format(lineFile)), args))))
#Pokemon Dictionary \/\/\/
#a.datas += [('/Users/jpollack/Desktop/CodingFiles/pokemon.txt'),('/Users/jpollack/Desktop/CodingFiles/moves.txt')]
input = open('./pokemon.txt', 'r')
pokemon = [[] for i in range(892)]
pokeDict = {}
i = -1
for line in input:
    if line == '#-------------------------------\n':
        i += 1
    pokemon[i].append(line.rstrip('\n'))
input.close()
pokemon.insert(0,pokemon[-1])
del(pokemon[-1])

for p in range(len(pokemon)):
    if 'Type2' not in pokemon[p][5]:
        pokemon[p].insert(5,'Type2=')
    stats = pokemon[p][6].split(',')
    stats[0] = stats[0].lstrip('BaseStats=')
    for i in range(len(stats)):
        stats[i] = int(stats[i])
    pokeDict[pokemon[p][2].lstrip('Name=')] = {'name':pokemon[p][2].lstrip('Name='),'types':[pokemon[p][4].lstrip('Type1=').capitalize(),pokemon[p][5].lstrip('Type2=').capitalize()], 'baseStats': {'hp':stats[0],'atk':stats[1],'def':stats[2],'spa':stats[4],'spd':stats[5],'spe':stats[3]}, 'lvl': 100, 'modifiers':[0,0,0,0,0], 'statuses': [0,0,0,0,0,0], 'Evs': [0,0,0,0,0,0], 'Ivs': [0,0,0,0,0,0]}

#Pokemon Dictionary /\/\/\
# print(pokeDict['Entei'])
# print(pokeDict['Ivysaur'])
#Move Dictionary \/\/\/

input = open('moves.txt', 'r')
moves = []
moveDict = {}
for line in input:
    move = line.split(',')
    moves.append(move)
input.close()
q = 0
moveDict[''] = {'error':404}
for q in range(len(moves)):
    moveDict[moves[q][2]] = {'power':int(moves[q][4]),'acc':(int(moves[q][7]) if not int(moves[q][7]) == 0 else 101),'target':'?','category':moves[q][6],'targetBuffs':[0,0,0,0,0],'selfBuffs':[0,0,0,0,0],'statuses':[0,0,0,0,0,0],'type':moves[q][5].capitalize(),'name':moves[q][2], 'priority':int(moves[q][11]), 'flags':moves[q][12]}
    if moves[q][3] == '003':
        moveDict[moves[q][2]]['statuses'][5] = int(moves[q][9])
    elif moves[q][3] == '005':
        moveDict[moves[q][2]]['statuses'][3] = int(moves[q][9])
    elif moves[q][3] == '006':
        moveDict[moves[q][2]]['statuses'][4] = int(moves[q][9])
    elif moves[q][3] == '007':
        moveDict[moves[q][2]]['statuses'][2] = int(moves[q][9])
    elif moves[q][3] == '008':
        moveDict[moves[q][2]]['statuses'][2] = int(moves[q][9])
    elif moves[q][3] == '009':
        moveDict[moves[q][2]]['statuses'][2] = int(moves[q][9])
    elif moves[q][3] == '00A':
        moveDict[moves[q][2]]['statuses'][0] = int(moves[q][9])
    elif moves[q][3] == '00B':
        moveDict[moves[q][2]]['statuses'][0] = int(moves[q][9])
    elif moves[q][3] == '00C':
        moveDict[moves[q][2]]['statuses'][1] = int(moves[q][9])
    elif moves[q][3] == '00D':
        moveDict[moves[q][2]]['statuses'][1] = int(moves[q][9])
    elif moves[q][3] == '00E':
        moveDict[moves[q][2]]['statuses'][1] = int(moves[q][9])
    elif moves[q][3] == '01C':
        moveDict[moves[q][2]]['selfBuffs'][0] = int(moves[q][9])
    elif moves[q][3] == '01D':
        moveDict[moves[q][2]]['selfBuffs'][1] = int(moves[q][9])
    elif moves[q][3] == '01E':
        moveDict[moves[q][2]]['selfBuffs'][1] = int(moves[q][9])
    elif moves[q][3] == '01F':
        moveDict[moves[q][2]]['selfBuffs'][4] = int(moves[q][9])
    elif moves[q][3] == '020':
        moveDict[moves[q][2]]['selfBuffs'][2] = int(moves[q][9])
    elif moves[q][3] == '021':
        moveDict[moves[q][2]]['selfBuffs'][3] = int(moves[q][9])
    elif moves[q][3] == '024':
        moveDict[moves[q][2]]['selfBuffs'][0] = int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][1] = int(moves[q][9])
    elif moves[q][3] == '025':
        moveDict[moves[q][2]]['selfBuffs'][0] = int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][1] = int(moves[q][9])
    elif moves[q][3] == '026':
        moveDict[moves[q][2]]['selfBuffs'][0] = int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][4] = int(moves[q][9])
    elif moves[q][3] == '027':
        moveDict[moves[q][2]]['selfBuffs'][0] = int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][2] = int(moves[q][9])
    elif moves[q][3] == '028':
        moveDict[moves[q][2]]['selfBuffs'][0] = int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][2] = int(moves[q][9])
    elif moves[q][3] == '029':
        moveDict[moves[q][2]]['selfBuffs'][0] = int(moves[q][9])
    elif moves[q][3] == '02A':
        moveDict[moves[q][2]]['selfBuffs'][1] = int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][3] = int(moves[q][9])
    elif moves[q][3] == '02B':
        moveDict[moves[q][2]]['selfBuffs'][2] = int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][3] = int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][4] = int(moves[q][9])
    elif moves[q][3] == '02C':
        moveDict[moves[q][2]]['selfBuffs'][2] = int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][3] = int(moves[q][9])
    elif moves[q][3] == '02D':
        moveDict[moves[q][2]]['selfBuffs'][0] = int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][1] = int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][2] = int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][3] = int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][4] = int(moves[q][9])
    elif moves[q][3] == '02E':
        moveDict[moves[q][2]]['selfBuffs'][0] = int(moves[q][9]) + 200
    elif moves[q][3] == '02F':
        moveDict[moves[q][2]]['selfBuffs'][1] = int(moves[q][9]) + 200
    elif moves[q][3] == '030':
        moveDict[moves[q][2]]['selfBuffs'][4] = int(moves[q][9]) + 200
    elif moves[q][3] == '031':
        moveDict[moves[q][2]]['selfBuffs'][4] = int(moves[q][9]) + 200
    elif moves[q][3] == '032':
        moveDict[moves[q][2]]['selfBuffs'][2] = int(moves[q][9]) + 200
    elif moves[q][3] == '033':
        moveDict[moves[q][2]]['selfBuffs'][3] = int(moves[q][9]) + 200
    elif moves[q][3] == '034':
        #+2 evasion, not implemented yet
        pass
    elif moves[q][3] == '035':
        moveDict[moves[q][2]]['selfBuffs'][0] = int(moves[q][9]) + 200
        moveDict[moves[q][2]]['selfBuffs'][1] = 0 - int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][2] = int(moves[q][9]) + 200
        moveDict[moves[q][2]]['selfBuffs'][3] = 0 - int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][4] = int(moves[q][9]) + 200
    elif moves[q][3] == '036':
        moveDict[moves[q][2]]['selfBuffs'][0] = int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][4] = int(moves[q][9]) + 200
    elif moves[q][3] == '037':
        moveDict[moves[q][2]]['selfBuffs'][random.randint(0,4)] = int(moves[q][9])
    elif moves[q][3] == '038':
        moveDict[moves[q][2]]['selfBuffs'][1] = int(moves[q][9]) + 300
    elif moves[q][3] == '039':
        moveDict[moves[q][2]]['selfBuffs'][2] = int(moves[q][9]) + 300
    elif moves[q][3] == '03A':
        #belly drum, cut to half health
        moveDict[moves[q][2]]['selfBuffs'][0] = int(moves[q][9]) + 1200
    elif moves[q][3] == '03B':
        moveDict[moves[q][2]]['selfBuffs'][0] = 0 - int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][1] = 0 - int(moves[q][9])
    elif moves[q][3] == '03C':
        moveDict[moves[q][2]]['selfBuffs'][1] = 0 - int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][3] = 0 - int(moves[q][9])
    elif moves[q][3] == '03D':
        moveDict[moves[q][2]]['selfBuffs'][1] = 0 - int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][3] = 0 - int(moves[q][9])
        moveDict[moves[q][2]]['selfBuffs'][4] = 0 - int(moves[q][9])
    elif moves[q][3] == '03E':
        moveDict[moves[q][2]]['selfBuffs'][4] = 0 - int(moves[q][9])
    elif moves[q][3] == '03F':
        moveDict[moves[q][2]]['selfBuffs'][2] = -100 - int(moves[q][9])
    elif moves[q][3] == '040':
        moveDict[moves[q][2]]['targetBuffs'][2] = int(moves[q][9])
        #confuse target
    elif moves[q][3] == '041':
        moveDict[moves[q][2]]['targetBuffs'][0] = int(moves[q][9]) + 200
    elif moves[q][3] == '042':
        moveDict[moves[q][2]]['targetBuffs'][0] = 0 - int(moves[q][9])
    elif moves[q][3] == '043':
        moveDict[moves[q][2]]['targetBuffs'][1] = 0 - int(moves[q][9])
    elif moves[q][3] == '044':
        moveDict[moves[q][2]]['targetBuffs'][4] = 0 - int(moves[q][9])
        #decreases speed for bulldoze? apparently
    elif moves[q][3] == '045':
        moveDict[moves[q][2]]['targetBuffs'][2] = 0 - int(moves[q][9])
    elif moves[q][3] == '046':
        moveDict[moves[q][2]]['targetBuffs'][3] = 0 - int(moves[q][9])
    elif moves[q][3] == '047':
        #decreases accuracy by 1
        pass
    elif moves[q][3] == '048':
        #decreases evasion by 1
        pass
    elif moves[q][3] == '049':
        #this is just defog
        pass
    elif moves[q][3] == '04A':
        moveDict[moves[q][2]]['targetBuffs'][0] = 0 - int(moves[q][9])
        moveDict[moves[q][2]]['targetBuffs'][1] = 0 - int(moves[q][9])
    elif moves[q][3] == '04B':
        moveDict[moves[q][2]]['targetBuffs'][0] = -100 - int(moves[q][9])
    elif moves[q][3] == '04C':
        moveDict[moves[q][2]]['targetBuffs'][1] = -100 - int(moves[q][9])
    elif moves[q][3] == '04D':
        moveDict[moves[q][2]]['targetBuffs'][4] = -100 - int(moves[q][9])
    elif moves[q][3] == '04E':
        #i am not in the mood to add genders rn, that is a can of horses for another day
        pass
    elif moves[q][3] == '04F':
        moveDict[moves[q][2]]['targetBuffs'][3] = -100 - int(moves[q][9])
    #Everything from 050 to 0A4 needs to be implemented first, so we'll figure that out
    elif moves[q][3] == '0A5':
        moveDict[moves[q][2]]['acc'] = 101
    #Everything 0A6 to 126 needs to be implemented lmao
    elif moves[q][3] == '127':
        moveDict[moves[q][2]]['statuses'][2] = int(moves[q][9])
    elif moves[q][3] == '128':
        moveDict[moves[q][2]]['statuses'][0] = int(moves[q][9])
    elif moves[q][3] == '129':
        moveDict[moves[q][2]]['statuses'][1] = int(moves[q][9])
    elif moves[q][3] == '12A':
        #confuse
        pass
    elif moves[q][3] == '12B':
        moveDict[moves[q][2]]['targetBuffs'][1] = -100 - int(moves[q][9])
    #12C to 134 need to be implemented
    elif moves[q][3] == '135':
        moveDict[moves[q][2]]['statuses'][1] = int(moves[q][9])
    elif moves[q][3] == '136':
        moveDict[moves[q][2]]['selfBuffs'][1] = 100 + int(moves[q][9])
    elif moves[q][3] == '137':
        #oh yeah this is that plus/minus ability garbage
        pass
    elif moves[q][3] == '138':
        #more ally stuff
        pass
    elif moves[q][3] == '139':
        moveDict[moves[q][2]]['targetBuffs'][0] = 0 - int(moves[q][9])
    elif moves[q][3] == '13A':
        moveDict[moves[q][2]]['targetBuffs'][0] = 0 - int(moves[q][9])
        moveDict[moves[q][2]]['targetBuffs'][2] = 0 - int(moves[q][9])
    elif moves[q][3] == '13B':
        #some more unimplemented stuff
        pass
    elif moves[q][3] == '13C':
        moveDict[moves[q][2]]['targetBuffs'][2] = 0 - int(moves[q][9])
        moveDict[moves[q][2]]['acc'] = 101
    elif moves[q][3] == '13D':
        moveDict[moves[q][2]]['targetBuffs'][2] = -100 - int(moves[q][9])
    #13E to 158 aren't implemented
    elif moves[q][3] == '159':
        moveDict[moves[q][2]]['statuses'][3] = int(moves[q][9])
    #15A to 15E are unimplemented
    elif moves[q][3] == '15F':
        moveDict[moves[q][2]]['selfBuffs'][1] = 0 - int(moves[q][9])
    #160 to 175 are unimplemented
    elif moves[q][3] == 'FFF':
        moveDict[moves[q][2]]['selfBuffs'][0] = 1200
        moveDict[moves[q][2]]['selfBuffs'][1] = 1200
        moveDict[moves[q][2]]['selfBuffs'][2] = 1200
        moveDict[moves[q][2]]['selfBuffs'][3] = 1200
        moveDict[moves[q][2]]['selfBuffs'][4] = 1200
        moveDict[moves[q][2]]['targetBuffs'][0] = -1200
        moveDict[moves[q][2]]['targetBuffs'][1] = -1200
        moveDict[moves[q][2]]['targetBuffs'][2] = -1200
        moveDict[moves[q][2]]['targetBuffs'][3] = -1200
        moveDict[moves[q][2]]['targetBuffs'][4] = -1200
    if moves[q][10] == 'None':
        target = 1
    elif moves[q][10] == 'User':
        target = 0
    elif moves[q][10] == 'NearAlly':
        target = 0
    elif moves[q][10] == 'UserOrNearAlly':
        target = 0
    elif moves[q][10] == 'UserAndAllies':
        target = 0
    elif moves[q][10] == 'NearFoe':
        target = 1
    elif moves[q][10] == 'AllNearFoes':
        target = 1
    elif moves[q][10] == 'RandomNearFoe':
        target = 1
    elif moves[q][10] == 'Foe':
        target = 1
    elif moves[q][10] == 'AllFoes':
        target = 1
    elif moves[q][10] == 'NearOther':
        target = 1
    elif moves[q][10] == 'AllNearOthers':
        target = 1
    elif moves[q][10] == 'Other':
        target = 1
    elif moves[q][10] == 'AllBattlers':
        target = 1
    elif moves[q][10] == 'UserSide':
        target = 0
    elif moves[q][10] == 'FoeSide':
        target = 1
    elif moves[q][10] == 'BothSides':
        target = 1
    else:
        target = 2
    moveDict[moves[q][2]]['target'] = target
count = 0
# for name, move in moveDict.items():
  # try:
    # if 'sword' in move['name'].lower() or 'earth' in move['name'].lower() or 'dragon' in move['name'].lower():
      # print(name,':',move)
  # except KeyError:
    # print('fuck you')
#Move Dictionary /\/\/\
# for pokemon in pokeDict:
#   print(pokemon)
# for move in moveDict:
#   print(move)
# print([(k, v) for k, v in pokeDict.items()][0])
# print([(k, v) for k, v in moveDict.items()][0])