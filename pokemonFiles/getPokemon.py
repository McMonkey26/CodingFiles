import PySimpleGUI as sg
import pokemonGUI as pGUI
import pokemonLookUp as pLookUp

print = sg.Print

pokemon1 = sg.InputText('Pokemon 1', size=(30,1), key='pokemon1')
lvl1 = sg.InputText('Level', size=(5,1), pad=(10,3), key='lvl1')
poke1move1Name = sg.InputText('Move 1', size=(40,1), key='name11')
poke1move2Name = sg.InputText('Move 2', size=(40,1), key='name21')
poke1move3Name = sg.InputText('Move 3', size=(40,1), key='name31')
poke1move4Name = sg.InputText('Move 4', size=(40,1), key='name41')
pokemon2 = sg.InputText('Pokemon 2', size=(30,1), key='pokemon2')
lvl2 = sg.InputText('Level', size=(5,1), pad=(10,3), key='lvl2')
poke2move1Name = sg.InputText('Move 1', size=(40,1), key='name12')
poke2move2Name = sg.InputText('Move 2', size=(40,1), key='name22')
poke2move3Name = sg.InputText('Move 3', size=(40,1), key='name32')
poke2move4Name = sg.InputText('Move 4', size=(40,1), key='name42')

Evs1 = [0,0,0,0,0,0]
spins1 = ['hpS1', 'atkS1', 'defS1', 'spaS1', 'spdS1', 'speS1']
hpEv1 = sg.Button('HP', size=(5,1), pad=(0,3), key='hp1')
atkEv1 = sg.Button('Atk', size=(5,1), pad=(0,3), key='atk1')
defEv1 = sg.Button('Def', size=(5,1), pad=(0,3), key='def1')
spaEv1 = sg.Button('Spa', size=(5,1), pad=(0,3), key='spa1')
spdEv1 = sg.Button('Spd', size=(5,1), pad=(0,3), key='spd1')
speEv1 = sg.Button('Spe', size=(5,1), pad=(0,3), key='spe1')
hpSpin1 = sg.Spin(list(range(256)), enable_events=True, size=(4,1), pad=(0,3), key='hpS1')
atkSpin1 = sg.Spin(list(range(256)), enable_events=True, size=(4,1), pad=(0,3), key='atkS1')
defSpin1 = sg.Spin(list(range(256)), enable_events=True, size=(4,1), pad=(0,3), key='defS1')
spaSpin1 = sg.Spin(list(range(256)), enable_events=True, size=(4,1), pad=(0,3), key='spaS1')
spdSpin1 = sg.Spin(list(range(256)), enable_events=True, size=(4,1), pad=(0,3), key='spdS1')
speSpin1 = sg.Spin(list(range(256)), enable_events=True, size=(4,1), pad=(0,3), key='speS1')
slider1 = sg.Slider(orientation = 'horizontal', range = (0,255), key='stat1', enable_events = True, size=(35,5))
chosenStat1 = 0

Evs2 = [0,0,0,0,0,0]
spins2 = ['hpS2', 'atkS2', 'defS2', 'spaS2', 'spdS2', 'speS2']
hpEv2 = sg.Button('HP', size=(5,1), pad=(0,3), key='hp2')
atkEv2 = sg.Button('Atk', size=(5,1), pad=(0,3), key='atk2')
defEv2 = sg.Button('Def', size=(5,1), pad=(0,3), key='def2')
spaEv2 = sg.Button('Spa', size=(5,1), pad=(0,3), key='spa2')
spdEv2 = sg.Button('Spd', size=(5,1), pad=(0,3), key='spd2')
speEv2 = sg.Button('Spe', size=(5,1), pad=(0,3), key='spe2')
hpSpin2 = sg.Spin(list(range(256)), enable_events=True, size=(4,1), pad=(0,3), key='hpS2')
atkSpin2 = sg.Spin(list(range(256)), enable_events=True, size=(4,1), pad=(0,3), key='atkS2')
defSpin2 = sg.Spin(list(range(256)), enable_events=True, size=(4,1), pad=(0,3), key='defS2')
spaSpin2 = sg.Spin(list(range(256)), enable_events=True, size=(4,1), pad=(0,3), key='spaS2')
spdSpin2 = sg.Spin(list(range(256)), enable_events=True, size=(4,1), pad=(0,3), key='spdS2')
speSpin2 = sg.Spin(list(range(256)), enable_events=True, size=(4,1), pad=(0,3), key='speS2')
slider2 = sg.Slider(orientation = 'horizontal', range = (0,255), key='stat2', enable_events = True, size=(35,5))
chosenStat2 = 0

lColumn = [[pokemon1,lvl1],[hpEv1, atkEv1, defEv1, spaEv1, spdEv1, speEv1],[hpSpin1,atkSpin1,defSpin1,spaSpin1,spdSpin1,speSpin1],[slider1],[poke1move1Name],[poke1move2Name],[poke1move3Name],[poke1move4Name]]
rColumn = [[pokemon2,lvl2],[hpEv2, atkEv2, defEv2, spaEv2, spdEv2, speEv2],[hpSpin2,atkSpin2,defSpin2,spaSpin2,spdSpin2,speSpin2],[slider2],[poke2move1Name],[poke2move2Name],[poke2move3Name],[poke2move4Name]]
layout = [[sg.Column(lColumn, element_justification = 'c'),sg.VerticalSeparator(),sg.Column(rColumn, element_justification = 'c')],[sg.Submit()]]

