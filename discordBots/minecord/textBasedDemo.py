from switch import *
# Chop Mats: (60s)
# Oak: 10
# Birch: 12
# Spruce: 28
# Jungle: 12
# Acacia: 75
# Crimson: 250
# Charcoal: 49

# Mine Mats: (5s)
# Stone: 1
# Coal: 2
# Iron: 4
# Gold: 6
# Diamond: 9
# Obsidian: 16
# Netherite: 13

# Fight Mats: (40s)
# Rotten Flesh: 12
# Bone: 18
# Gunpowder: 16
# String: 28
# Ender Pearl: 50
# Shulker Shell: 180
# Blaze Rod: 400
error = ''

class Item:
  def __init__(self, master, name, amount, drop, value, type):
    self.master = master
    self.name = name
    self.amount = amount
    self.drop = drop
    self.value = value
    self.type = type
  def harvest(self):
    print('Harvested {} {}.'.format(self.drop, self.name))
    self.amount += self.drop
  def sell(self, amount):
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
    print('Player has ${}.'.format(self.master.money))
  def show(self):
    print(vars(self))

class Tool:
  def __init__(self, name, harvests):
    self.name = name
    self.type = name.split()[1].lower()
    self.level = name.split()[0].lower()
    self.harvests = harvests
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
      '{:20}'.format('')+
      '{:20}'.format('Oak: {}'.format(self.const.oak.amount) if self.const.oak.amount > 0 else ''))
    print(
      '{:20}'.format('Coal: {}'.format(self.const.coal.amount) if self.const.coal.amount > 0 else '')+
      '{:20}'.format('')+
      '{:20}'.format('Birch: {}'.format(self.const.birch.amount) if self.const.birch.amount > 0 else ''))
    print(
      '{:20}'.format('Iron: {}'.format(self.const.iron.amount) if self.const.iron.amount > 0 else '')+
      '{:20}'.format('')+
      '{:20}'.format('Spruce: {}'.format(self.const.spruce.amount) if self.const.spruce.amount > 0 else ''))
  def upgrade(self, type, tool, cost):
    if cost > self.money:
      return None
    switch(type)
    if case('pick'):
      self.pick = tool
    elif case('axe'):
      self.axe = tool
    self.money -= cost
  def use(self, tool):
    switch(tool)
    if case('pick'):
      self.pick.use()
    elif case('axe'):
      self.axe.use()
  def sell(self, material, amt):
    switch(material.lower())
    if case('oak'):
      self.const.oak.sell(amt)
    if case('birch'):
      self.const.birch.sell(amt)
    if case('spruce'):
      self.const.spruce.sell(amt)
    if case('stone'):
      self.const.stone.sell(amt)
    if case('coal'):
      self.const.coal.sell(amt)
    if case('iron'):
      self.const.iron.sell(amt)
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
      self.oak = Item(master, 'Oak', 0, 3, 10, 'wood')
      self.birch = Item(master, 'Birch', 0, 4, 12, 'wood')
      self.spruce = Item(master, 'Spruce', 0, 4, 28, 'wood')
      self.stone = Item(master, 'Stone', 0, 2, 1, 'ore')
      self.coal = Item(master, 'Coal', 0, 3, 2, 'ore')
      self.iron = Item(master, 'Iron', 0, 3, 2, 'ore')
      self.woodPickaxe = Tool('Wood Pickaxe', [self.stone])
      self.stonePickaxe = Tool('Stone Pickaxe', [self.stone, self.coal])
      self.ironPickaxe = Tool('Iron Pickaxe', [self.stone, self.coal, self.iron])
      self.woodAxe = Tool('Wood Axe', [self.oak])
      self.stoneAxe = Tool('Stone Axe', [self.oak, self.birch])
      self.ironAxe = Tool('Iron Axe', [self.birch, self.spruce])
player = Player()
message = input()
while not message == 'stop':
  args = message.split()
  try:
    if message.startswith('!'):
      args[0] = args[0][1:]
      switch(args[0])
      if case('mine') or case('m'):
        player.use('pick')
      elif case('chop') or case('c'):
        player.use('axe')
      elif case('sell') or case('s'):
        player.sell(args[1].lower(), ''.join(args[2:]))
      elif case('buy'):
        pass
      elif case('inventory') or case('inv') or case('i'):
        player.showInv()
  except IndexError:
    error += '\nInput not long enough'
  message = input()
print('Errors:{}'.format(error))