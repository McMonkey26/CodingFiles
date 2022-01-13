# https://www.dndbeyond.com/characters/65548079
# https://orkerhulen.dk/onewebmedia/DnD%205e%20Players%20Handbook%20%28BnW%20OCR%29.pdf
# -1 wisdom, +1 charisma
class adventurer:
  def __init__(self, name, race, charClass, health, attack, atkRange, moves=[None, None, None], nickname=None):
    self.name = name
    self.nick = name if nickname == None else nickname
    self.race = race
    self.charClass = charClass
    self.maxHp = health
    self.hp = health
    self.maxStm = 100
    self.stm = 100
    self.dmg = attack
    self.range = atkRange
    self.combat = False
    for i in moves:
      j = i
      setattr(self, i.id, lambda:i.attack(self, j, 'target'))
  def show(self):
    print(self.name,'('+self.nick+')')
    print(self.race+',',self.charClass)
    print('HP:',self.hp,'/',self.maxHp)
    print('Stamina:',self.stm,'/',self.maxStm)
    print('Damage:',self.dmg)
    print('Range:',self.range)
  def attack(self, weapon, target):
    print(self.nick,'used',weapon.name,'on',target.nick)
    target.hp -= weapon.damage
    self.stm -= weapon.stamina
class weapon:
  def __init__(self, id, name, type, damage, dType, stamina):
    self.id = id
    self.name = name
    self.type = type
    self.damage = damage
    self.type = dType
    self.stamina = stamina
elvenBlade = weapon('elvenBlade', 'Elven Blade', 'sword', 20, 'Normal', 10)
elvenBow = weapon('elvenBow', 'Elven Bow', 'bow', 10, 'Projectile', 20)
thievesKnife = weapon('thievesKnife', 'Thieve\'s Knive', 'dagger', 5, 'Normal', 3)
print('hrm')
julian = adventurer('Hawk Feather', 'Tabaxi', 'Rogue', 81, 6, 10, [elvenBlade, elvenBow, thievesKnife], 'Hawk')
exAdvent = adventurer('Aragorn', 'Wood Elf', 'Druid', 94, 3, 30, [elvenBlade, elvenBow, thievesKnife])
print('-')
julian.show()
print('-')
exAdvent.show()
print('-')
julian.attack(elvenBow, exAdvent)
world = [[' ']*8]*8
print('-')
julian.show()
print('-')
exAdvent.show()
print('-')