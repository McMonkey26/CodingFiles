import os
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import pokemonLookUp as pLU
import pokemonGUI as pGUI
import battleGUI as bGUI
os.chdir('/Users/jpollack/Desktop/CodingFiles/pokemonFiles')

pokeList = [{'name': 'Entei', 'types': ['Fire', ''], 'baseStats': {'hp': 115, 'atk': 115, 'def': 85, 'spa': 90, 'spd': 75, 'spe': 100}, 'lvl': 100, 'Evs': [0,0,0,0,0,0], 'Ivs': [31,31,31,31,31,31], 'finalStats': {'hp': 0, 'atk': 0, 'def': 0, 'spa': 0, 'spd': 0, 'spe': 0},
'move1': {'power': '80', 'acc': '100', 'target': 1, 'category': 'Physical', 'targetBuffs': [0, -20, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Dark', 'name': 'Crunch', 'priority': 0, 'flags': 'abefi'},
'move2': {'power': '120', 'acc': '100', 'target': 1, 'category': 'Special', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Grass', 'name': 'Solar Beam', 'priority': 0, 'flags': 'bef'},
'move3': {'power': '80', 'acc': '100', 'target': 1, 'category': 'Physical', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Steel', 'name': 'Iron Head', 'priority': 0, 'flags': 'abe'},
'move4': {'power': '100', 'acc': '95', 'target': 1, 'category': 'Physical', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [50, 0, 0, 0, 0, 0], 'type': 'Fire', 'name': 'Sacred Fire', 'priority': 0, 'flags': 'befg'}}]

# [{'name': 'Entei', 'types': ['Fire', ''], 'baseStats': {'hp': 115, 'atk': 115, 'def': 85, 'spa': 100, 'spd': 90, 'spe': 75}, 'modifiers': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'lvl': 100,
# 'move1': {'power': 80, 'acc': 100, 'target': 1, 'category': 'Physical', 'targetBuffs': [0, -20, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Dark', 'name': 'Crunch', 'priority': 0, 'flags': 'abefi'},
# 'move2': {'power': 120, 'acc': 100, 'target': 1, 'category': 'Special', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Grass', 'name': 'Solar Beam', 'priority': 0, 'flags': 'bef'},
# 'move3': {'power': 80, 'acc': 100, 'target': 1, 'category': 'Physical', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Steel', 'name': 'Iron Head', 'priority': 0, 'flags': 'abe'},
# 'move4': {'power': 100, 'acc': 95, 'target': 1, 'category': 'Physical', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [50, 0, 0, 0, 0, 0], 'type': 'Fire', 'name': 'Sacred Fire', 'priority': 0, 'flags': 'befg'},
# 'Evs': [0, 252, 0, 4, 0, 252], 'atk': 329, 'def': 206, 'spa': 237, 'spd': 216, 'spe': 249, 'hp': 340},
# {'name': 'Suicune', 'types': ['Water', ''], 'baseStats': {'hp': 100, 'atk': 75, 'def': 115, 'spa': 85, 'spd': 90, 'spe': 115}, 'modifiers': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'lvl': 100,
# 'move1': {'power': 75, 'acc': 95, 'target': 1, 'category': 'Special', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Flying', 'name': 'Air Slash', 'priority': 0, 'flags': 'be'},
# 'move2': {'power': 90, 'acc': 100, 'target': 1, 'category': 'Special', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 10, 0, 0, 0, 0], 'type': 'Ice', 'name': 'Ice Beam', 'priority': 0, 'flags': 'bef'},
# 'move3': {'power': 85, 'acc': 100, 'target': 1, 'category': 'Physical', 'targetBuffs': [0, -20, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Water', 'name': 'Liquidation', 'priority': 0, 'flags': 'abef'},
# 'move4': {'power': 85, 'acc': 100, 'target': 1, 'category': 'Physical', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 30, 0, 0, 0], 'type': 'Normal', 'name': 'Body Slam', 'priority': 0, 'flags': 'abef'},
# 'Evs': [252, 4, 0, 252, 0, 0], 'atk': 187, 'def': 266, 'spa': 269, 'spd': 216, 'spe': 266, 'hp': 373}]

finalStats = {}
pokeList2 = []

def printDict():
    pokeList2.append({})
    pokeList2[-1]['name'] = widgetArrays['pokemon'+str(notebook.index(notebook.select()))].get()
    pokeList2[-1]['types'] = [widgetArrays['type1'+str(notebook.index(notebook.select()))]['text'], widgetArrays['type2'+str(notebook.index(notebook.select()))]['text']]
    pokeList2[-1]['baseStats'] = {'hp':pokeList[0]['baseStats']['hp'],'atk':pokeList[0]['baseStats']['atk'],'def':pokeList[0]['baseStats']['def'],'spa':pokeList[0]['baseStats']['spa'],'spd':pokeList[0]['baseStats']['spd'],'spe':pokeList[0]['baseStats']['spe']}
    pokeList2[-1]['lvl'] = 100
    pokeList2[-1]['item'] = widgetArrays['item'+str(notebook.index(notebook.select()))].get()
    pokeList2[-1]['Evs'] = [int(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][0].get()), int(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][1].get()), int(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][2].get()), int(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][3].get()), int(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][4].get()), int(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][5].get())]
    pokeList2[-1]['Ivs'] = [int(widgetArrays['ivEntry'+str(notebook.index(notebook.select()))][0].get()), int(widgetArrays['ivEntry'+str(notebook.index(notebook.select()))][1].get()), int(widgetArrays['ivEntry'+str(notebook.index(notebook.select()))][2].get()), int(widgetArrays['ivEntry'+str(notebook.index(notebook.select()))][3].get()), int(widgetArrays['ivEntry'+str(notebook.index(notebook.select()))][4].get()), int(widgetArrays['ivEntry'+str(notebook.index(notebook.select()))][5].get())]
    pokeList2[-1]['modifiers'] = [0,0,0,0,0]
    pokeList2[-1]['statuses'] = [0,0,0,0,0,0]
    pokeList2[-1]['finalStats'] = {'hp':finalStats['hp'], 'atk': finalStats['atk'], 'def': finalStats['def'], 'spa': finalStats['spa'], 'spd': finalStats['spd'], 'spe': finalStats['spe']}
    pokeList2[-1]['move1'] = pLU.moveDict[widgetArrays['mo1'+str(notebook.index(notebook.select()))].get()]
    pokeList2[-1]['move2'] = pLU.moveDict[widgetArrays['mo2'+str(notebook.index(notebook.select()))].get()]
    pokeList2[-1]['move3'] = pLU.moveDict[widgetArrays['mo3'+str(notebook.index(notebook.select()))].get()]
    pokeList2[-1]['move4'] = pLU.moveDict[widgetArrays['mo4'+str(notebook.index(notebook.select()))].get()]
    if(widgetArrays['type1'+str(notebook.index(notebook.select()))]['text'] == ''):
        pokeList2[-1]['types'][0] = widgetArrays['type2'+str(notebook.index(notebook.select()))]['text']
        pokeList2[-1]['types'][1] = ''
    #print(bGUI.pokeList[-1])
