import json, ssl, io, base64, requests, urllib.request, re, random, fileClassTesting
from urllib.request import Request, urlopen
import nbt.nbt as nbt
import tkinter as tk
from tkinter import ttk, font
import tkinter.tix as tkt
import idlelib.tooltip as tip
from nbtlib.tag import Int
from PIL import ImageTk, Image
debug = True

def stripFormatting(text):
  reg = r'§[a-fk-or0-9]'
  text = re.sub(reg, '', str(text))
  reg = r' *✪+'
  return re.sub(reg, '', text)

def decode_inventory_data(raw):
    return nbt.NBTFile(fileobj = io.BytesIO(base64.b64decode(raw)))

def getUUID(username):
  if debug: print('Getting uuid of player {}:'.format(username))
  url = f'https://api.mojang.com/users/profiles/minecraft/{username}?'
  response = requests.get(url)
  uuid = response.json()['id']
  if debug: print('Got uuid {}.'.format(uuid))
  return uuid

def getUserData(uuid):
  #get data from hypixel api
  ssl._create_default_https_context = ssl._create_unverified_context
  req = Request('https://api.hypixel.net/skyblock/profiles?key=595cec6c-9bac-4299-a769-f7cea97494e4&uuid={}'.format(uuid), headers={'User-Agent': 'Mozilla/5.0'})
  web_byte = urlopen(req).read()
  webpage = web_byte.decode('utf-8')
  webpage = json.loads(webpage)
  if debug: print('Got json data')
  #save data to a file so i can look at it if something goes wrong
  fileName = 'profileData.json'
  file = open(fileName, 'w')
  json.dump(webpage, file, indent=2)
  file.close()
  if debug: print('Saved json data to file {}'.format(fileName))

