import sys
N = int(sys.stdin.readline().rstrip())
li = [0]+list(map(int,sys.stdin.readline().rstrip().split()))
dp =[0]*1001
ans=0
for i in range(1,N+1):
    dp[i]=li[i]
    ans=max(ans,dp[i])
    for j in range(1,i):
        if li[i]>li[j]:
            dp[i]=max(dp[i],li[i]+dp[j])
            ans=max(ans,dp[i])
print(ans)