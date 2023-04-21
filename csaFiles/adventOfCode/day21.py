debug = True
def debugPrint(*args, **kwargs):
  if debug: print(*args, **kwargs)

nums = {}

with open('csaFiles/adventOfCode/day21.txt') as inp:
  for line in inp:
    try:
      int(line[6:].strip())
      nums[line[:4]] = line[6:].strip()
    except ValueError:
      nums[line[:4]] = 'nums[{}] {} nums[{}]'.format(line[6:10], line[11], line[13:17])
curLeft = 1985
while not all([type(nums[i]) == type(1) for i in nums]):
  curLeft = sum([type(nums[i]) != type(1) for i in nums])
  for val in nums:
    try:
      debugPrint(sum([type(nums[i]) != type(1) for i in nums]), nums[val])
      nums[val] = eval(nums[val])
    except NameError:
      pass
    except TypeError:
      pass
  if sum([type(nums[i]) != type(1) for i in nums]) == curLeft:
    print('aaaaa')
    break
print(nums['root'])