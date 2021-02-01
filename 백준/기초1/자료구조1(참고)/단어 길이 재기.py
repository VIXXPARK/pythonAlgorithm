import sys
ans = sys.stdin.readline().rstrip()
ret=''
for x in ans:
    if x.isupper():
        gap = (ord(x)-ord('A')+13)%26
        ret+=chr(ord('A')+gap)
    elif x.isspace():
        ret+=' '
    elif x.islower():
        gap = (ord(x)-ord('a')+13)%26
        ret+=chr(ord('a')+gap)
    else:
        ret+=x
print(ret)