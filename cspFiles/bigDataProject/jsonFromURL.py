import requests, json, os
os.chdir('/Users/jpollack/Desktop/CodingFiles/repos/testFile/CodingFiles/cspFiles/bigDataProject')

def getData(url):
  text = requests.get('url').text
  return json.loads(text)