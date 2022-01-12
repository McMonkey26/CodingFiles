import tkinter as tk
from tkinter import font
from switch import *
from PIL import ImageTk, Image
import os, copy
os.chdir('/Users/jpollack/Desktop/CodingFiles/HearthStone')
class card:
  def __init__(self, name, cardType, type=None, *, mana, imageURL, description, **kwargs):
    self.name = name
    self.mana = mana
    self.cardType = cardType
    self.type = type
    self.description = description
    switch(self.cardType)
    if case('minion'):
      self.attack = kwargs['attack']
      self.health = kwargs['health']
    elif case('weapon'):
      self.attack = kwargs['attack']
      self.durability = kwargs['durability']
    elif case('spell'):
      pass
    elif case('hero'):
      self.armor = kwargs['armor']
    self.abilities = {}
    for name, abil in kwargs['abilities'].items():
      self.abilities[name] = abil
  def show(self):
    print('Name:{}'.format(self.name))
    print('Mana:{}'.format(self.mana))
    print('Type:{}'.format(self.type))
    print('Card Type:{}'.format(self.cardType))
    switch(self.cardType)
    if case('minion'):
      print('Damage/Health:{}/{}'.format(self.attack,self.health))
    elif case('weapon'):
      print('Damage/Durability:{}/{}'.format(self.attack,self.durability))
    elif case('spell'):
      pass
    elif case('hero'):
      print('Armor:{}'.format(self.armor))
    try:
      print('Type:{}'.format(self.type))
    except AttributeError:
      pass
    print('Abilities:')
    for name, abil in self.abilities.items():
      if abil == '':
        print(name)
      else:
        print('{}:{}'.format(name, abil))
  def showCard(self, width):
    self.card = []
    self.card.append('┌──────────────────────────────┐')
    nameString = '|'+self.name.center(30)+'|'
    nameString = nameString[:2]+str(self.mana).center(3)+nameString[5:]
    self.card.append(nameString)
    self.card.append('|'+'┌──────────────────┐'.center(30)+'|')
    for _ in range(8):
      self.card.append('|'+'|     NO IMAGE     |'.center(30)+'|')
    self.card.append('|'+'└──────────────────┘'.center(30)+'|')
    tempDesc = [self.description[i:i+25] for i in range(0, len(self.description), 25)]
    self.card.append('|'+' '.center(30)+'|')
    for i in range(3):
      try:
        self.card.append('|'+tempDesc[i].center(30)+'|')
      except IndexError:
        self.card.append('|'+' '.center(30)+'|')
    switch(self.cardType)
    if case('minion'):
      self.card.append('| '+str(self.attack).center(3)+'                      '+str(self.health).center(3)+' |')
    elif case('weapon'):
      self.card.append('| '+str(self.attack).center(3)+'                      '+str(self.durability).center(3)+' |')
    elif case('spell'):
      self.card.append('|'+' ' * 30 + '|')
      pass
    elif case('hero'):
      self.card.append('|                          '+str(self.armor).center(3)+' |')
    self.card.append('└──────────────────────────────┘')
stonetuskBoar = card('Stonetusk Boar', 'minion', type='Beast', mana=1, imageURL='', description='Charge', attack=1, health=1, abilities={'Charge':''})
stonetuskBoar.show()
stonetuskBoar2 = copy.deepcopy(stonetuskBoar)
stonetuskBoar2.name = 'Stonetusk Boar 2'
stonetuskBoar3 = copy.deepcopy(stonetuskBoar)
stonetuskBoar3.name = 'Stonetusk Boar 3'
stonetuskBoar4 = copy.deepcopy(stonetuskBoar)
stonetuskBoar4.name = 'Stonetusk Boar 4'
silverSword = card('Silver Sword', 'weapon', mana=8, imageURL='', description='After your hero attacks, give your minions +1/+1.', attack=3, durability=4, abilities={})

def printMultipleCards(*cards):
  for card in cards:
    card.showCard(1)
  printLength = (len(cards) + 2) // 3 * 19
  tempLines = [' '] * printLength
  cardLines = [cards[i:i+3] for i in range(0, len(cards), 3)]
  layerNum = 0
  for layer in cardLines:
    for card in range(3):
        for line in range(18):
          try:
            tempLines[line+layerNum*19] += layer[card].card[line] + ' '
          except IndexError:
            pass
            # tempLines[line+layerNum*19] += ' ' * 33
    layerNum += 1
  print('|' + ' ' * 110 + '|')
  for line in tempLines:
    print('|'+line.center(110)+'|')
stonetuskBoar.showCard(1)
print('┌' + '─' * 110 + '┐')
for i in stonetuskBoar.card:
  print('|'+i.center(110)+'|')
printMultipleCards(stonetuskBoar, silverSword)#,stonetuskBoar2,stonetuskBoar3, stonetuskBoar4)
print('└' + '─' * 110 + '┘')

def showBoard(playerHero, playerMinions, opponentHero, opponentMinions):
  print('┌' + '─' * 110 + '┐')
  opponentHero.showCard(1)
  for line in opponentHero.card:
    print('|' + line.center(110) + '|')
  print()
  printMultipleCards(opponentMinions)

def attack(attack, defend):
  defend.health -= attack.attack
  attack.health -= defend.health