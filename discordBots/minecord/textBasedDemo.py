from switch import switch, case
from playerClass import Player
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
        tool = (temp:=''.join(list(map(lambda x:x.capitalize(), args[1:]))))[0].lower()+temp[1:]
        player.upgrade(vars(player.const)[tool])
      elif case('inventory') or case('inv') or case('i'):
        player.showInv()
      elif case('give'):
        player.money += int(args[1])
  except IndexError:
    error += '\nInput not long enough'
  message = input()
print('Errors:{}'.format(error))