def changeFont(start, end):
  possChars = ['2','3','4','5','6','7','8','9','0','A','B','C','D','E','F','G','H','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  chosenChar = random.randint(0, len(possChars)-1)
  textBox.delete(start, end)
  textBox.insert(start, possChars[chosenChar])
  textBox.after(10, lambda:changeFont(start, end))
  textBox.tag_add('pinkbold', start, end)

test = open('./properties/absolute_ender_pearl.properties', 'r')
for i in test:
  print(i)
  property = i.split('=')
  if 'ExtraAttributes.id' in property[0]:
    print(property[1])
test.close()
name = 'mcmonkey26'
getUserData(getUUID(name))
#get the data back from the file
profileDataFile = open('profileData.json', 'r')
profileData = json.load(profileDataFile)
profileDataFile.close()
# armorData = decode_inventory_data(profileData['profiles'][0]['members'][getUUID(name)]['talisman_bag']['data'])
armorData = decode_inventory_data(profileData['profiles'][0]['members'][getUUID(name)]['inv_contents']['data'])
file = open('profileData.txt', 'w')
file.write(armorData.pretty_tree())
file.close()
lore = []
lore.append(str(armorData['i'][1]['tag']['display']['Name'])+'\n')
for i in armorData['i'][1]['tag']['display']['Lore']:
  lore.append(str(i)+'\n')
  # try:
  #   print(i['tag']['ExtraAttributes']['id'])
  # except KeyError:
  #   print('empty slot')
#print(armorData['i'][2]['tag']['ExtraAttributes']['id'])
root = tk.Tk()
tabWindow = ttk.Notebook(root)

textBox = tk.Text(tabWindow, background='black', highlightbackground='black')
invFrame = tk.Frame(tabWindow)
invButtons = []
invItemNames = []
blank_image = tk.PhotoImage()
for i in range(36):
  invButtons.append(tk.Button(invFrame, image=blank_image, text=str(i+1), compound=tk.CENTER))
  invButtons[i].config(width=15, height=15)
  invButtons[i].grid(row=4-i//9, column=i%9, sticky="NWSE")
  try:
    invItemNames.append(stripFormatting(armorData['i'][i]['tag']['display']['Name']))
  except Exception:
    print('no item at slot {}'.format(i))
    invItemNames.append('')
  try:
    img = ImageTk.PhotoImage(Image.open('images/'+str(armorData['i'][i]['tag']['ExtraAttributes']['id'])+'.png'))
    invButtons[i].config(image=img)
    invButtons[i]['text'] = ''
    test = tip.Hovertip(invButtons[i], invItemNames[i], hover_delay=0)
  except FileNotFoundError:
    properties = fileClassTesting.goThroughFolder('./properties')
    fileName = properties[str(armorData['i'][i]['tag']['ExtraAttributes']['id'])]
    print(fileName)
    img = ImageTk.PhotoImage(Image.open('./images/'+fileName+'.png'))
    print('no image for item{}'.format(str(armorData['i'][i]['tag']['ExtraAttributes']['id'])))
  except KeyError:
    print(armorData['i'][i])
testing = tk.Button(tabWindow, text='your mom', command=lambda:print('gay'))
tabWindow.add(textBox, text='tab 1')
tabWindow.add(testing, text='tab 2')
tabWindow.add(invFrame, text='tab 3')
tabWindow.pack()
#textBox.pack()
textFont = font.nametofont('TkTextFont')
defaultFont = font.nametofont('TkDefaultFont')
fixedFont = font.nametofont('TkFixedFont')
textFont.configure(family='Minecraft', size=14)
defaultFont.configure(family='Minecraft', size=14)
fixedFont.configure(family='Minecraft', size=14)
textBox.tag_config('§k', font=font.Font(family='Bodoni Ornaments 47'), foreground='#FF55FF')
textBox.tag_config('§l', font=font.Font(family='Minecraft', weight='bold'))
textBox.tag_config('§m', font=font.Font(family='Minecraft', overstrike=1))
textBox.tag_config('§n', font=font.Font(family='Minecraft', underline=1))
textBox.tag_config('§o', font=font.Font(family='Minecraft', slant='italic'))
textBox.tag_config('§r', foreground='#000000')

textBox.tag_config('§0', foreground='#000000')
textBox.tag_config('§1', foreground='#0000AA')
textBox.tag_config('§2', foreground='#00AA00')
textBox.tag_config('§3', foreground='#00AAAA')
textBox.tag_config('§4', foreground='#AA0000')
textBox.tag_config('§5', foreground='#AA00AA')
textBox.tag_config('§6', foreground='#FFAA00')
textBox.tag_config('§7', foreground='#AAAAAA')
textBox.tag_config('§8', foreground='#555555')
textBox.tag_config('§9', foreground='#5555FF')
textBox.tag_config('§a', foreground='#55FF55')
textBox.tag_config('§b', foreground='#55FFFF')
textBox.tag_config('§c', foreground='#FF5555')
textBox.tag_config('§d', foreground='#FF55FF')
textBox.tag_config('§e', foreground='#FFFF55')
textBox.tag_config('§f', foreground='#FFFFFF')
textBox.tag_config('blackbg', background='#000000')
textBox.tag_config('pinkbold', font=font.Font(family='Minecraft', weight='bold'), foreground='#FF55FF')
for i in range(len(lore)):
  textBox.insert('{}.0'.format(i+2), lore[i])
  lore[i] = lore[i].rstrip('\n')
  # print(lore[i])

reg = r'§[a-fr0-9]'
tagEnd = '1.0'
lastTag = lore[0][0:2]
for lineCount in range(len(lore)):
  # print('test'+lore[lineCount])
  # print(re.findall(reg, lore[lineCount]))
  for match in re.finditer(reg, lore[lineCount]):
    tagStart = tagEnd
    tagEnd = str(str(lineCount+1)+'.'+str(match.start()))
    # print("{}, {}, {}".format(lastTag, tagStart, tagEnd))
    textBox.tag_add(lastTag, tagStart, tagEnd)
    lastIndex = match.start()
    lastTag = match.group()
reg = r'§[a-fk-or0-9]'
count = 0
for line in range(len(textBox.get('1.0', 'end').split('\n'))):
  for match in re.finditer(reg, textBox.get('1.0', 'end').split('\n')[line]):
    start = '{}.{}'.format(line+1, match.start()-count)
    end = '{}.{}'.format(line+1, match.end()-count)
    # print('{}, {}: {}'.format(start, end, textBox.get(start, end)))
    textBox.delete(start, end)
    count += 2
  count = 0
textBox.delete('end-1c', 'end')
textBox.tag_add('blackbg', '1.0', 'end')
textBox.state = 'disabled'
changeFont('31.0', '31.1')
changeFont('31.23', '31.24')
# print(textFont.measure(textBox.get('3.0', '3.end')))
# print('({},{})'.format(len(textBox.get('1.0', 'end').split('\n')), max(map(len, textBox.get('1.0', '8.0').split('\n')))))
textBox['width'] = int(max(map(len, textBox.get('1.0', 'end').split('\n'))))
textBox['height'] = len(textBox.get('1.0', 'end').split('\n'))-1
#class garbage \/\/\/
# class hmm():
#   def __init__(self, **kwargs):
#     for a in kwargs:
#       setattr(self, a, kwargs[a])
#   def show(self):
#     print(vars(self))
# hrm = hmm(legs = '2', gaming = True)
# hrm.show()
# class item():
#   def __init__(self, *name, rarity=None, **kwargs):
#     self.name = name
#     self.rarity = rarity
#     for arg in kwargs:
#       setattr(self, arg, kwargs[arg])
#   def show(self):
#     print(vars(self))
# boots = item(name='Necron\'s Boots', rarity='Mythic', strength=120)
# boots.show()
# leggings = item(name='Necron\'s Leggings', rarity='Mythic', recom=True, dungeon=True, stars=5, hpb=10, reforge='Ancient', gem0={'type':'jasper', 'lvl':'fine'}, gem1={'type':'jasper', 'lvl':'fine'}, enchants={'depth_strider':3, 'ultimate_wisdom':5, 'thorns':3, 'feather_falling':10, 'rejuvenate':5, 'growth':5, 'protection':5})
# leggings.show()
# leggingData = armorData['i'][1]['tag']['ExtraAttributes']
# def humina(humina2):
#   print(humina2,':',type(int(leggingData['enchantments'][humina2].valuestr())))
#   return int(leggingData['enchantments'][humina2].valuestr())
# leggings = item(name=stripFormatting(armorData['i'][1]['tag']['display']['Name']), rarity='Mythic', recom=True, dungeon=True, stars=int(leggingData['dungeon_item_level'].valuestr()), hpb=int(leggingData['hot_potato_count'].valuestr()), reforge=leggingData['modifier'], gem0={'type':'jasper', 'lvl':leggingData['gems']['JASPER_0']}, gem1={'type':leggingData['gems']['COMBAT_0_gem'], 'lvl':leggingData['gems']['COMBAT_0']}, enchants={str(k): humina(str(k)) for k in leggingData['enchantments']})
# leggings.show()
#class garbage /\/\/\
root.mainloop()
# if Int(leggingData['rarity_upgrades'])==1 else False
# if Int(leggingData['dungeon_item_level'])>0 else False