import sys
a,b = map(int,sys.stdin.readline().rstrip().split())
c = int(sys.stdin.readline().rstrip())
loc = list(map(int,sys.stdin.readline().rstrip().split()))
cnt = c-1
ans=0
ret=[]
for x in range(c):
    ans+=(a**cnt)*loc[x]
    cnt-=1
while True:
    if ans==0:
        break
    else:
        ret.append(str(ans%b))
        ans//=b
ret.reverse()
print(' '.join(ret))

