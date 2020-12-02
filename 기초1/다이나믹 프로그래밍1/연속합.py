import sys
N =int(input())
li = [0]+list(map(int,sys.stdin.readline().split()))
dp = [0]*(N+1)
ans=-1000
for i in range(1,N+1):
    dp[i]=max(dp[i-1]+li[i],li[i])
    ans=max(dp[i],ans)
print(ans)