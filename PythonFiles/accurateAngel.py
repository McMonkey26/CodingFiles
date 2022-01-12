import random
import string

possLimbs = ["Eye","Wing","Head","Mouth","Arm","Leg","Finger","Ear"]
amtLimbs = random.randint(0,100)
totalLimbs = []
totalLimbsNum = [0,0,0,0,0,0,0,0]
currentLimb = random.randint(0,len(possLimbs) - 1)
for i in range(amtLimbs):
    totalLimbs.append(possLimbs[currentLimb])
    totalLimbsNum[currentLimb] += 1
    currentLimb = random.randint(0,len(possLimbs) - 1)

totalLimbs.sort()
print(totalLimbs)
print(possLimbs)
print(totalLimbsNum)
