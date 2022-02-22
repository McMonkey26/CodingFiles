import pygame
from constants import *
class Inventory(pygame.sprite.Sprite):
  def __init__(self, adventurer):
    super().__init__()
    self.image = pygame.Surface((tileSize*12, tileSize*3))
    self.image.fill((40, 40, 40))
    self.hpBar = pygame.Surface((tileSize*18/4, tileSize/2))
    self.manaBar = pygame.Surface((tileSize*18/4, tileSize/2))
    self.xpBar = pygame.Surface((tileSize*18/4, tileSize/2))
    self.barBorder = pygame.Surface((tileSize*19/4, tileSize*2))
    self.barBorder.fill((20, 20, 20))
    self.barBorderInside = pygame.Surface((tileSize*18/4, tileSize*7/4))
    self.barBorderInside.fill((40, 40,40))
    self.barBorder.blit(self.barBorderInside, (tileSize*1/8, tileSize*1/8))
    self.weaponBackground = pygame.Surface((tileSize*19/4, tileSize))
    self.weaponBackground.fill((20, 20, 20))
    self.lWeapon = adventurer.moveL.image
    self.rWeapon = adventurer.moveR.image
    self.uWeapon = adventurer.moveU.image
    self.dWeapon = adventurer.moveD.image
    # self.lWeapon = pygame.Surface((tileSize, tileSize))
    # self.rWeapon = pygame.Surface((tileSize, tileSize))
    # self.uWeapon = pygame.Surface((tileSize, tileSize))
    # self.dWeapon = pygame.Surface((tileSize, tileSize))
    self.hpBar.fill((225, 0, 0))
    self.manaBar.fill((88, 88, 217))
    self.xpBar.fill((25, 170, 25))
    # self.lWeapon.fill((60, 60, 60))
    # self.rWeapon.fill((70, 70, 70))
    # self.uWeapon.fill((60, 60, 60))
    # self.dWeapon.fill((70, 70, 70))
    self.image.blit(self.barBorder, (0, 0))
    self.image.blit(self.hpBar, (tileSize*1/8, tileSize*1/8))
    self.image.blit(self.manaBar, (tileSize*1/8, tileSize*6/8))
    self.image.blit(self.xpBar, (tileSize*1/8, tileSize*11/8))
    self.image.blit(self.weaponBackground, (0, tileSize*2))
    self.image.blit(self.lWeapon, (tileSize*0/4, tileSize*2))
    self.image.blit(self.rWeapon, (tileSize*5/4, tileSize*2))
    self.image.blit(self.uWeapon, (tileSize*10/4, tileSize*2))
    self.image.blit(self.dWeapon, (tileSize*15/4, tileSize*2))
