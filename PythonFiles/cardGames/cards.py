import random
class Card:
  def __init__(self, num, suit):
    self.num = num
    self.suit = suit
  def __str__(self):
    return str(self.num)+str(self.suit)
deck = []
for suit in '♠♥♣♦':
  for num in ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']:
    deck.append(Card(num, suit))