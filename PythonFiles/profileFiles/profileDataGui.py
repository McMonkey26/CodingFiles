import tkinter as tk
from tkinter import font
from tkinter import ttk
import re, random, base64, json, ssl
from urllib.request import Request, urlopen
import _pickle as cPickle

jsonFile = open('profileData.json', 'r')
jsonDict = json.load(jsonFile)
jsonFile.close()
window = tk.Tk()
window.configure(bg='black')

profile = open('profileData.txt', 'r')
lores = []
for i in profile:
    lores.append(i)
    if str(i).startswith('display'):
        j = i.index('Lore')
        lore = i[j+5:]
        lore = lore.replace('//', '////')
        #print(lore)
        lores.append(lore)
profile.close()
testLore = lores[0].split('Â')
print(testLore)
#profile = open('profileData.txt', 'w')
#for i in lores:
#    profile.write(i+'\n')
#profile.close()

text = tk.Text(window, height=32, width=27, background='black', highlightbackground='black')

def changeFont(start, end):
    possChars = ['2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    chosenChar = random.randint(0, len(possChars)-1)
    text.delete(start, end)
    text.insert(start, possChars[chosenChar])
    text.after(10, lambda:changeFont(start, end))
    text.tag_add('pinkbold', start, end)
text.insert('end', 'Ancient Necron\'s Boots ✪✪✪✪✪\n')
text.insert('end', 'Gear Score: 735 (2126)\n')
text.insert('end', 'Strength: +75 (+35) (+231.75)\n')
text.insert('end', 'Crit Chance: +15% (+15%) (+22.5%)\n')
text.insert('end', 'Crit Damage: +56% (+26%) (+173.04%)\n')
text.insert('end', 'Health: +267 (+40) (+7) (+825.03)\n')
text.insert('end', 'Defense: +127 (+20) (+7) (+392.43)\n')
text.insert('end', 'Speed: +6 (+18.54)\n')
text.insert('end', 'Intelligence: +35 (+25) (+108.15)\n')
text.insert('end', '[❁] [⚔]\n')
text.insert('end', '\n')
text.insert('end', 'Wisdom V, Depth Strider III,\n')
text.insert('end', 'Feather Falling X, ​Growth V,\n')
text.insert('end', 'Protection V, Rejuvenate V\n')
text.insert('end', 'Sugar Rush III\n')
text.insert('end', '\n')
text.insert('end', 'Full Set Bonus: Witherborn\n')
text.insert('end', 'Spawns a wither minion every\n')
text.insert('end', '30 seconds up to a maximum\n')
text.insert('end', '1 wither. Your withers will\n')
text.insert('end', 'travel to and explode on nearby\n')
text.insert('end', 'enemies.\n')
text.insert('end', '\n')
text.insert('end', 'Reduces the damage you take from\n')
text.insert('end', 'withers by 10%.\n')
text.insert('end', '\n')
text.insert('end', 'Ancient Bonus\n')
text.insert('end', 'Grants +1 ☠  Crit Damage\n')
text.insert('end', 'per Catacombs level.\n')
text.insert('end', '\n')
text.insert('end', 'a MYTHIC DUNGEON BOOTS a ')
text.pack()

textFont = font.nametofont('TkTextFont')
defaultFont = font.nametofont('TkDefaultFont')
fixedFont = font.nametofont('TkFixedFont')
textFont.configure(family='Minecraft')
defaultFont.configure(family='Minecraft')
fixedFont.configure(family='Minecraft')
text.tag_config('&l', font=font.Font(family='Minecraft', weight='bold'))
text.tag_config('&k', font=font.Font(family='Bodoni Ornaments 47'), foreground='#FF55FF')
text.tag_config('&m', font=font.Font(family='Minecraft', overstrike=1))
text.tag_config('&n', font=font.Font(family='Minecraft', underline=1))
text.tag_config('&o', font=font.Font(family='Minecraft', slant='italic'))
text.tag_config('&r', foreground='#000000')

text.tag_config('&0', foreground='#000000')
text.tag_config('&1', foreground='#0000AA')
text.tag_config('&2', foreground='#00AA00')
text.tag_config('&3', foreground='#00AAAA')
text.tag_config('&4', foreground='#AA0000')
text.tag_config('&5', foreground='#AA00AA')
text.tag_config('&6', foreground='#FFAA00')
text.tag_config('&7', foreground='#AAAAAA')
text.tag_config('&8', foreground='#555555')
text.tag_config('&9', foreground='#5555FF')
text.tag_config('&a', foreground='#55FF55')
text.tag_config('&b', foreground='#55FFFF')
text.tag_config('&c', foreground='#FF5555')
text.tag_config('&d', foreground='#FF55FF')
text.tag_config('&e', foreground='#FFFF55')
text.tag_config('&f', foreground='#FFFFFF')
text.tag_config('blackbg', background='#000000')
text.tag_config('pinkbold', font=font.Font(family='Minecraft', weight='bold'), foreground='#FF55FF')


# text.tag_add('&d', 1.0, 1.22)
# text.tag_add('&6', 1.23, '1.end')
# text.tag_add('&7', 2.0, 2.11)
# text.tag_add('&d', 2.12, 2.15)
# text.tag_add('&8', 2.16, '2.end')
# text.tag_add('&7', 3.0, 3.9)
# text.tag_add('&c', 3.10, 3.13)
# text.tag_add('&9', 3.14, 3.19)
# text.tag_add('&8', 3.19, '3.end')
# text.tag_add('&7', 4.0, 4.12)
# text.tag_add('&c', 4.13, 4.17)
# text.tag_add('&9', 4.18, 4.24)
# text.tag_add('&8', 4.25, '4.end')
# text.tag_add('&7', 5.0, 5.12)
# text.tag_add('&c', 5.13, 5.17)
# text.tag_add('&9', 5.18, 5.24)
# text.tag_add('&8', 5.25, '5.end')


itemData = """&dAncient Necron\'s Boots &6✪&6✪&6✪&6✪&6✪
&7Gear Score: &d735 &8(2126)
&7Strength: &c+75 &9(+35) &8(+231.75)
&7Crit Chance: &c+15% &9(+15%) &8(+22.5%)
&7Crit Damage: &c+56% &9(+26%) &8(+173.04%)
&7Health: &a+267 &e(+40) &9(+7) &8(+825.03)
&7Defense: &a+127 &e(+20) &9(+7) &8(+392.43)
&7Speed: &a+6 &8(+18.54)
&7Intelligence: &a+35 &9(+25) &8(+108.15)
&8[❁] &8[⚔]

Wisdom V&9, &9Depth Strider III&9,
&9Feather Falling X&9, &9Growth V&9,
&9Protection V&9, &9Rejuvenate V
&9Sugar Rush \I\I\I

&6Full Set Bonus: Witherborn
&7Spawns a wither minion every
&7&e30 &7seconds up to a maximum
&7&a1 &7wither. Your withers will
&7travel to and explode on nearby
&7enemies.

&7Reduces the damage you take from
&7withers by &c10%&7.

&9Ancient Bonus
&7Grants &a+1 &9☠  Crit Damage
&9&7per &cCatacombs &7level.

&ka&r MYTHIC DUNGEON BOOTS &ka&r"""

textAdd = re.sub(r'&[a-fk-or0-9]', r'', itemData)
textAdd = re.sub(r'\n', r'\\n', textAdd)
itemDataByLine = itemData.split('\n')
reg = r'&[a-fk-or0-9]'
lineCount = 0
count = 0
lastIndex = 0
lastTag = itemData[0:2]
tagEnd = '1.0'
for line in itemDataByLine:
    lineCount += 1
    count = 0
    for match in re.finditer(reg, line):
        tagStart = tagEnd
        tagEnd = str(str(lineCount)+'.'+str(match.start()-count))
        text.tag_add(lastTag, tagStart, tagEnd)
        lastIndex = match.start()
        lastTag = match.group()
        count += 2
text.tag_add('pinkbold', 31.1, 31.23)
text.tag_add('pinkbold', 12.0, 12.8)
changeFont('31.0', '31.1')
changeFont('31.23', '31.24')
window.mainloop()
