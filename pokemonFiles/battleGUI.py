import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import pokemonLookUp as pLU
import pokemonInput as pi
import os
os.chdir('/Users/jpollack/Desktop/CodingFiles/pokemonFiles')

moveChecks = {'hasMoved0':False, 'hasMoved1': False, 'p0Move': 0, 'p0Move': 0}
def useMove(player, move):
    moveChecks['p'+str(player)+'Move'] = pokeList[player]['move'+str(move)]
    moveChecks['hasMoved'+str(player)] = True
    if(moveChecks['hasMoved0'] and moveChecks['hasMoved1']):
        moveChecks['hasMoved0'] = False
        moveChecks['hasMoved1'] = False
        if pi.changeStat(pokeList[0]['finalStats']['spe'],pokeList[0]['modifiers'][4]) > pi.changeStat(pokeList[1]['finalStats']['spe'],pokeList[1]['modifiers'][4]):
            pi.attack(pokeList[0],moveChecks['p0Move'],pokeList[moveChecks['p0Move']['target'] % 2])
            if pokeList[1]['finalStats']['hp'] > 0 and pokeList[0]['finalStats']['hp'] > 0:
                pi.attack(pokeList[1],moveChecks['p1Move'],pokeList[(moveChecks['p1Move']['target'] + 1) % 2])
        else:
            pi.attack(pokeList[1],moveChecks['p1Move'],pokeList[(moveChecks['p1Move']['target']) % 2])
            if pokeList[0]['finalStats']['hp'] > 0 and pokeList[1]['finalStats']['hp'] > 0:
                pi.attack(pokeList[0],moveChecks['p0Move'],pokeList[(moveChecks['p0Move']['target'] + 1) % 2])
    print(pokeList[0]['name']+':'+str(pokeList[0]['finalStats']['hp']))
    print(pokeList[1]['name']+':'+str(pokeList[1]['finalStats']['hp']))

#pokeList = [{'name': 'Entei', 'types': ['', 'Fire'], 'baseStats': {'hp': 115, 'atk': 115, 'def': 85, 'spa': 90, 'spd': 75, 'spe': 100}, 'lvl': 100, 'item': 'Charcoal', 'Evs': [0, 252, 0, 4, 0, 252], 'Ivs': [31, 31, 31, 31, 31, 31], 'modifiers': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'finalStats': {'hp': 371, 'atk': 329, 'def': 206, 'spa': 217, 'spd': 186, 'spe': 299}, 'move1': {'power': 80, 'acc': 100, 'target': 1, 'category': 'Physical', 'targetBuffs': [0, -20, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Dark', 'name': 'Crunch', 'priority': 0, 'flags': 'abefi'}, 'move2': {'power': 120, 'acc': 100, 'target': 1, 'category': 'Special', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Grass', 'name': 'Solar Beam', 'priority': 0, 'flags': 'bef'}, 'move3': {'power': 80, 'acc': 100, 'target': 1, 'category': 'Physical', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Steel', 'name': 'Iron Head', 'priority': 0, 'flags': 'abe'}, 'move4': {'power': 100, 'acc': 95, 'target': 1, 'category': 'Physical', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [50, 0, 0, 0, 0, 0], 'type': 'Fire', 'name': 'Sacred Fire', 'priority': 0, 'flags': 'befg'}}, {'name': 'Suicune', 'types': ['', 'Water'], 'baseStats': {'hp': 100, 'atk': 75, 'def': 115, 'spa': 90, 'spd': 115, 'spe': 85}, 'lvl': 100, 'item': 'Assault Vest', 'Evs': [252, 4, 0, 252, 0, 0], 'Ivs': [31, 31, 31, 31, 31, 31], 'modifiers': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'finalStats': {'hp': 404, 'atk': 187, 'def': 266, 'spa': 279, 'spd': 266, 'spe': 206}, 'move1': {'power': 75, 'acc': 95, 'target': 1, 'category': 'Special', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Flying', 'name': 'Air Slash', 'priority': 0, 'flags': 'be'}, 'move2': {'power': 85, 'acc': 100, 'target': 1, 'category': 'Physical', 'targetBuffs': [0, -20, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 0, 0, 0, 0], 'type': 'Water', 'name': 'Liquidation', 'priority': 0, 'flags': 'abef'}, 'move3': {'power': 90, 'acc': 100, 'target': 1, 'category': 'Special', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 10, 0, 0, 0, 0], 'type': 'Ice', 'name': 'Ice Beam', 'priority': 0, 'flags': 'bef'}, 'move4': {'power': 85, 'acc': 100, 'target': 1, 'category': 'Physical', 'targetBuffs': [0, 0, 0, 0, 0], 'selfBuffs': [0, 0, 0, 0, 0], 'statuses': [0, 0, 30, 0, 0, 0], 'type': 'Normal', 'name': 'Body Slam', 'priority': 0, 'flags': 'abef'}}]
pokeList = []
root = tk.Tk()
root.withdraw()

