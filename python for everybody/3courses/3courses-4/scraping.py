import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
val=None
url = input('Enter URL:')
count = int(input("Enter count:"))
position = int(input("Enter position:"))
print("Retrieving:",url)
for i in range(count):
    if i==0:
        html = urllib.request.urlopen(url, context=ctx).read()
    else:
        html = urllib.request.urlopen(val, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for i,tag in enumerate(tags):
        if i==position-1:
            val=tag.get('href')
            break
    print("Retrieving:",val)
#http://py4e-data.dr-chuck.net/known_by_Camillie.html