def makeStat(event):
    pokeList[0]['Ivs'][0] = int(widgetArrays['ivEntry'+str(notebook.index(notebook.select()))][0].get())
    pokeList[0]['Ivs'][1] = int(widgetArrays['ivEntry'+str(notebook.index(notebook.select()))][1].get())
    pokeList[0]['Ivs'][2] = int(widgetArrays['ivEntry'+str(notebook.index(notebook.select()))][2].get())
    pokeList[0]['Ivs'][3] = int(widgetArrays['ivEntry'+str(notebook.index(notebook.select()))][3].get())
    pokeList[0]['Ivs'][4] = int(widgetArrays['ivEntry'+str(notebook.index(notebook.select()))][4].get())
    pokeList[0]['Ivs'][5] = int(widgetArrays['ivEntry'+str(notebook.index(notebook.select()))][5].get())
    finalStats['hp'] = ((2 * pokeList[0]['baseStats']['hp'] + pokeList[0]['Ivs'][0] + (pokeList[0]['Evs'][0] // 4)) * pokeList[0]['lvl']) // 100 + pokeList[0]['lvl'] + 10
    finalStats['atk'] = (((2 * pokeList[0]['baseStats']['atk'] + pokeList[0]['Ivs'][1] + (pokeList[0]['Evs'][1] // 4)) * pokeList[0]['lvl']) // 100) + 5
    finalStats['def'] = (((2 * pokeList[0]['baseStats']['def'] + pokeList[0]['Ivs'][2] + (pokeList[0]['Evs'][2] // 4)) * pokeList[0]['lvl']) // 100) + 5
    finalStats['spa'] = (((2 * pokeList[0]['baseStats']['spa'] + pokeList[0]['Ivs'][3] + (pokeList[0]['Evs'][3] // 4)) * pokeList[0]['lvl']) // 100) + 5
    finalStats['spd'] = (((2 * pokeList[0]['baseStats']['spd'] + pokeList[0]['Ivs'][4] + (pokeList[0]['Evs'][4] // 4)) * pokeList[0]['lvl']) // 100) + 5
    finalStats['spe'] = (((2 * pokeList[0]['baseStats']['spe'] + pokeList[0]['Ivs'][5] + (pokeList[0]['Evs'][5] // 4)) * pokeList[0]['lvl']) // 100) + 5
    widgetArrays['statEvs'+str(notebook.index(notebook.select()))][0]['text'] = pokeList[0]['Evs'][0]
    widgetArrays['statEvs'+str(notebook.index(notebook.select()))][1]['text'] = pokeList[0]['Evs'][1]
    widgetArrays['statEvs'+str(notebook.index(notebook.select()))][2]['text'] = pokeList[0]['Evs'][2]
    widgetArrays['statEvs'+str(notebook.index(notebook.select()))][3]['text'] = pokeList[0]['Evs'][3]
    widgetArrays['statEvs'+str(notebook.index(notebook.select()))][4]['text'] = pokeList[0]['Evs'][4]
    widgetArrays['statEvs'+str(notebook.index(notebook.select()))][5]['text'] = pokeList[0]['Evs'][5]
    widgetArrays['totalStats'+str(notebook.index(notebook.select()))][0].config(text = finalStats['hp'])
    widgetArrays['totalStats'+str(notebook.index(notebook.select()))][1].config(text = finalStats['atk'])
    widgetArrays['totalStats'+str(notebook.index(notebook.select()))][2].config(text = finalStats['def'])
    widgetArrays['totalStats'+str(notebook.index(notebook.select()))][3].config(text = finalStats['spa'])
    widgetArrays['totalStats'+str(notebook.index(notebook.select()))][4].config(text = finalStats['spd'])
    widgetArrays['totalStats'+str(notebook.index(notebook.select()))][5].config(text = finalStats['spe'])
    widgetArrays['statBarsIcon'+str(notebook.index(notebook.select()))][0]['value'] = finalStats['hp'] * 95 / maxStat[0]
    widgetArrays['statBarsIcon'+str(notebook.index(notebook.select()))][1]['value'] = finalStats['atk'] * 95 / maxStat[1]
    widgetArrays['statBarsIcon'+str(notebook.index(notebook.select()))][2]['value'] = finalStats['def'] * 95 / maxStat[2]
    widgetArrays['statBarsIcon'+str(notebook.index(notebook.select()))][3]['value'] = finalStats['spa'] * 95 / maxStat[3]
    widgetArrays['statBarsIcon'+str(notebook.index(notebook.select()))][4]['value'] = finalStats['spd'] * 95 / maxStat[4]
    widgetArrays['statBarsIcon'+str(notebook.index(notebook.select()))][5]['value'] = finalStats['spe'] * 95 / maxStat[5]
    widgetArrays['statBars'+str(notebook.index(notebook.select()))][0]['value'] = finalStats['hp'] / 714 * 100
    widgetArrays['statBars'+str(notebook.index(notebook.select()))][1]['value'] = finalStats['atk'] / 461 * 100
    widgetArrays['statBars'+str(notebook.index(notebook.select()))][2]['value'] = finalStats['def'] / 559 * 100
    widgetArrays['statBars'+str(notebook.index(notebook.select()))][3]['value'] = finalStats['spa'] / 445 * 100
    widgetArrays['statBars'+str(notebook.index(notebook.select()))][4]['value'] = finalStats['spd'] / 559 * 100
    widgetArrays['statBars'+str(notebook.index(notebook.select()))][5]['value'] = finalStats['spe'] / 499 * 100
    widgetArrays['baseStats'+str(notebook.index(notebook.select()))][0]['text'] = pokeList[0]['baseStats']['hp']
    widgetArrays['baseStats'+str(notebook.index(notebook.select()))][1]['text'] = pokeList[0]['baseStats']['atk']
    widgetArrays['baseStats'+str(notebook.index(notebook.select()))][2]['text'] = pokeList[0]['baseStats']['def']
    widgetArrays['baseStats'+str(notebook.index(notebook.select()))][3]['text'] = pokeList[0]['baseStats']['spa']
    widgetArrays['baseStats'+str(notebook.index(notebook.select()))][4]['text'] = pokeList[0]['baseStats']['spd']
    widgetArrays['baseStats'+str(notebook.index(notebook.select()))][5]['text'] = pokeList[0]['baseStats']['spe']
    widgetArrays['statSliders'+str(notebook.index(notebook.select()))][0].set(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][0].get())
    widgetArrays['statSliders'+str(notebook.index(notebook.select()))][1].set(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][1].get())
    widgetArrays['statSliders'+str(notebook.index(notebook.select()))][2].set(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][2].get())
    widgetArrays['statSliders'+str(notebook.index(notebook.select()))][3].set(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][3].get())
    widgetArrays['statSliders'+str(notebook.index(notebook.select()))][4].set(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][4].get())
    widgetArrays['statSliders'+str(notebook.index(notebook.select()))][5].set(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][5].get())
    pokeList[0]['Evs'][0] = int(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][0].get())
    pokeList[0]['Evs'][1] = int(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][1].get())
    pokeList[0]['Evs'][2] = int(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][2].get())
    pokeList[0]['Evs'][3] = int(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][3].get())
    pokeList[0]['Evs'][4] = int(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][4].get())
    pokeList[0]['Evs'][5] = int(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][5].get())
    printDict()
#'atk': 298, 'def': 238, 'spa': 268, 'spd': 248, 'spe': 218, 'hp': 403
#714,461,559,445,559,499

def changeHp(event):
    widgetArrays['lastVal'+str(notebook.index(notebook.select()))][0] = widgetArrays['currentVal'+str(notebook.index(notebook.select()))][0]
    widgetArrays['currentVal'+str(notebook.index(notebook.select()))][0] = int(event)
    if(sum(widgetArrays['currentVal'+str(notebook.index(notebook.select()))]) > 510):
        widgetArrays['currentVal'+str(notebook.index(notebook.select()))][0] = widgetArrays['lastVal'+str(notebook.index(notebook.select()))][0]
        event = widgetArrays['currentVal'+str(notebook.index(notebook.select()))][0]
    widgetArrays['evEntry'+str(notebook.index(notebook.select()))][0].delete(0, 'end')
    widgetArrays['evEntry'+str(notebook.index(notebook.select()))][0].insert(0, event)
    pokeList[0]['Evs'][0] = int(event)
    makeStat(event)
def changeAtk(event):
    widgetArrays['lastVal'+str(notebook.index(notebook.select()))][1] = widgetArrays['currentVal'+str(notebook.index(notebook.select()))][1]
    widgetArrays['currentVal'+str(notebook.index(notebook.select()))][1] = int(event)
    if(sum(widgetArrays['currentVal'+str(notebook.index(notebook.select()))]) > 510):
        widgetArrays['currentVal'+str(notebook.index(notebook.select()))][1] = widgetArrays['lastVal'+str(notebook.index(notebook.select()))][1]
        event = widgetArrays['currentVal'+str(notebook.index(notebook.select()))][1]
    widgetArrays['evEntry'+str(notebook.index(notebook.select()))][1].delete(0, 'end')
    widgetArrays['evEntry'+str(notebook.index(notebook.select()))][1].insert(0, event)
    pokeList[0]['Evs'][1] = int(event)
    makeStat(event)
def changeDef(event):
    widgetArrays['lastVal'+str(notebook.index(notebook.select()))][2] = widgetArrays['currentVal'+str(notebook.index(notebook.select()))][2]
    widgetArrays['currentVal'+str(notebook.index(notebook.select()))][2] = int(event)
    if(sum(widgetArrays['currentVal'+str(notebook.index(notebook.select()))]) > 510):
        widgetArrays['currentVal'+str(notebook.index(notebook.select()))][2] = widgetArrays['lastVal'+str(notebook.index(notebook.select()))][2]
        event = widgetArrays['currentVal'+str(notebook.index(notebook.select()))][2]
    widgetArrays['evEntry'+str(notebook.index(notebook.select()))][2].delete(0, 'end')
    widgetArrays['evEntry'+str(notebook.index(notebook.select()))][2].insert(0, event)
    pokeList[0]['Evs'][2] = int(event)
    makeStat(event)
def changeSpa(event):
    widgetArrays['lastVal'+str(notebook.index(notebook.select()))][3] = widgetArrays['currentVal'+str(notebook.index(notebook.select()))][3]
    widgetArrays['currentVal'+str(notebook.index(notebook.select()))][3] = int(event)
    if(sum(widgetArrays['currentVal'+str(notebook.index(notebook.select()))]) > 510):
        widgetArrays['currentVal'+str(notebook.index(notebook.select()))][3] = widgetArrays['lastVal'+str(notebook.index(notebook.select()))][3]
        event = widgetArrays['currentVal'+str(notebook.index(notebook.select()))][3]
    widgetArrays['evEntry'+str(notebook.index(notebook.select()))][3].delete(0, 'end')
    widgetArrays['evEntry'+str(notebook.index(notebook.select()))][3].insert(0, event)
    pokeList[0]['Evs'][3] = int(event)
    makeStat(event)
def changeSpd(event):
    widgetArrays['lastVal'+str(notebook.index(notebook.select()))][4] = widgetArrays['currentVal'+str(notebook.index(notebook.select()))][4]
    widgetArrays['currentVal'+str(notebook.index(notebook.select()))][4] = int(event)
    if(sum(widgetArrays['currentVal'+str(notebook.index(notebook.select()))]) > 510):
        widgetArrays['currentVal'+str(notebook.index(notebook.select()))][4] = widgetArrays['lastVal'+str(notebook.index(notebook.select()))][4]
        event = widgetArrays['currentVal'+str(notebook.index(notebook.select()))][4]
    widgetArrays['evEntry'+str(notebook.index(notebook.select()))][4].delete(0, 'end')
    widgetArrays['evEntry'+str(notebook.index(notebook.select()))][4].insert(0, event)
    pokeList[0]['Evs'][4] = int(event)
    makeStat(event)
def changeSpe(event):
    widgetArrays['lastVal'+str(notebook.index(notebook.select()))][5] = widgetArrays['currentVal'+str(notebook.index(notebook.select()))][5]
    widgetArrays['currentVal'+str(notebook.index(notebook.select()))][5] = int(event)
    if(sum(widgetArrays['currentVal'+str(notebook.index(notebook.select()))]) > 510):
        widgetArrays['currentVal'+str(notebook.index(notebook.select()))][5] = widgetArrays['lastVal'+str(notebook.index(notebook.select()))][5]
        event = widgetArrays['currentVal'+str(notebook.index(notebook.select()))][5]
    widgetArrays['evEntry'+str(notebook.index(notebook.select()))][5].delete(0, 'end')
    widgetArrays['evEntry'+str(notebook.index(notebook.select()))][5].insert(0, event)
    pokeList[0]['Evs'][5] = int(event)
    makeStat(event)
def changeSlider(event):
    for i in range(0):
        widgetArrays['statSliders'+str(notebook.index(notebook.select()))][i].set(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][i].get())
        pokeList[0]['Evs'][i] = int(widgetArrays['evEntry'+str(notebook.index(notebook.select()))][i].get())
    makeStat(event)
def clickedStats(event):
    #placeHolderFrame.grid_remove()
    #bottom.grid()
    print(event)
def setPokemon(event):
    pokeList[0] = pLU.pokeDict[widgetArrays['pokemon'+str(notebook.index(notebook.select()))].get().capitalize()]
    widgetArrays['pokeImage'+str(notebook.index(notebook.select()))].delete('all')
    widgetArrays['window'+str(notebook.index(notebook.select()))].testImage = testImage = ImageTk.PhotoImage(Image.open("./dex/" + widgetArrays['pokemon'+str(notebook.index(notebook.select()))].get().lower() + ".png").convert("RGBA"), master = widgetArrays['pokeImage'+str(notebook.index(notebook.select()))])
    widgetArrays['pokeImage'+str(notebook.index(notebook.select()))].create_image(0,0, anchor=tk.NW, image=widgetArrays['window'+str(notebook.index(notebook.select()))].testImage)
    widgetArrays['pokemon'+str(notebook.index(notebook.select()))].delete(0,'end')
    widgetArrays['pokemon'+str(notebook.index(notebook.select()))].insert(0, pokeList[0]['name'])
    if pokeList[0]['types'][1] != '':
        widgetArrays['type1'+str(notebook.index(notebook.select()))]['text'] = pokeList[0]['types'][0]
        widgetArrays['type1'+str(notebook.index(notebook.select()))]['bg'] = pGUI.pi.colors[pokeList[0]['types'][0]]
        widgetArrays['type1'+str(notebook.index(notebook.select()))]['relief'] = 'ridge'
        widgetArrays['type2'+str(notebook.index(notebook.select()))]['text'] = pokeList[0]['types'][1]
        widgetArrays['type2'+str(notebook.index(notebook.select()))]['bg'] = pGUI.pi.colors[pokeList[0]['types'][1]]
        widgetArrays['type2'+str(notebook.index(notebook.select()))]['relief'] = 'ridge'
    else:
        widgetArrays['type1'+str(notebook.index(notebook.select()))]['text'] = ''
        widgetArrays['type1'+str(notebook.index(notebook.select()))]['bg'] = widgetArrays['window'+str(notebook.index(notebook.select()))]['bg']
        widgetArrays['type1'+str(notebook.index(notebook.select()))]['relief'] = 'flat'
        widgetArrays['type2'+str(notebook.index(notebook.select()))]['text'] = pokeList[0]['types'][0]
        widgetArrays['type2'+str(notebook.index(notebook.select()))]['bg'] = pGUI.pi.colors[pokeList[0]['types'][0]]
        widgetArrays['type2'+str(notebook.index(notebook.select()))]['relief'] = 'ridge'
    for i in range(6):
        widgetArrays['evEntry'+str(notebook.index(notebook.select()))][i].delete(0, 'end')
        widgetArrays['evEntry'+str(notebook.index(notebook.select()))][i].insert(0, 0)
        widgetArrays['ivEntry'+str(notebook.index(notebook.select()))][i].delete(0, 'end')
        widgetArrays['ivEntry'+str(notebook.index(notebook.select()))][i].insert(0, 31)
    makeStat('event')
    print('setPokemon'+widgetArrays['pokemon'+str(notebook.index(notebook.select()))].get()+str(event))
def setItem(event):
    print('setItem'+item.get()+str(event))
def setAbil(event):
    print('setAbil'+abil.get()+str(event))
def setMo1(event):
    print('setMo1'+mo1.get()+str(event))
def setMo2(event):
    print('setMo2'+mo2.get()+str(event))
def setMo3(event):
    print('setMo3'+mo3.get()+str(event))
def setMo4(event):
    print('setMo4'+mo4.get()+str(event))
def createPokemonSelector(pokemonNumber):
    global mo1, mo2, mo3, mo4
    currentVal = [0,0,0,0,0,0]
    lastVal = [0,0,0,0,0,0]
    widgetArrays['currentVal'+str(pokemonNumber)] = currentVal
    widgetArrays['lastVal'+str(pokemonNumber)] = lastVal
    window = tk.Frame(fullWindow)
    window.pack()
    frames.append(window)
    widgetArrays['window'+str(pokemonNumber)] = window
    notebook.add(window, text='Pokemon '+str(pokemonNumber))
    print(type(window))
    print(notebook.tab('.!frame', option='text')[-1])
    print(type(notebook.tab('.!frame')))
    ttk.Style(window).theme_use('alt')
    print(ttk.Style(window).theme_names())
    ttk.Style(window).configure('Horizontal.TProgressbar', troughborderwidth = 0, troughcolor = '#F0ECEC')
    ttk.Style(window).configure('white.Horizontal.TProgressbar', troughborderwidth=0, troughcolor = '#FFFFFF')
    window.rowconfigure(0, weight=7)
    window.rowconfigure(1, weight=7)
    window.rowconfigure(2, weight=7)
    window.rowconfigure(3, weight=7)
    window['bg']='#F0ECEC'

    pokeImage = tk.Canvas(window, bd=0, bg=window['bg'], width=120, height=120, highlightcolor=window['bg'], highlightthickness=0)
    #relief = 'flat, groove, raised, ridge, solid, or sunken'
    pokeImage.grid(row=0, column=0, rowspan=3, columnspan=1)
    widgetArrays['pokeImage'+str(pokemonNumber)] = pokeImage
    pokemon = tk.Entry(window, width=10, font=('Helvetica', 24), relief='ridge', highlightcolor = '#F0ECEC', highlightbackground='#F0ECEC')
    pokemon.bind('<Return>', setPokemon)
    pokemon.grid(row=3, column=0, sticky=tk.NS)
    widgetArrays['pokemon'+str(pokemonNumber)] = pokemon
    item = tk.Entry(window, width=10, font=('Helvetica', 24), relief='ridge', highlightcolor = '#F0ECEC', highlightbackground='#F0ECEC')
    item.bind('<Return>', setItem)
    item.grid(row=3, column=1, sticky=tk.NS)
    widgetArrays['item'+str(pokemonNumber)] = item
    abil = tk.Entry(window, width=10, font=('Helvetica', 24), relief='ridge', highlightcolor = '#F0ECEC', highlightbackground='#F0ECEC')
    abil.bind('<Return>', setAbil)
    abil.grid(row=3, column=2, sticky=tk.NS)
    widgetArrays['abil'+str(pokemonNumber)] = abil
    mo1 = tk.Entry(window, width=10, font=('Helvetica', 24), relief='ridge', highlightcolor = '#F0ECEC', highlightbackground='#F0ECEC')
    mo1.bind('<Return>', setMo1)
    mo1.grid(row=0, column=3, sticky=tk.NS)
    widgetArrays['mo1'+str(pokemonNumber)] = mo1
    mo2 = tk.Entry(window, width=10, font=('Helvetica', 24), relief='ridge', highlightcolor = '#F0ECEC', highlightbackground='#F0ECEC')
    mo2.bind('<Return>', setMo2)
    mo2.grid(row=1, column=3, sticky=tk.NS)
    widgetArrays['mo2'+str(pokemonNumber)] = mo2
    mo3 = tk.Entry(window, width=10, font=('Helvetica', 24), relief='ridge', highlightcolor = '#F0ECEC', highlightbackground='#F0ECEC')
    mo3.bind('<Return>', setMo3)
    mo3.grid(row=2, column=3, sticky=tk.NS)
    widgetArrays['mo3'+str(pokemonNumber)] = mo3
    mo4 = tk.Entry(window, width=10, font=('Helvetica', 24), relief='ridge', highlightcolor = '#F0ECEC', highlightbackground='#F0ECEC')
    mo4.bind('<Return>', setMo4)
    mo4.grid(row=3, column=3, sticky=tk.NS)
    widgetArrays['mo4'+str(pokemonNumber)] = mo4

    types = tk.Frame(window, bg=window['bg'])
    types.grid(row=1, column=2, rowspan=2, columnspan=1)
    types.columnconfigure(0, weight=4)
    types.columnconfigure(1, weight=3)
    types.columnconfigure(2, weight=3)
    types.rowconfigure(0, weight=1)
    types.rowconfigure(1, weight=1)
    types.rowconfigure(2, weight=1)
    tk.Label(types, bg=window['bg']).grid(row=0, column=0, rowspan=1, columnspan=3, sticky=tk.EW)
    tk.Label(types, bg=window['bg'], width=5).grid(row=1, column=0, rowspan=1, columnspan=1, sticky=tk.EW)
    type1 = tk.Label(types, bg=window['bg'], fg='white', text='', width=5, relief='flat')
    type1.grid(row=1, column=1, sticky=tk.EW)
    widgetArrays['type1'+str(pokemonNumber)] = type1
    type2 = tk.Label(types, bg='red', fg='white', text='Fire', width=5, relief='ridge')
    type2.grid(row=1, column=2, sticky=tk.EW)
    widgetArrays['type2'+str(pokemonNumber)] = type2
    tk.Label(types, bg=window['bg']).grid(row=2, column=0, rowspan=1, columnspan=3, sticky=tk.EW)

    stats = tk.Frame(window, bg='#FFFFFF', relief='ridge', bd=2)
    stats.columnconfigure(0, weight=1)
    stats.columnconfigure(1, weight=3)
    stats.columnconfigure(2, weight=2)
    stats.rowconfigure(6, weight=4)
    stats.bind('<Button-1>', clickedStats)
    statNames = [
        tk.Label(stats, width=3, text='HP').grid(row=1, column=0),
        tk.Label(stats, width=3, text='Atk').grid(row=2, column=0),
        tk.Label(stats, width=3, text='Def').grid(row=3, column=0),
        tk.Label(stats, width=3, text='Spa').grid(row=4, column=0),
        tk.Label(stats, width=3, text='Spd').grid(row=5, column=0),
        tk.Label(stats, width=3, text='Spe').grid(row=6, column=0)
    ]
    statBarsIcon = [
        ttk.Progressbar(stats, style='white.Horizontal.TProgressbar', orient='horizontal', length=100),
        ttk.Progressbar(stats, style='white.Horizontal.TProgressbar', orient='horizontal', length=100),
        ttk.Progressbar(stats, style='white.Horizontal.TProgressbar', orient='horizontal', length=100),
        ttk.Progressbar(stats, style='white.Horizontal.TProgressbar', orient='horizontal', length=100),
        ttk.Progressbar(stats, style='white.Horizontal.TProgressbar', orient='horizontal', length=100),
        ttk.Progressbar(stats, style='white.Horizontal.TProgressbar', orient='horizontal', length=100)
    ]
    statEvs = [
        tk.Label(stats, width=5, text=''),
        tk.Label(stats, width=5, text=''),
        tk.Label(stats, width=5, text=''),
        tk.Label(stats, width=5, text=''),
        tk.Label(stats, width=5, text=''),
        tk.Label(stats, width=5, text='')
    ]
    for i in range(6):
        stats.rowconfigure(i, weight=4)
        statBarsIcon[i].grid(row=i+1, column=1)
        statEvs[i].grid(row=i+1, column=2)
        #statBarsIcon[i]['value'] = pokeStats[i] * 90 / maxStat[i]
    tk.Label(stats, width=3, text='').grid(row=0, column=0)
    tk.Label(stats, width=10, text='').grid(row=0, column=1)
    evLabel = tk.Label(stats, width=5, text='EV').grid(row=0, column=2)
    stats.grid(row=0, column=4, rowspan = 4, sticky=tk.NS, pady=3)
    placeHolderFrame = ttk.Frame(window)
    placeHolderFrame.grid(row=4, column=0, rowspan=1, columnspan=5)
    for i in range(6):
        tk.Label(placeHolderFrame, bg=window['bg']).grid(row=i, column=0)
    bottom = tk.Frame(window, bg=window['bg'])
    bottom.grid(row=4, column=0, rowspan=1, columnspan=5)
    bottom.columnconfigure(0, weight=1)
    bottom.columnconfigure(1, weight=1)
    bottom.columnconfigure(2, weight=4)
    bottom.columnconfigure(3, weight=1)
    bottom.columnconfigure(4, weight=5)
    bottom.columnconfigure(5, weight=1)
    bottom.columnconfigure(6, weight=1)

    tk.Label(bottom, bg=window['bg']).grid(row=0, column=0, columnspan = 7, sticky = tk.EW)
    #[Stat, Base, Progressbar, Input, Slider, Input, Total]
    statNames = [
        tk.Label(bottom, width=5, bg=window['bg'], text='HP').grid(row=1, column=00, sticky = tk.NS),
        tk.Label(bottom, width=5, bg=window['bg'], text='Attack').grid(row=2, column=00, sticky = tk.NS),
        tk.Label(bottom, width=5, bg=window['bg'], text='Defence').grid(row=3, column=00, sticky = tk.NS),
        tk.Label(bottom, width=5, bg=window['bg'], text='Sp. Atk.').grid(row=4, column=00, sticky = tk.NS),
        tk.Label(bottom, width=5, bg=window['bg'], text='Sp. Def.').grid(row=5, column=00, sticky = tk.NS),
        tk.Label(bottom, width=5, bg=window['bg'], text='Speed').grid(row=6, column=0, sticky = tk.NS)
    ]
    baseStats = [
        tk.Label(bottom, width=4, bg=window['bg'], text=pokeList[0]['baseStats']['hp']),
        tk.Label(bottom, width=4, bg=window['bg'], text=pokeList[0]['baseStats']['atk']),
        tk.Label(bottom, width=4, bg=window['bg'], text=pokeList[0]['baseStats']['def']),
        tk.Label(bottom, width=4, bg=window['bg'], text=pokeList[0]['baseStats']['spa']),
        tk.Label(bottom, width=4, bg=window['bg'], text=pokeList[0]['baseStats']['spd']),
        tk.Label(bottom, width=4, bg=window['bg'], text=pokeList[0]['baseStats']['spe'])
    ]
    statBars = [
        ttk.Progressbar(bottom, orient='horizontal', length=240),
        ttk.Progressbar(bottom, orient='horizontal', length=240),
        ttk.Progressbar(bottom, orient='horizontal', length=240),
        ttk.Progressbar(bottom, orient='horizontal', length=240),
        ttk.Progressbar(bottom, orient='horizontal', length=240),
        ttk.Progressbar(bottom, orient='horizontal', length=240)
    ]
    evEntry = [
        tk.Entry(bottom, width=4, highlightbackground=window['bg']),
        tk.Entry(bottom, width=4, highlightbackground=window['bg']),
        tk.Entry(bottom, width=4, highlightbackground=window['bg']),
        tk.Entry(bottom, width=4, highlightbackground=window['bg']),
        tk.Entry(bottom, width=4, highlightbackground=window['bg']),
        tk.Entry(bottom, width=4, highlightbackground=window['bg'])
    ]
    statSliders = [
        tk.Scale(bottom, from_=0, to=252, orient='horizontal', length=325, showvalue=0, bd=0, sliderlength=15, resolution=4, command=changeHp),
        tk.Scale(bottom, from_=0, to=252, orient='horizontal', length=325, showvalue=0, bd=0, sliderlength=15, resolution=4, command=changeAtk),
        tk.Scale(bottom, from_=0, to=252, orient='horizontal', length=325, showvalue=0, bd=0, sliderlength=15, resolution=4, command=changeDef),
        tk.Scale(bottom, from_=0, to=252, orient='horizontal', length=325, showvalue=0, bd=0, sliderlength=15, resolution=4, command=changeSpa),
        tk.Scale(bottom, from_=0, to=252, orient='horizontal', length=325, showvalue=0, bd=0, sliderlength=15, resolution=4, command=changeSpd),
        tk.Scale(bottom, from_=0, to=252, orient='horizontal', length=325, showvalue=0, bd=0, sliderlength=15, resolution=4, command=changeSpe)
    ]
    ivEntry = [
        tk.Entry(bottom, width=4, highlightbackground=window['bg']),
        tk.Entry(bottom, width=4, highlightbackground=window['bg']),
        tk.Entry(bottom, width=4, highlightbackground=window['bg']),
        tk.Entry(bottom, width=4, highlightbackground=window['bg']),
        tk.Entry(bottom, width=4, highlightbackground=window['bg']),
        tk.Entry(bottom, width=4, highlightbackground=window['bg'])
    ]
    #BA5
    totalStats = [
        tk.Label(bottom, bg=window['bg'], width=4),
        tk.Label(bottom, bg=window['bg'], width=4),
        tk.Label(bottom, bg=window['bg'], width=4),
        tk.Label(bottom, bg=window['bg'], width=4),
        tk.Label(bottom, bg=window['bg'], width=4),
        tk.Label(bottom, bg=window['bg'], width=4)
    ]
    for i in range(6):
        baseStats[i].grid(row=i+1, column=1, sticky = tk.NS)
        statBars[i].grid(row=i+1, column=2)
        evEntry[i].grid(row=i+1, column=3)
        evEntry[i].insert(i+1, '0')
        evEntry[i].bind('<Return>', changeSlider)
        statSliders[i].grid(row=i+1, column=4)
        ivEntry[i].grid(row=i+1, column=5)
        ivEntry[i].insert(i+1, '31')
        ivEntry[i].bind('<Return>', makeStat)
        totalStats[i].grid(row=i+1, column=6, sticky=tk.NS)
    widgetArrays['statNames'+str(pokemonNumber)] = statNames
    widgetArrays['statBarsIcon'+str(pokemonNumber)] = statBarsIcon
    widgetArrays['statEvs'+str(pokemonNumber)] = statEvs
    widgetArrays['baseStats'+str(pokemonNumber)] = baseStats
    widgetArrays['statBars'+str(pokemonNumber)] = statBars
    widgetArrays['evEntry'+str(pokemonNumber)] = evEntry
    widgetArrays['statSliders'+str(pokemonNumber)] = statSliders
    widgetArrays['ivEntry'+str(pokemonNumber)] = ivEntry
    widgetArrays['totalStats'+str(pokemonNumber)] = totalStats
    makeStat('a')
    tk.Button(window, text='button', command=printDict).grid(row=1, column=1)
    bottom.grid_remove()
    bottom.grid()
    placeHolderFrame.grid_remove()
    pokemon.insert(0, 'Entei')
    setPokemon('start')
    pokeImage.create_image(0,0, anchor=tk.NW, image=ImageTk.PhotoImage(Image.open("./gen5/" + pokemon.get().lower() + ".png").convert("RGBA"), master = widgetArrays['pokeImage'+str(notebook.index(notebook.select()))]))
def startGame():
  bGUI.pokeList.append(pokeList2[2])
  bGUI.pokeList.append(pokeList2[-1])
  makeStat('4')
  bGUI.makeBattle(fullWindow)

maxStat = [714,461,559,445,559,499]
fullWindow = tk.Tk()
notebook = ttk.Notebook(fullWindow)
notebook.pack()
frames = []
widgetArrays = {}
tk.Button(fullWindow, text='Play Battle', command=startGame).pack()
createPokemonSelector(0)
createPokemonSelector(1)
fullWindow.mainloop()
