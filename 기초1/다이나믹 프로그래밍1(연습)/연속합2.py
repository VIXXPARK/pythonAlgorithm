import sys
N =int(sys.stdin.readline())
li = [0]+list(map(int,sys.stdin.readline().rstrip().split()))
dp = [[-1000]*2 for _ in range(N+1)]
ans=-1000
for i in range(1,N+1):
    dp[i][0]=max(li[i],li[i]+dp[i-1][0])
    dp[i][1]=max(dp[i][1],dp[i][0])
    if dp[i-1][0]>dp[i-1][1]+li[i]:
        dp[i][1]=dp[i-1][0]
    elif li[i]+dp[i-1][1]>li[i]:
        dp[i][1]=li[i]+dp[i-1][1]
    ans=max(ans,max(dp[i][1],dp[i][0]))
print(ans)