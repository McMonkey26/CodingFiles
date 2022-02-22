import json, urllib.request, ssl, os, ast, statistics
os.chdir('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/cspFiles/bigDataProject')
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.smogon.com/stats/2021-12/moveset/gen8ou-0.txt'
file = urllib.request.urlopen(url)
tempList = []
with open('hrmmm.txt', 'w') as tempFile:
  tempFile.write('')
textFile = open('hrmmm.txt', 'a')
for line in file:
  decoded_line = line.decode('utf-8').strip().strip('|').strip()
  try:
    if tempList[-1] == [] and decoded_line == '+----------------------------------------+':
      textFile.write(str(tempList)+'\n')
      tempList = [[]]
      continue
  except IndexError: pass
  if decoded_line == '+----------------------------------------+':
    tempList.append([])
    continue
  tempList[-1].append(decoded_line)
textFile.close()

maxLengths = {
  'Abilities':{'Abilities':''},
  'Items': {'Items':''},
  'Spreads': {'Spreads':''},
  'Moves': {'Moves':''},
  'Teammates': {'Teammates':''},
  'Checks and Counters': {'Checks and Counters':''}
}
avgLengths = {
  'Abilities': [],
  'Items': [],
  'Spreads': [],
  'Moves': [],
  'Teammates': [],
  'Checks and Counters': []
}
with open('hrmmm2.txt', 'w') as outFile:
  outFile.write('')
with open('hrmmm.txt', 'r') as inFile:
  for line in inFile:
    lineList = ast.literal_eval(line.strip())
    tempDict = {'Name': lineList[0][0]}
    tempDict['Weight'] = {
      'Raw count':lineList[1][0].split(' ')[-1],
      'Avg. weight':lineList[1][1].split(' ')[-1],
      'Viability Ceiling':lineList[1][2].split(' ')[-1]
    }
    tempDict['Abilities'] = {}
    for word in lineList[2]:
      if word == 'Abilities':
        continue
      else:
        tempDict['Abilities'][' '.join(word.split(' ')[:-1])] = word.split(' ')[-1]
    tempDict['Items'] = {}
    for word in lineList[3]:
      if word == 'Items':
        continue
      else:
        tempDict['Items'][' '.join(word.split(' ')[:-1])] = word.split(' ')[-1]
    tempDict['Spreads'] = {}
    for word in lineList[4]:
      if word == 'Spreads':
        continue
      else:
        tempDict['Spreads'][word.split(' ')[0]] = word.split(' ')[1]
    tempDict['Moves'] = {}
    for word in lineList[5]:
      if word == 'Moves':
        continue
      else:
        tempDict['Moves'][' '.join(word.split(' ')[:-1])] = word.split(' ')[-1]
    tempDict['Teammates'] = {}
    for word in lineList[6]:
      if word == 'Teammates':
        continue
      else:
        tempDict['Teammates'][' '.join(word.split(' ')[:-1])] = word.split(' ')[-1]
    tempDict['Checks and Counters'] = {}
    for word in lineList[7]:
      if word == 'Checks and Counters':
        continue
      elif '±' in word:
        tempDict['Checks and Counters'][word.split(' ')[0]] = [word.split(' ')[1], word.split(' ')[2]]
        currentPoke = word.split(' ')[0]
      else:
        tempDict['Checks and Counters'][currentPoke].append(' '.join(word.split(' ')[:2]).lstrip('('))
        tempDict['Checks and Counters'][currentPoke].append(' '.join(word.split(' ')[3:]).rstrip(')'))
    
    for key in list(maxLengths.keys()):
      avgLengths[key].append(len(tempDict[key]))
      if len(tempDict[key]) > len(maxLengths[key][key]):
        maxLengths[key] = tempDict

    outList = [tempDict['Name']] + list(tempDict['Weight'].values())
    for i in range(3):
      try:
        outList.append(':'.join(list(tempDict['Abilities'].items())[i]))
      except IndexError:
        outList.append('-')
    for i in range(20):
      try:
        outList.append(':'.join(list(tempDict['Items'].items())[i]))
      except IndexError:
        outList.append('-')
    for i in range(7):
      try:
        outList.append(':'.join(list(tempDict['Spreads'].items())[i]))
      except IndexError:
        outList.append('-')
    for i in range(20):
      try:
        outList.append(':'.join(list(tempDict['Moves'].items())[i]))
      except IndexError:
        outList.append('-')
    for key in tempDict['Teammates']:
      outList.append(key+':'+tempDict['Teammates'][key])
    for i in range(12):
      try:
        outList.append(list(tempDict['Checks and Counters'].keys())[i] + ':(' + '|'.join(list(tempDict['Checks and Counters'].values())[i])+')')
      except IndexError:
        outList.append('-')
    with open('hrmmm2.txt', 'a') as outFile:
      outFile.write('~'.join(outList)+'\n')
outputString = ''
with open('hrmmm2.txt', 'r') as inFile:
  for line in inFile:
    outputString += (line.rstrip()+'@')
with open('hrmmm3.txt', 'w') as outFile:
  outFile.write(outputString)
sheetList = [[] for _ in range(49)]
lastLen = 0
lastList = ''
with open('hrmmm2.txt', 'r') as inFile:
  for line in inFile:
    lineList = line.strip().split('~')
    if len(lineList) > lastLen:
      lastLen = len(lineList)
      lastList = lineList
for key in maxLengths:
  print(maxLengths[key]['Name'],':',key,'('+str(len(maxLengths[key][key]))+')')
for key, value in avgLengths.items():
  statString = '{:20} '.format(key+':')
  statString += 'Mean ({:5.5}) '.format(str(float(statistics.mean(value))))
  statString += 'Medians ({:2},{:2},{:2}) '.format(statistics.median_low(value), statistics.median(value), statistics.median_high(value))
  statString += 'Mode ({:2}) '.format(statistics.mode(value))
  statString += 'Max ({:2}) '.format(max(value))
  statString += 'Min ({:2})'.format(min(value))
  print(statString)