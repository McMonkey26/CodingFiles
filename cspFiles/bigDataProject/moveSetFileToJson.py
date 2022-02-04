import json, urllib.request, ssl, os
os.chdir('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/cspFiles/bigDataProject')
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.smogon.com/stats/2021-12/moveset/gen8ou-0.txt'
file = urllib.request.urlopen(url)
landorusList = []
dragapult = False
for line in file:
  decoded_line = line.decode('utf-8').strip().strip('|').strip()
  if 'Dragapult' in decoded_line:
    if dragapult:
      break
    dragapult = True
  if decoded_line == '+----------------------------------------+':
    landorusList.append([])
    continue
  landorusList[-1].append(decoded_line)
landorusList = landorusList[:-1]
list(map(lambda x:list(map(print, x)), landorusList))
testList = {'Name':landorusList[0][0]}
testList['Weight'] = {
  'Raw count':landorusList[1][0].split(' ')[-1],
  'Avg. weight':landorusList[1][1].split(' ')[-1],
  'Viability Ceiling':landorusList[1][2].split(' ')[-1]
}
testList['Abilities'] = {}
for line in landorusList[2]:
  if line == 'Abilities':
    continue
  else:
    testList['Abilities'][' '.join(line.split(' ')[:-1])] = line.split(' ')[-1]
testList['Items'] = {}
for line in landorusList[3]:
  if line == 'Items':
    continue
  else:
    testList['Items'][' '.join(line.split(' ')[:-1])] = line.split(' ')[-1]
testList['Spreads'] = {}
for line in landorusList[4]:
  if line == 'Spreads':
    continue
  else:
    testList['Spreads'][line.split(' ')[0]] = line.split(' ')[1]
testList['Moves'] = {}
for line in landorusList[5]:
  if line == 'Moves':
    continue
  else:
    testList['Moves'][' '.join(line.split(' ')[:-1])] = line.split(' ')[-1]
testList['Teammates'] = {}
for line in landorusList[6]:
  if line == 'Teammates':
    continue
  else:
    testList['Teammates'][' '.join(line.split(' ')[:-1])] = line.split(' ')[-1]
testList['Checks and Counters'] = {}
for line in landorusList[7]:
  if line == 'Checks and Counters':
    continue
  elif '±' in line:
    testList['Checks and Counters'][line.split(' ')[0]] = [line.split(' ')[1], line.split(' ')[2]]
    currentPoke = line.split(' ')[0]
  else:
    testList['Checks and Counters'][currentPoke].append(' '.join(line.split(' ')[:2]).lstrip('('))
    testList['Checks and Counters'][currentPoke].append(' '.join(line.split(' ')[3:]).rstrip(')'))
print(testList)
landorusTherian = []
for section in landorusList:
  if len(section) == 1:
    landorusTherian.append({'name':section[0]})
    continue
  landorusTherian.append({})
  for line in section:
    if 'section' in line:
      continue
    lineList = line.split(' ')
    landorusTherian[-1][lineList[0]] = ' '.join(lineList[1:])
with open('hrmmm.json', 'w') as outfile:
  json.dump(testList, outfile, indent=2)