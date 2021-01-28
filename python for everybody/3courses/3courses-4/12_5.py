import urllib.request,urllib.parse,urllib.error
from bs4 import BeautifulSoup

url = input("Enter - ")
html = urllib.request.urlopen(url).read() # all read
soup = BeautifulSoup(html,'html.parser') 

tags=soup('a')
for tag in tags:
    print(tag.get('href',None))

## The TCP/IP gives us pipes/sockets between applications
## We designed application protocols to make use of these pipes
## HTTP is a simple yet powerful protocl
## Python has good support for sockets,HTTP,and HTML parsing