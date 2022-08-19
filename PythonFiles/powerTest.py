num = 1

with open("/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/PythonFiles/powersOf2.txt") as file:
  for line in file:
    if not 2 ** num == int(line.rstrip()):
      print(2 ** num, int(line.rstrip()))
    print(2 ** num == int(line.rstrip()))
    num += 1