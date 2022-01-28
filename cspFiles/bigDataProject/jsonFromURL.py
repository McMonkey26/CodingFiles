import requests, json, os
os.chdir('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/cspFiles/bigDataProject')

url = requests.get('https://www.smogon.com/stats/2021-12/chaos/gen8ou-0.json')
text = url.text
data = json.loads(text)
print(data['data']['Eevee'])
with open('eevee.json', 'w') as outfile:
  json.dump(data['data']['Eevee'], outfile, indent=2)