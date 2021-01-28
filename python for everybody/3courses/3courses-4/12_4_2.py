import urllib.request
import re
fhand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
ans=''
for line in fhand:
    data = line.decode().strip()
    val = re.findall('^\<a\shref=\"([^ ].+)\"',data)
    if len(val)>=1:
        ans=val
print(ans[0])
