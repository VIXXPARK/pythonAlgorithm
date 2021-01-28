import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) < 1: pass
    
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)
lst=[]
data = uh.read()
# print(data.decode())
tree = ET.fromstring(data)
counts= tree.findall('.//count')
for count in counts:
    lst.append(int(count.text))
print(len(lst))
print(sum(lst))