def onClose():
    root.destroy()

def makeBattle(pastWindow):
    # print(pokeList)
    for i in pokeList:
      print(i)
    pastWindow.destroy()
    window = tk.Toplevel(root)
    window.protocol("WM_DELETE_WINDOW", lambda:root.destroy())
    ttk.Style(window).theme_use('alt')
    for type in pi.colors:
        ttk.Style(window).configure(type+'.TButton', background=pi.colors[type])
    ttk.Style(window).configure('TButton', background='#705746')

    p0m1 = ttk.Button(window, style=pokeList[0]['move1']['type']+'.TButton', text=pokeList[0]['move1']['name'], command=lambda:useMove(0,1))
    p0m2 = ttk.Button(window, style=pokeList[0]['move2']['type']+'.TButton', text=pokeList[0]['move2']['name'], command=lambda:useMove(0,2))
    p0m3 = ttk.Button(window, style=pokeList[0]['move3']['type']+'.TButton', text=pokeList[0]['move3']['name'], command=lambda:useMove(0,3))
    p0m4 = ttk.Button(window, style=pokeList[0]['move4']['type']+'.TButton', text=pokeList[0]['move4']['name'], command=lambda:useMove(0,4))
    p1m1 = ttk.Button(window, style=pokeList[1]['move1']['type']+'.TButton', text=pokeList[1]['move1']['name'], command=lambda:useMove(1,1))
    p1m2 = ttk.Button(window, style=pokeList[1]['move2']['type']+'.TButton', text=pokeList[1]['move2']['name'], command=lambda:useMove(1,2))
    p1m3 = ttk.Button(window, style=pokeList[1]['move3']['type']+'.TButton', text=pokeList[1]['move3']['name'], command=lambda:useMove(1,3))
    p1m4 = ttk.Button(window, style=pokeList[1]['move4']['type']+'.TButton', text=pokeList[1]['move4']['name'], command=lambda:useMove(1,4))
    p0m1.grid(row=2, column=2, sticky=tk.NSEW, ipady=20)
    p0m2.grid(row=2, column=3, sticky=tk.NSEW, ipady=20)
    p0m3.grid(row=3, column=2, sticky=tk.NSEW, ipady=20)
    p0m4.grid(row=3, column=3, sticky=tk.NSEW, ipady=20)
    p1m1.grid(row=0, column=0, sticky=tk.NSEW, ipady=20)
    p1m2.grid(row=0, column=1, sticky=tk.NSEW, ipady=20)
    p1m3.grid(row=1, column=0, sticky=tk.NSEW, ipady=20)
    p1m4.grid(row=1, column=1, sticky=tk.NSEW, ipady=20)
    icon = tk.Button(window, text='nothing here', bg='red', activebackground='red')
    icon.grid(row=0, column=2, rowspan=2, columnspan=2, sticky=tk.NSEW)
    
    tk.Button(window, text='nothing here either', bg='blue').grid(row=2, column=0, rowspan=2, columnspan=2, sticky=tk.NSEW)
    window.mainloop()
