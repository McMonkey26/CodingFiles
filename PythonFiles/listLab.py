numList = [1,2,3,4,69]
strList = ["lists","are","very","helpful","."]
wordList = list("gamer")
print(numList)
print(strList)
print(wordList)


print(numList[2])
strList[1] = "dog"
print(strList)


print(len(wordList))


for num in numList:
    print(num)

for i in range(len(numList)):
    print(numList[i])


numList2 = [57,12,-5,32,65,0,15,1,90,72]
print(numList2)
for num in numList2:
    print(num)
print("The even numbers are:")
for num in numList2:
    if(num%2==0):
        print(num)
print("The max is",max(numList2))
print("The minimum is",min(numList2))
print("The average is",sum(numList2) / len(numList2))
