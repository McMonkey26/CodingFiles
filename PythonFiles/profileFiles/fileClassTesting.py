import os, json, re

def goThroughFolder(startingPath):
  ids = {}
  with os.scandir(startingPath) as entries:
    for entry in entries:
      with open(entry.path, 'r') as f:
        data = f.read().split('\n')
        for property in data:
          property = property.split('=')
          if 'ExtraAttributes.id' in property[0]:
            ids[property[1]] = re.sub(r'\..*$', '', entry.name)
            #print('File: {}, ID: {}'.format(entry.name, property[1]))
  return ids