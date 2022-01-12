import PySimpleGUI as sg
import pokemonInput as pi
import os
os.chdir('/Users/jpollack/Desktop/CodingFiles/pokemonFiles')

print = sg.Print

pokemon = {}
pokeList = [{'name': 'Entei', 'types': ['', 'Fire'], 'baseStats': {'hp': 115, 'atk': 115, 'def': 85, 'spa': 90, 'spd': 75, 'spe': 100}, 'lvl': 100, 'item': 'Charcoal', 'Evs': [0, 252, 0, 4, 0, 252], 'Ivs': [31, 31, 31, 31, 31, 31], 'modifiers': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'finalStats': {'hp': 371, 'atk': 329, 'def': 206, 'spa': 217, 'spd': 186, 'spe': 299}, 'move1': {'power': 80, 'acc': 100, 'target': 1, 'category': 'Physical', 'targetBuffs': [0, -20, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Dark', 'name': 'Crunch', 'priority': 0, 'flags': 'abefi'}, 'move2': {'power': 120, 'acc': 100, 'target': 1, 'category': 'Special', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Grass', 'name': 'Solar Beam', 'priority': 0, 'flags': 'bef'}, 'move3': {'power': 80, 'acc': 100, 'target': 1, 'category': 'Physical', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Steel', 'name': 'Iron Head', 'priority': 0, 'flags': 'abe'}, 'move4': {'power': 100, 'acc': 95, 'target': 1, 'category': 'Physical', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [50, 0, 0, 0, 0, 0], 'type': 'Fire', 'name': 'Sacred Fire', 'priority': 0, 'flags': 'befg'}}, {'name': 'Suicune', 'types': ['', 'Water'], 'baseStats': {'hp': 100, 'atk': 75, 'def': 115, 'spa': 90, 'spd': 115, 'spe': 85}, 'lvl': 100, 'item': 'Assault Vest', 'Evs': [252, 4, 0, 252, 0, 0], 'Ivs': [31, 31, 31, 31, 31, 31], 'modifiers': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'finalStats': {'hp': 404, 'atk': 187, 'def': 266, 'spa': 279, 'spd': 266, 'spe': 206}, 'move1': {'power': 75, 'acc': 95, 'target': 1, 'category': 'Special', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Flying', 'name': 'Air Slash', 'priority': 0, 'flags': 'be'}, 'move2': {'power': 85, 'acc': 100, 'target': 1, 'category': 'Physical', 'targetBuffs': [0, -20, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Water', 'name': 'Liquidation', 'priority': 0, 'flags': 'abef'}, 'move3': {'power': 90, 'acc': 100, 'target': 1, 'category': 'Special', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 10, 0, 0, 0, 0], 'type': 'Ice', 'name': 'Ice Beam', 'priority': 0, 'flags': 'bef'}, 'move4': {'power': 85, 'acc': 100, 'target': 1, 'category': 'Physical', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 30, 0, 0, 0], 'type': 'Normal', 'name': 'Body Slam', 'priority': 0, 'flags': 'abef'}}]

#take pokemon base stats and level and turn into actual stats
#later i need to add in EVs and IVs

def makeStat(base, lvl, Ev):
    Iv = 31
    stat = (((2 * base + Iv + (Ev // 4)) * lvl) // 100) + 5
    return stat

def openWindow():
    print('opened window')
    for i in pokeList:
        i['atk'] = makeStat(i['baseStats']['atk'], i['lvl'], i['Evs'][1])
        i['def'] = makeStat(i['baseStats']['def'], i['lvl'], i['Evs'][2])
        i['spa'] = makeStat(i['baseStats']['spa'], i['lvl'], i['Evs'][3])
        i['spd'] = makeStat(i['baseStats']['spd'], i['lvl'], i['Evs'][4])
        i['spe'] = makeStat(i['baseStats']['spe'], i['lvl'], i['Evs'][5])
        i['hp'] = ((2 * i['baseStats']['hp'] + i['Ivs'][0] + i['Evs'][0] // 4) * i['lvl']) // 100 + i['lvl'] + 10
    print(pokeList)
    start = sg.Button('Start', size=(1,2), key='start')
    pokemon1 = sg.Text(pokeList[0]['name'], pad=(70,0), key='poke1name', visible=False)
    pokemon1Image = sg.Image(r'/Users/jpollack/Documents/Java Programs/pokemonBattle/images/'+pokeList[0]['name']+'.png', key='poke1image', visible=False)
    poke1Health = sg.ProgressBar(pokeList[0]['finalStats']['hp'], orientation = 'h', size = (17,10), key = 'health1', visible=False)
    poke1Move1 = sg.Button(pokeList[0]['move1']['name'], size = (10,1), key = 'move1poke1', button_color = ('#FFFFFF',pi.colors[pokeList[0]['move1']['type']]), visible=False)
    poke1Move2 = sg.Button(pokeList[0]['move2']['name'], size = (10,1), key = 'move2poke1', button_color = ('#FFFFFF',pi.colors[pokeList[0]['move2']['type']]), visible=False)
    poke1Move3 = sg.Button(pokeList[0]['move3']['name'], size = (10,1), key = 'move3poke1', button_color = ('#FFFFFF',pi.colors[pokeList[0]['move3']['type']]), visible=False)
    poke1Move4 = sg.Button(pokeList[0]['move4']['name'], size = (10,1), key = 'move4poke1', button_color = ('#FFFFFF',pi.colors[pokeList[0]['move4']['type']]), visible=False)
    poke1column1 = sg.Column([[poke1Move1],[poke1Move3]])
    poke1column2 = sg.Column([[poke1Move2],[poke1Move4]])
    pokemon2 = sg.Text(pokeList[1]['name'], pad=(60,0), key='poke2name', visible=False)
    pokemon2Image = sg.Image(r'/Users/jpollack/Documents/Java Programs/pokemonBattle/images/'+pokeList[1]['name']+'.png', key='poke2image', visible=False)
    poke2Health = sg.ProgressBar(pokeList[1]['finalStats']['hp'], orientation = 'h', size = (17,10), key = 'health2', visible=False)
    poke2Move1 = sg.Button(pokeList[1]['move1']['name'], size = (10,1), key = 'move1poke2', button_color = ('#FFFFFF',pi.colors[pokeList[1]['move1']['type']]), visible=False)
    poke2Move2 = sg.Button(pokeList[1]['move2']['name'], size = (10,1), key = 'move2poke2', button_color = ('#FFFFFF',pi.colors[pokeList[1]['move2']['type']]), visible=False)
    poke2Move3 = sg.Button(pokeList[1]['move3']['name'], size = (10,1), key = 'move3poke2', button_color = ('#FFFFFF',pi.colors[pokeList[1]['move3']['type']]), visible=False)
    poke2Move4 = sg.Button(pokeList[1]['move4']['name'], size = (10,1), key = 'move4poke2', button_color = ('#FFFFFF',pi.colors[pokeList[1]['move4']['type']]), visible=False)
    poke2column1 = sg.Column([[poke2Move1],[poke2Move3]])
    poke2column2 = sg.Column([[poke2Move2],[poke2Move4]])

    lSideColumn = [[pokemon1],[poke1Health],[poke1column1,poke1column2],[pokemon2Image]]
    rSideColumn = [[pokemon1Image],[pokemon2],[poke2Health],[poke2column1,poke2column2]]
    layout = [[sg.Column(lSideColumn, key='lcolumn'),sg.Column(rSideColumn, key='rcolumn')],[sg.Button('Start')]]

    window = sg.Window("Pokemon", layout)
    health1 = window['health1']
    health2 = window['health2']
    poke1maxHp = pokeList[0]['finalStats']['hp']
    poke2maxHp = pokeList[1]['finalStats']['hp']
    makeVisible = [window['poke1name'],window['poke1image'],window['move1poke1'],window['move2poke1'],window['move3poke1'],window['move4poke1'],window['poke2name'],window['poke2image'],window['move1poke2'],window['move2poke2'],window['move3poke2'],window['move4poke2']]
    hasP1Moved = False
    hasP2Moved = False
    while True:
        event, values = window.read()
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        if event == 'Start':
            window['Start'].update(visible=False)
            for i in makeVisible:
                i.update(visible=True)
            health1.update(pokeList[0]['finalStats']['hp'], poke1maxHp, visible=True)
            health2.update(pokeList[1]['finalStats']['hp'], poke2maxHp, visible=True)
        if pokeList[0]['hp'] > 0 and pokeList[1]['hp'] > 0:
            if event == 'move1poke1':
                p1move = pokeList[0]['move1']
                hasP1Moved = True
            if event == 'move2poke1':
                p1move = pokeList[0]['move2']
                hasP1Moved = True
            if event == 'move3poke1':
                p1move = pokeList[0]['move3']
                hasP1Moved = True
            if event == 'move4poke1':
                p1move = pokeList[0]['move4']
                hasP1Moved = True
            if event == 'move1poke2':
                p2move = pokeList[1]['move1']
                hasP2Moved = True
            if event == 'move2poke2':
                p2move = pokeList[1]['move2']
                hasP2Moved = True
            if event == 'move3poke2':
                p2move = pokeList[1]['move3']
                hasP2Moved = True
            if event == 'move4poke2':
                p2move = pokeList[1]['move4']
                hasP2Moved = True
            if(hasP1Moved and hasP2Moved):
                hasP1Moved = False
                hasP2Moved = False
                if pi.changeStat(pokeList[0]['spe'],pokeList[0]['modifiers'][4]) > pi.changeStat(pokeList[1]['spe'],pokeList[1]['modifiers'][4]):
                    pi.attack(pokeList[0],p1move,pokeList[(p1move['target'] + 1) % 2])
                    if pokeList[1]['finalStats']['hp'] > 0 and pokeList[0]['finalStats']['hp'] > 0:
                        pi.attack(pokeList[1],p2move,pokeList[p2move['target'] % 2])
                else:
                    pi.attack(pokeList[1],p2move,pokeList[p2move['target'] % 2])
                    if pokeList[0]['finalStats']['hp'] > 0 and pokeList[1]['finalStats']['hp'] > 0:
                        pi.attack(pokeList[0],p1move,pokeList[(p1move['target'] + 1) % 2])
            elif(hasP1Moved):
                print("Player 2 hasn't moved")
            else:
                print("Player 1 hasn't moved")
        health1.update(pokeList[0]['finalStats']['hp'],poke1maxHp)
        health2.update(pokeList[1]['finalStats']['hp'],poke2maxHp)
    window.close()
