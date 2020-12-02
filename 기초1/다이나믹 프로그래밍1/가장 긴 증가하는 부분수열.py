import sys
N = int(sys.stdin.readline().rstrip())
quest = [0]+list(map(int,sys.stdin.readline().rstrip().split()))
dp = [0]*1001
ans=0
for i in range(1,N+1):
    dp[i]=1
    ans=max(dp[i],ans)
    for j in range(1,i+1):
        if quest[j]<quest[i]:
            dp[i]=max(dp[i],dp[j]+1)
            ans=max(dp[i],ans)
print(ans)