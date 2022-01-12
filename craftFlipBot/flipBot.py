import urllib.request, json, ssl, re, os
os.chdir('/Users/jpollack/Desktop/CodingFiles/craftFlipBot')
ssl._create_default_https_context = ssl._create_unverified_context
priceDataFile = open('priceData.json', 'r')
itemDatas = json.load(priceDataFile)
priceDataFile.close()

priceData = {}
for i in itemDatas.keys():
    priceData[i] = itemDatas[i]['cost']
url = "https://moulberry.codes/lowestbin.json"
response = urllib.request.urlopen(url)
priceData = json.loads(response.read())
priceData['coin'] = 1

url = "https://api.hypixel.net/skyblock/bazaar"
response = urllib.request.urlopen(url)
bazaarData = json.loads(response.read())
costInsta = {}
costOrder = {}
forgeMats = {}
def getForgeMats(itemid):
    url = "https://raw.githubusercontent.com/NotEnoughUpdates/NotEnoughUpdates-REPO/master/items/"+itemid+".json"
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError as exception:
        print(exception,i)
        return "error"
    currentRecipe = json.loads(response.read())
    required = currentRecipe['lore'].index("§eItems Required")
    mats = {}
    for i in range(required+1, len(currentRecipe['lore'])-2):
        # print(currentRecipe['lore'][i]+"i")
        currentItem = re.sub('§[a-zA-Z\\d]','',currentRecipe['lore'][i])
        currentItem = re.sub(',', '', currentItem)
        # print(currentItem+"currentItem1")
        currentItem = re.sub(r' x(\d+)$', r':\1', currentItem)
        # print(currentItem+"currentItem2")
        if re.search(r'Coins?', currentItem):
            currentItem = re.sub(r'([\d,]*) Coins?', 'coin:\\1', currentItem)
            # print(currentItem+'currentItem3')
        mats['mat'+str(i-required-1)] = currentItem
    # print(mats)
    forgeMats[itemid] = mats
    return mats
def getBazaarCost():
    inp = input('Would you like buy/sell order or insta buy/sell prices? ').lower()
    if inp == 'order':
        return True
    elif inp == 'insta':
        return False
    while inp != 'order' and inp != 'insta':
        if inp == 'order':
            return True
        elif inp == 'insta':
            return False
        else:
            inp = input('Please enter "order" or "insta"')

for i in bazaarData['products'].keys():
    costInsta[i.replace(':','-')] = bazaarData['products'][i]['quick_status']['buyPrice']
    costOrder[i.replace(':','-')] = bazaarData['products'][i]['quick_status']['sellPrice']

def recipeCost(itemid):
    global itemList
    itemList = {}
    if itemid not in recipes:
        return 'Not Craftable'
    for item in recipes[itemid]:
        printValues(item, recipes[itemid])
    itemCost = 0
    for x in itemList:
        if x in priceData:
            itemCost += priceData[x] * itemList[x]
    return round(itemCost,2)
def printValues(item, itemDict):
    if ':' in itemDict[item]:
        recipe = itemDict[item].split(':')
        recipe[1] = int(recipe[1])
        if recipe[0] not in itemList.keys():
            itemList[recipe[0]] = recipe[1]
        else:
            itemList[recipe[0]] += recipe[1]
        if(itemDict == recipes['DIVAN_DRILL']):
            return itemList
def getPriceMarginPercent(itemid):
    if recipeCost(itemid) == 'Not Craftable' or recipeCost(itemid) == 0:
        return 0

    return (priceData[itemid] - recipeCost(itemid)) / recipeCost(itemid) * 100
def getPriceMarginFlat(itemid):
    if recipeCost(itemid) == 'Not Craftable' or recipeCost(itemid) == 0:
        return 0
    return int(priceData[itemid] - recipeCost(itemid))

if getBazaarCost():
    for item in costOrder.keys():
        priceData[item] = costOrder[item]
else:
    for item in costInsta.keys():
        priceData[item] = costInsta[item]
def getPrice(itemid):
    if itemid in priceData.keys():
        return priceData[itemid]
    else:
        return 0
