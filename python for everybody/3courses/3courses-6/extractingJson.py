import json
import urllib.request,urllib.parse
import ssl,re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
url= address
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data=uh.read()
info = json.loads(data)
print('Retrieved', len(data), 'characters')
lst=[]
print('Count:',len(info['comments']))
for x in info['comments']:
    lst.append(x['count'])
print(sum(lst))
    