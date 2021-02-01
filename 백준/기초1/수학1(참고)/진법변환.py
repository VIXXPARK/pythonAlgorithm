import sys
a,b=sys.stdin.readline().split()
li=[]
b=int(b)
for x in a:
    li.append(x)
li.reverse()
cnt=0
ans=0
for x in li:
    if x>='0' and x<='9':
        ans+=(b**cnt)*int(x)
    else:
        ans+=(b**cnt)*int((ord(x)-ord('A')+10))
    cnt+=1
print(ans)