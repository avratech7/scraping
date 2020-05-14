import urllib.request
import urllib.parse
import re

url = 'https://en.wikipedia.org/wiki/Basketball'
def scraping_wikipedia (url_address , *label):
    
  values = {'s': 'basics', 'submit': 'search'}
  data = urllib.parse.urlencode(values)
  data = data.encode('utf-8')
  req = urllib.request.Request(url, data)
  resp = urllib.request.urlopen(req)
  respData = resp.read()
  pargraphs = re.findall(r'<title>(.*?)</title>', str(respData))
  
  for eachP in pargraphs:
    print(eachP)
    
  return(pargraphs)
  
print(scraping_wikipedia(url))
