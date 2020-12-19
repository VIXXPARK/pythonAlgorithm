import sys
input=sys.stdin.readline
N=input().rstrip()
num=int(input())
ableList={i for i in range(10)}
ans=abs(int(N)-100)

def solve(n):
    global ans
    for i in ableList:
            ret=n+str(i)
            ans=min(ans,len(str(int(ret)))+int(abs(int(N)-int(ret))))
            if len(ret)<6:
                solve(ret)

if num:
    numList=list(map(int,input().rstrip().split()))
    ableList=ableList-set(numList)
else:
    ans=min(ans,len(N))
solve('')
print(ans)