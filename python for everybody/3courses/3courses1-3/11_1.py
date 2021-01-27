import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x)
print(y)
z= 'From: Using the : character'
w= re.findall('^F.+?:',z) # ?는 non-greedy 
print(w)
k = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
looks = re.findall('\S+@\S+',k)
catch  = re.findall('^From (\S+@\S+)',k)
print(catch)
atpos = k.find('@')
sppos = k.find(' ',atpos)
host = k[atpos+1:sppos]
print(host)
part = re.findall('@([^ ]*)',k) # [^ ]는 공백이 없는 문자와 매칭, *는 0개 이상의 문자와 매칭
print(part)