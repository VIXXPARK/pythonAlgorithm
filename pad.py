import re
s='123ffd3ddg'
s=re.sub('[^a-z]','',s)
print(s)