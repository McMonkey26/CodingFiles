from pokemonLookUp import pokeDict, moveDict
from switch import *
def print(*args, **kwargs):
  import os, inspect, builtins
  builtins.print('{:20}'.format(lineFile:=f'{os.path.basename(__file__)}:{inspect.currentframe().f_back.f_lineno}')+' '.join(list(map(lambda x:str(x).replace('\n', '\n{:20}'.format(lineFile)), args))))
class obj(object):
  pass
class pokemon:
  def __init__(self, pokemon, level, *, name=None, evs=[0,0,0,0,0,0], ivs=[0,0,0,0,0,0], nature='Serious'):
    self.id = pokemon
    self.name = name
    self.typeMain = pokeDict[pokemon]['types'][0]
    self.typeSub = pokeDict[pokemon]['types'][1] if not pokeDict[pokemon]['types'][1] == '' else None
    self.level = level
    self.evs = evs
    self.ivs = ivs
    self.bHp = pokeDict[pokemon]['baseStats']['hp']
    self.bAtk = pokeDict[pokemon]['baseStats']['atk']
    self.bDef = pokeDict[pokemon]['baseStats']['def']
    self.bSpa = pokeDict[pokemon]['baseStats']['spa']
    self.bSpd = pokeDict[pokemon]['baseStats']['spd']
    self.bSpe = pokeDict[pokemon]['baseStats']['spe']
    self.atkM = 0
    self.defM = 0
    self.spaM = 0
    self.spdM = 0
    self.speM = 0
    self.stats = [self.atkM, self.defM, self.spaM, self.spdM, self.speM]
    self.status = obj()
    self.status.brn = False
    self.status.frz = False
    self.status.par = False
    self.status.pos = False
    self.status.tox = False
    self.status.slp = False
    switch(nature.lower())
    if case('hardy') or case('docile') or case('bashful') or case('quirky') or case('serious'):
      self.nature = [1,1,1,1,1]
    elif case('lonely'):
      self.nature = [1.1,0.9,1,1,1]
    elif case('adamant'):
      self.nature = [1.1,1,0.9,1,1]
    elif case('naughty'):
      self.nature = [1.1,1,1,0.9,1]
    elif case('brave'):
      self.nature = [1.1,1,1,1,0.9]
    elif case('bold'):
      self.nature = [0.9,1.1,1,1,1]
    elif case('impish'):
      self.nature = [1,1.1,0.9,1,1]
    elif case('lax'):
      self.nature = [1,1.1,1,0.9,1]
    elif case('relaxed'):
      self.nature = [1,1.1,1,1,0.9]
    elif case('modest'):
      self.nature = [0.9,1,1.1,1,1]
    elif case('mild'):
      self.nature = [1,0.9,1.1,1,1]
    elif case('rash'):
      self.nature = [1,1,1.1,0.9,1]
    elif case('quiet'):
      self.nature = [1,1,1.1,1,0.9]
    elif case('calm'):
      self.nature = [0.9,1,1,1.1,1]
    elif case('gentle'):
      self.nature = [1,0.9,1,1.1,1]
    elif case('careful'):
      self.nature = [1,1,0.9,1.1,1]
    elif case('sassy'):
      self.nature = [1,1,1,1.1,0.9]
    elif case('timid'):
      self.nature = [0.9,1,1,1,1.1]
    elif case('hasty'):
      self.nature = [1,0.9,1,1,1.1]
    elif case('jolly'):
      self.nature = [1,1,0.9,1,1.1]
    elif case('naive'):
      self.nature = [1,1,1,0.9,1.1]
    else:
      self.nature = [1,1,1,1,1]
  def getStats(self):
    self.tHp = int((2 * self.bHp + self.ivs[0] + self.evs[0] / 4) * self.level / 100 + self.level + 10)
    self.cHp = self.tHp
    self.tAtk = int(((2 * self.bAtk + self.ivs[1] + self.evs[1]/4) * self.level / 100 + 5) * self.nature[0])
    self.tDef = int(((2 * self.bDef + self.ivs[2] + self.evs[2]/4) * self.level / 100 + 5) * self.nature[1])
    self.tSpa = int(((2 * self.bSpa + self.ivs[3] + self.evs[3]/4) * self.level / 100 + 5) * self.nature[2])
    self.tSpd = int(((2 * self.bSpd + self.ivs[4] + self.evs[4]/4) * self.level / 100 + 5) * self.nature[3])
    self.tSpe = int(((2 * self.bSpe + self.ivs[5] + self.evs[5]/4) * self.level / 100 + 5) * self.nature[4])
  def modifyStats(self):
    self.mAtk = self.changeStat(self.tAtk, self.atkM)
    self.mDef = self.changeStat(self.tDef, self.defM)
    self.mSpa = self.changeStat(self.tSpa, self.spaM)
    self.mSpd = self.changeStat(self.tSpd, self.spdM)
    self.mSpe = self.changeStat(self.tSpe, self.speM)
  def changeStat(self, baseStat, statChange):
    statReturned = baseStat
    if statChange == 0:
        return statReturned
    elif statChange < 0:
        statReturned = (baseStat * 2 / (2 - statChange))
        return statReturned
    else:
        statReturned = (baseStat * (2 + statChange) / 2)
        return statReturned
  def show(self):
    print(vars(self))
# bulbasaur = pokemon('Garchomp', 78, ivs=[24,12,30,16,23,5], evs=[74,190,91,48,84,23], nature='Adamant')
# bulbasaur.getStats()
# bulbasaur.modifyStats()