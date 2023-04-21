debug = False
def debugPrint(*args, **kwargs):
  if debug: print(*args, **kwargs)

with open('csaFiles/adventOfCode/day20.txt') as inp:
  list1 = list(map(int, inp.readlines()))
  list2 = [i for i in list1]
for num in range(len(list1)):
  list2.pop(num)
  list2.insert(num+list1[num] % len(list2), list1[num])
ind = list2.index(0)
ind0 = ind+1000
ind1 = ind+2000
ind2 = ind+3000
print(list2[ind0%len(list2)]+list2[ind1%len(list2)]+list2[ind2%len(list2)])