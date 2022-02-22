import re
totalMats = []
splitMats = {}
with open('PythonFiles/materialList.txt', 'r') as file:
  for line in file:
    material = line.split('png')[1].strip()
    material = material.replace(',', '')
    splitMaterial = re.split(r"(\d+)x", material)[1:]
    splitMaterial[1] = splitMaterial[1].strip()
    splitMaterial[0] = int(splitMaterial[0])
    try:
      splitMats[splitMaterial[1]] += splitMaterial[0]
    except KeyError:
      splitMats[splitMaterial[1]] = splitMaterial[0]
    totalMats.append(material)
print(totalMats)
print(splitMats)
allPossibleMats = ['Gold Ingot', 'Iron Ingot', 'Coal', 'Redstone', 'Diamond', 'Mithril', 'Titanium', 'Corleonite', 'Glacite Jewel', 'Plasma', 'Rough Amber Gemstone', 'Rough Amethyst Gemstone', 'Rough Jade Gemstone', 'Rough Ruby Gemstone', 'Rough Sapphire Gemstone', 'Sludge Juice', 'Treasurite', 'Superlite Motor', 'Synthetic Heart', 'FTX 3070', 'Electron Transmitter', 'Control Switch', 'Robotron Reflector', 'Enchanted Gold', 'Enchanted Iron', 'Enchanted Coal', 'Enchanted Redstone', 'Enchanted Diamond', 'Enchanted Mithril', 'Enchanted Titanium', 'Flawed Amber Gemstone', 'Flawed Amethyst Gemstone', 'Flawed Jade Gemstone', 'Flawed Ruby Gemstone', 'Flawed Sapphire Gemstone']
t2Mats = ['Drill Engine', 'Enchanted Block of Coal', 'Enchanted Diamond Block', 'Enchanted Gold Block', 'Enchanted Iron Block', 'Enchanted Redstone Block', 'Fine Amber Gemstone', 'Fine Amethyst Gemstone', 'Fine Jade Gemstone', 'Fine Ruby Gemstone', 'Fine Sapphire Gemstone', 'Flawless Amber Gemstone', 'Flawless Ruby Gemstone', 'Fuel Tank', 'Gemstone Mixture', 'Golden Plate', 'Mithril Plate', 'Refined Diamond', 'Refined Mithril', 'Refined Titanium']
t2MatDict = {}
for key in sorted(splitMats.keys()):
  if key not in allPossibleMats:
    if key in t2Mats:
      t2MatDict[key] = splitMats[key]
    print('X',key)
    splitMats.pop(key)
list(map(lambda x:print(x,':',splitMats[x]), sorted(splitMats.keys())))
list(map(lambda x:print('T2:',x,':',t2MatDict[x]), sorted(t2MatDict.keys())))