infile = open('recipeData.json', 'r')
recipes = json.load(infile)
infile.close()
def getRecipes():
    currentItem = 0
    for i in priceData.keys():
        currentItem += 1
        if currentItem % 50 == 0:
            print(str(round(currentItem / len(priceData.keys()),4)*100)+'%')
        if i not in recipes.keys():
            url = "https://raw.githubusercontent.com/NotEnoughUpdates/NotEnoughUpdates-REPO/master/items/"+i+".json"
            try:
                response = urllib.request.urlopen(url)
            except urllib.error.HTTPError as exception:
                print(exception,i)
                continue
            currentRecipe = json.loads(response.read())
            if 'recipe' in currentRecipe.keys():
                recipes[i] = currentRecipe['recipe']
                if currentItem % 50 == 0:
                    print(i, currentItem)
            elif '§eItems Required' in currentRecipe['lore']:
                print(i, True)
                recipes[i] = getForgeMats(i)

getRecipes()
print(recipes['DIVAN_DRILL'])

for x in priceData.keys():
    itemDatas[x] = {"cost": round(priceData[x],2), "recipeCost": recipeCost(x), "priceMarginPercent": str(round(getPriceMarginPercent(x),2))+'%', "priceMarginFlat": round(getPriceMarginFlat(x),2)}

print(itemDatas['DIVAN_DRILL'])

outfile = open('recipeData.json', 'w')
json.dump(recipes, outfile, indent=2)
outfile.close()
# outfile = open('priceData.json', 'w')
# json.dump(itemDatas, outfile, indent=2)
# outfile.close()
#print(itemDatas)



byPrice = sorted(itemDatas.items(), key = lambda x: x[1]['cost'], reverse=True)
byPercent = sorted(itemDatas.items(), key= lambda x: x[1]['priceMarginPercent'], reverse=True)
byMargin = sorted(itemDatas.items(), key= lambda x: x[1]['priceMarginFlat'], reverse=True)
uniqueForgeMats = []
for x in forgeMats.values():
    for y in x.values():
        if y.split(':')[0] not in uniqueForgeMats:
            uniqueForgeMats.append(y.split(':')[0])
print(uniqueForgeMats)
print(forgeMats)
for i in range(10):
    print(byPrice[i])
#     print(byPercent[i])
#     print(byMargin[i])

#['☘ Fine Jade Gemstone', '⸕ Fine Amber Gemstone', '❈ Fine Amethyst Gemstone', '✎ Fine Sapphire Gemstone', 'Sludge Juice', 'Refined Titanium', 'Titanium Ring', 'Titanium Drill DR-X455', 'Refined Diamond', 'Enchanted Iron Block', 'Mithril Plate', 'Plasma', 'Enchanted Cobblestone', 'Treasurite', 'Refined Mithril', 'Golden Plate', 'Titanium Talisman', 'Gemstone Drill Model LT-522', '✧ Flawless Topaz Gemstone', 'Gemstone Mixture', 'Magma Core', 'Drill Engine', 'Fuel Tank', 'Beacon III', 'Divan Fragment', '❤ Flawless Ruby Gemstone', 'Enchanted Redstone Block', 'Topaz Drill KGR-12', '❁ Flawless Jasper Gemstone', 'Helix', 'coin', 'Titanium Drill DR-X555', 'Corleonite', 'Ruby-polished Drill Engine', 'Sapphire-polished Drill Engine', '⸕ Flawless Amber Gemstone', 'Robotron Reflector', 'Enchanted Gold Block', 'Glacite Jewel', 'Goblin Egg', 'Red Goblin Egg', '❤ Flawed Ruby Gemstone', '❤ Fine Ruby Gemstone', 'Enchanted Ender Pearl', 'Yellow Goblin Egg', '✧ Fine Topaz Gemstone', 'Titanium Artifact', 'Mithril Drill SX-R226', 'Starfall', 'Titanium-Plated Drill Engine', 'Electron Transmitter', 'FTX 3070', 'Beacon IV', 'Titanium Drill DR-X355', 'Mithril', 'Titanium', 'Beacon I', 'Ruby Drill Model TX-15', 'Bejeweled Handle', 'Enchanted Gold', 'Enchanted Block of Coal', "Divan's Alloy", 'Titanium Drill DR-X655', 'Worm Membrane', 'Mithril-Plated Drill Engine', 'Superlite Motor', 'Titanium-Infused Fuel Tank', 'Control Switch', 'Beacon II', 'Green Goblin Egg', 'Gemstone Fuel Tank', 'Synthetic Heart', '☘ Flawless Jade Gemstone', 'Jade Crystal', 'Enchanted Mithril', 'Ruby Crystal', 'Jasper Crystal', 'Enchanted Diamond Block', 'Amber Crystal', '❈ Flawless Amethyst Gemstone', 'Amethyst Crystal', 'Topaz Crystal', 'Enchanted Titanium', '✎ Flawless Sapphire Gemstone', 'Sapphire Crystal']
