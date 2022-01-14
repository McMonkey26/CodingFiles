from switch import switch, case
import json, os
os.chdir('/Users/jpollack/Desktop/CodingFiles/repos/CodingFiles/discordBots/minecord')
class Item:
  def __init__(self, master, name, drop, value, type):
    self.master = master
    self.name = name
    self.amount = 0
    self.drop = drop
    self.value = value
    self.type = type
  def harvest(self):
    print('Harvested {} {}.'.format(self.drop, self.name))
    self.amount += self.drop
  def sell(self, amount):
    if self.amount == 0:
      return None
    try:
      if int(amount) > self.amount:
        print('You do not have that much {}'.format(self.name))
        return None
      print('Sold {} {} for ${}'.format(int(amount), self.name, self.value * int(amount)))
      self.amount -= int(amount)
      self.master.money += (self.value * int(amount))
    except ValueError:
      if amount == 'all':
        print('Sold {} {} for ${}'.format(self.amount, self.name, self.amount * self.value))
        self.master.money += (self.amount * self.value)
        self.amount = 0
  def show(self):
    print(vars(self))

class Tool:
  def __init__(self, name, harvests, cost):
    self.name = name
    self.type = name.split()[1].lower()
    self.level = name.split()[0].lower()
    self.harvests = harvests
    self.cost = cost
  def use(self):
    for material in self.harvests:
      material.harvest()
class Player:
  def __init__(self):
    self.const = self.Constants(self)
    self.stats = self.Stats()
    self.money = 0
    self.pick = self.const.woodPickaxe
    self.axe = self.const.woodAxe
    self.sword = self.const.woodSword
  def showInv(self):
    print('Tools:')
    print('{:20}Mines: {}'.format(self.pick.name, self.stats.mines))
    print('{:20}Chops: {}'.format(self.axe.name, self.stats.chops))
    print('{:20}Fights: {}'.format('Placeholder Sword', self.stats.fights))
    print()
    print('Money: ${}'.format(self.money))
    print('Level: {}'.format(self.stats.lvl))
    print('XP: {}/{}'.format(self.stats.lvlXp, self.stats.lvlCost))
    print('\n')
    print('{:20}'.format('Ore')+'{:20}'.format('Drops')+'{:20}'.format('Wood'))
    print(
      '{:20}'.format('Stone: {}'.format(self.const.stone.amount) if self.const.stone.amount > 0 else '')+
      '{:20}'.format('Rotten Flesh: {}'.format(self.const.rotten.amount) if self.const.rotten.amount > 0 else '')+
      '{:20}'.format('Oak: {}'.format(self.const.oak.amount) if self.const.oak.amount > 0 else ''))
    print(
      '{:20}'.format('Coal: {}'.format(self.const.coal.amount) if self.const.coal.amount > 0 else '')+
      '{:20}'.format('Bone: {}'.format(self.const.bone.amount) if self.const.bone.amount > 0 else '')+
      '{:20}'.format('Birch: {}'.format(self.const.birch.amount) if self.const.birch.amount > 0 else ''))
    print(
      '{:20}'.format('Iron: {}'.format(self.const.iron.amount) if self.const.iron.amount > 0 else '')+
      '{:20}'.format('Gunpowder: {}'.format(self.const.gunpowder.amount) if self.const.gunpowder.amount > 0 else '')+
      '{:20}'.format('Spruce: {}'.format(self.const.spruce.amount) if self.const.spruce.amount > 0 else ''))
  def upgrade(self, tool):#type, tool, cost):
    if tool.cost > self.money:
      print('too broke L')
      return None
    switch(tool.type)
    if case('pickaxe'):
      self.pick = tool
    elif case('axe'):
      self.axe = tool
    elif case('sword'):
      self.sword = tool
    self.money -= tool.cost
    print('Bought {} for ${}. You now have {}'.format(tool.name, tool.cost, self.money))
  def sell(self, material, amt):
    sold = True
    switch(material.lower())
    if case('oak'):
      self.const.oak.sell(amt)
    elif case('birch'):
      self.const.birch.sell(amt)
    elif case('spruce'):
      self.const.spruce.sell(amt)
    elif case('stone'):
      self.const.stone.sell(amt)
    elif case('coal'):
      self.const.coal.sell(amt)
    elif case('iron'):
      self.const.iron.sell(amt)
    elif case('rotten') or case('rotten'):
      self.const.rotten.sell(amt)
    elif case('bone'):
      self.const.bone.sell(amt)
    elif case('gunpowder'):
      self.const.gunpowder.sell(amt)
    elif case('all'):
      self.const.oak.sell('all')
      self.const.birch.sell('all')
      self.const.spruce.sell('all')
      self.const.stone.sell('all')
      self.const.coal.sell('all')
      self.const.iron.sell('all')
      self.const.rotten.sell('all')
      self.const.bone.sell('all')
      self.const.gunpowder.sell('all')
    else:
      sold = False
      print('Did not recognize {}'.format(material))
    if sold:
      print('Player has ${}'.format(self.money))

  class Stats:
    def __init__(self):
      self.mines = 0
      self.chops = 0
      self.fights = 0
      self.xp = 0
      self.lvl = 1
      self.lvlXp = 0
      self.lvlCost = 1
  class Constants:
    def __init__(self, master):
      self.stone = Item(master, 'Stone', 2, 1, 'ore')
      self.coal = Item(master, 'Coal', 3, 2, 'ore')
      self.iron = Item(master, 'Iron', 3, 2, 'ore')
      self.woodPickaxe = Tool('Wood Pickaxe', [self.stone], 0)
      self.stonePickaxe = Tool('Stone Pickaxe', [self.stone, self.coal], 1000)
      self.ironPickaxe = Tool('Iron Pickaxe', [self.stone, self.coal, self.iron], 7500)
      self.oak = Item(master, 'Oak', 3, 10, 'wood')
      self.birch = Item(master, 'Birch', 4, 12, 'wood')
      self.spruce = Item(master, 'Spruce', 4, 28, 'wood')
      self.woodAxe = Tool('Wood Axe', [self.oak], 0)
      self.stoneAxe = Tool('Stone Axe', [self.oak, self.birch], 1000)
      self.ironAxe = Tool('Iron Axe', [self.birch, self.spruce], 7500)
      self.rotten = Item(master, 'Rotten Flesh', 8, 12, 'drop')
      self.bone = Item(master, 'Bone', 11, 18, 'drop')
      self.gunpowder = Item(master, 'Gunpowder', 7, 16, 'drop')
      self.woodSword = Tool('Wood Sword', [self.rotten], 0)
      self.stoneSword = Tool('Stone Sword', [self.bone], 1000)
      self.ironSword = Tool('Iron Sword', [self.gunpowder], 7500)
stats = {
  'moons':4,
  'choop':16
}
with open('profiles.json','w') as outfile:
  json.dump(stats, outfile, indent=2)
with open('profiles.json', 'r') as infile:
  data = json.load(infile)
  print(data)
b32Ids = [
  '2394AHFD',
  '3KN54379',
  'GHK3245H'
]
b64Ids = [
  'b34DSF67',
  'a8n9SB98',
  'SD90yds0'
]
def testId():
  global ids
  import random
  base32choice = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ234567'
  base64choice = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/'
  newId32 = ''
  newId64 = ''
  for i in range(8):
    newId += random.choice(base32choice)