import sys
for _ in range(int(input())):
    n,l=map(int,input().split())
    lst=list(map(int,input().split()))
    ans=sys.maxsize
    for i in range(l,n+1):
        res=0
        for j in range(i):
            res+=lst[j]
        ans=min(ans,res/i)
        for j in range(1,n-i):
            res-=lst[j-1]
            res+=lst[j+i]
            ans=min(ans,res/i)
    print(ans)