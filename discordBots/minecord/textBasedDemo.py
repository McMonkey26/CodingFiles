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
  def __init__(self, master, name, amount, drop, value):
    self.master = master
    self.name = name
    self.amount = amount
    self.drop = drop
    self.value = value
  def harvest(self):
    print('Harvested {} {}.'.format(self.drop, self.name))
    self.amount += self.drop
  def sell(self, amount):
    try:
      if int(amount) > self.amount:
        print('You do not have that much {}'.format(self.name))
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

class Player:
  def __init__(self):
    self.money = 0
class Tool:
  def __init__(self, tool, level, harvests):
    self.type = tool
    self.level = level
    self.harvests = harvests
  def use(self):
    for material in harvests:
      material.harvest()
player = Player()
oak = Item(player, 'Oak', 5, 3, 10)
stone = Item(player, 'Stone', 0, 2, 1)
for i in range(6):
  stone.harvest()
oak.show()
print(player.money)
oak.harvest()
oak.show()
print(player.money)
oak.sell('4')
oak.show()
print(player.money)
oak.sell('all')
oak.show()
print(player.money)
test = ['a','b','c','d','e','f','g','h']
test1 = ''.join(test[2:5])
print(test)
print(test1)
message = input()
args = message.split()
try:
  if message.startswith('!'):
    args[0] = args[0][1:]
    switch(args[0])
    if case('sell'):
      switch(args[1].lower())
      if case('oak'):
        oak.sell(''.join(args[2:]))
      elif case('stone'):
        stone.sell(''.join(args[2:]))
except IndexError:
  error += '\nInput not long enough'
print('Errors:{}'.format(error))