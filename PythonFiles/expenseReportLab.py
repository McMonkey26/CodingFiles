inputFile = open("expenseReportList.txt", "r")
list1 = [] #getting list 1 code here
for line in inputFile:
    list1.append(int(line.rstrip("\n")))
inputFile.close()
list2 = list1
for x in list1:
    for y in list2:
        if(x + y == 2020):
            print(x * y,x,y)
