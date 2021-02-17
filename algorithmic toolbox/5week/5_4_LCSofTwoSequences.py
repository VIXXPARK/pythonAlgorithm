import itertools
n=int(input())
lst=list(map(int,input().split()))
m=int(input())
lst2=list(map(int,input().split()))
dp=[[-1 for _ in range(len(lst2)+1)]for _ in range(len(lst)+1)]
def lcs(a,b):
    if a==n or b==m:
        return 0
    if lst[a]==lst2[b]:
        if dp[a][b]==-1:
            dp[a][b]=1+lcs(a+1,b+1)
        return dp[a][b]
    else:
        if dp[a+1][b]==-1:
            dp[a+1][b]=lcs(a+1,b)
        if dp[a][b+1]==-1:
            dp[a][b+1]=lcs(a,b+1)
        return max(dp[a+1][b],dp[a][b+1])
print(lcs(0,0))
 

    