#window = sg.Window("Input Pokemon", layout, element_justification = 'c')

while False:
    events, values = window.read()
    if events == sg.WIN_CLOSED:
        break
    if events == 'stat1':
        Evs1[chosenStat1] = values['stat1']
        window[spins1[chosenStat1]].update(values['stat1'])
    if events == 'hp1':
        chosenStat1 = 0
    if events == 'atk1':
        chosenStat1 = 1
    if events == 'def1':
        chosenStat1 = 2
    if events == 'spa1':
        chosenStat1 = 3
    if events == 'spd1':
        chosenStat1 = 4
    if events == 'spe1':
        chosenStat1 = 5
    for i in range(len(spins1)):
        if events == spins1[i]:
            Evs1[i] = values[spins1[i]]
        if events == spins2[i]:
            Evs2[i] = values[spins2[i]]
    window['stat1'].update(Evs1[chosenStat1])
    if events == 'stat2':
        Evs2[chosenStat2] = values['stat2']
        window[spins2[chosenStat2]].update(values['stat2'])
    if events == 'hp2':
        chosenStat2 = 0
    if events == 'atk2':
        chosenStat2 = 1
    if events == 'def2':
        chosenStat2 = 2
    if events == 'spa2':
        chosenStat2 = 3
    if events == 'spd2':
        chosenStat2 = 4
    if events == 'spe2':
        chosenStat2 = 5
    window['stat2'].update(Evs2[chosenStat2])
    if events == 'Submit':
        if not pGUI.pi.debug:
            pGUI.pokemon[values['pokemon1']] = pLookUp.pokeDict[values['pokemon1']]
            pGUI.pokemon[values['pokemon1']]['lvl'] = values['lvl1']
            pGUI.pokemon[values['pokemon1']]['move1'] = pLookUp.moveDict[values['name11']]
            pGUI.pokemon[values['pokemon1']]['move2'] = pLookUp.moveDict[values['name21']]
            pGUI.pokemon[values['pokemon1']]['move3'] = pLookUp.moveDict[values['name31']]
            pGUI.pokemon[values['pokemon1']]['move4'] = pLookUp.moveDict[values['name41']]
            pGUI.pokemon[values['pokemon1']]['Evs'] = Evs1
            pGUI.pokemon[values['pokemon2']] = pLookUp.pokeDict[values['pokemon2']]
            pGUI.pokemon[values['pokemon2']]['lvl'] = values['lvl2']
            pGUI.pokemon[values['pokemon2']]['move1'] = pLookUp.moveDict[values['name12']]
            pGUI.pokemon[values['pokemon2']]['move2'] = pLookUp.moveDict[values['name22']]
            pGUI.pokemon[values['pokemon2']]['move3'] = pLookUp.moveDict[values['name32']]
            pGUI.pokemon[values['pokemon2']]['move4'] = pLookUp.moveDict[values['name42']]
            pGUI.pokemon[values['pokemon2']]['Evs'] = Evs2
            pGUI.pokeList.append(pGUI.pokemon[values['pokemon1']])
            pGUI.pokeList.append(pGUI.pokemon[values['pokemon2']])
        else:
            pGUI.pokemon['Entei'] = pLookUp.pokeDict['Entei']
            pGUI.pokemon['Entei']['lvl'] = 100
            pGUI.pokemon['Entei']['move1'] = pLookUp.moveDict['Crunch']
            pGUI.pokemon['Entei']['move2'] = pLookUp.moveDict['Solar Beam']
            pGUI.pokemon['Entei']['move3'] = pLookUp.moveDict['Iron Head']
            pGUI.pokemon['Entei']['move4'] = pLookUp.moveDict['Sacred Fire']
            pGUI.pokemon['Entei']['Evs'] = [0,252,0,4,0,252]
            pGUI.pokemon['Suicune'] = pLookUp.pokeDict['Suicune']
            pGUI.pokemon['Suicune']['lvl'] = 100
            pGUI.pokemon['Suicune']['move1'] = pLookUp.moveDict['Air Slash']
            pGUI.pokemon['Suicune']['move2'] = pLookUp.moveDict['Ice Beam']
            pGUI.pokemon['Suicune']['move3'] = pLookUp.moveDict['Liquidation']
            pGUI.pokemon['Suicune']['move4'] = pLookUp.moveDict['Body Slam']
            pGUI.pokemon['Suicune']['Evs'] = [252,4,0,252,0,0]
            pGUI.pokeList.append(pGUI.pokemon['Entei'])
            pGUI.pokeList.append(pGUI.pokemon['Suicune'])
        window.close()
        pGUI.openWindow()
        break
#window.close()
