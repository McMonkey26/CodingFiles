inputFile = open("animals.txt", "r")

fileList = []
for line in inputFile:
    print(line.rstrip("\n"))
    fileList.append(line.rstrip("\n"))
print(fileList)
inputFile.close()

inputAnimal = input("Input an animal: ")
outputFile = open("animals.txt", "a")
if(inputAnimal in fileList):
    print("Your animal is at line",fileList.index(inputAnimal))
else:
    outputFile.write(inputAnimal)
outputFile.close()
