import json, os
os.chdir('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/cspFiles/bigDataProject')

data = []
with open('gen8ou-0-nmod.txt') as file:
  for line in file:
    data.append(line.rstrip('\n'))
data = data[5:705]
line1 = list(map(lambda x:x.strip(), data[0].split('|')))[1:8]
print(line1)
splitData = []
for line in data:
  splitData.append(list(map(lambda x:x.strip(), line.split('|')))[1:8])
print(splitData[-1])
class Pokemon(object):
  def __init__(self, pokemon):
    self.rank = int(pokemon[0])
    self.name = pokemon[1]
    self.usPerc = float(pokemon[2].rstrip('%'))
    self.rawAmt = float(pokemon[3])
    self.rawPerc = float(pokemon[4].rstrip('%'))
    self.realAmt = float(pokemon[5])
    self.realPerc = float(pokemon[6].rstrip('%'))
pokemonObjects = []
for mon in splitData:
  pokemonObjects.append(Pokemon(mon))
lastUs = 0
lastRaw = 0
lastReal = 0
lastDif = 0
lastPoke = 'hrm'
for poke in pokemonObjects:
  currentRaw = poke.rawPerc
  currentUs = poke.usPerc
  try:
    difRaw = lastRaw/currentRaw
    difUs = lastUs/currentUs
  except ZeroDivisionError:
    continue
  if difRaw > lastDif:
    lastDif = difRaw
    # lastPoke = poke.name
  if difUs > lastUs:
    lastUs = difUs
    lastPoke = poke.name
  # if difRaw > 2:
  #   print(poke.name, currentRaw,'%', difRaw,'difference')
  lastRaw = currentRaw
  lastUs = currentUs
print(vars(pokemonObjects[3]))
print(lastPoke)
print(lastDif)