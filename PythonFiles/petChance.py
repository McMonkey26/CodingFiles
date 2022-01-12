petLevels = int(input('How many tiers of pets are there? '))

petChances = []
possPetsAtLevel = []
currPetsAtLevel = []
chanceForNewPet = []

for i in range(petLevels):
    petChances.append(float(input('What is the chance of a pet at rarity {}? '.format(i))))
    possPetsAtLevel.append(float(input('How many pets are available at rarity {}? '.format(i))))
    currPetsAtLevel.append(float(input('How many pets do you have at rarity {}? '.format(i))))
    chanceForNewPet.append(petChances[i] * (possPetsAtLevel[i]-currPetsAtLevel[i]) / possPetsAtLevel[i])

totalChanceForPet = sum(petChances)
totalChanceForNewPet = sum(chanceForNewPet)
print('You have a {}%% chance to get a pet.'.format(totalChanceForPet))
print('You have a {}%% chance to drop a pet you don\'t already have.'.format(totalChanceForNewPet))
for i in range(petLevels):
    print('You have {}/{} pets at rarity {}. You have a {}%% chance of getting a pet at this rarity, and a {}%% chance of getting a new pet at this rarity.'.format(currPetsAtLevel[i], possPetsAtLevel[i], i, petChances[i], chanceForNewPet[i]))