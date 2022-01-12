#gets integer input
housesVisited = int(input("Input an amount of houses to visit. This must be at least 3. "))
#finds the decimal chance to find a dollar
chanceForDollar = 2.0 / housesVisited
#converts into a percent
percentChance = int(100 * chanceForDollar + 0.5)
#prints the chance
print("The chance that you will pull out a dollar is",percentChance,"%")
