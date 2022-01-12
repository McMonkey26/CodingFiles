import json, re, ssl, urllib.request, os, base64
os.chdir('/Users/jpollack/Desktop/CodingFiles/PythonFiles')
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://api.github.com/repos/NotEnoughUpdates/NotEnoughUpdates-REPO/git/trees/c5ee90a8f46d76b7731bb4bfcbf26e6bc348d3eb'
response = urllib.request.urlopen(url)
itemData = json.loads(response.read())
outfile = open('getAllIds.json', 'w')
json.dump(itemData, outfile, indent=2)
outfile.close()
# print(itemData['tree'][0]['url'])
for item in itemData['tree']:
  pass
  # print(item['path'])
url = itemData['tree'][0]['url']
response = urllib.request.urlopen(url)
nextItemData = json.loads(response.read())
currentItemData = base64.b64decode(nextItemData['content'])
currentItemData = re.sub('\\n  ', '\n', str(currentItemData))
json.dump(str(currentItemData), open('getAllIds.json', 'w'), indent=2)
try:
  file = open('itemIds/getAllIds.txt', 'x')
except FileExistsError:
  file = open('itemIds/getAllIds.txt', 'w')
# json.dump(currentItemData, file, indent=2)
print(json.dumps(nextItemData, indent=2),':',itemData['tree'][0]['path'])
# print(itemData['content'])
# outfile = open('getAllIds.txt', 'w')
# content = str(base64.b64decode(itemData['content']))
# reg = r'\\n  '
# jsonContent = re.sub(reg, '\n', content)
# outfile.write(jsonContent)
# outfile.close()
# print(base64.b64decode(itemData['content']))
