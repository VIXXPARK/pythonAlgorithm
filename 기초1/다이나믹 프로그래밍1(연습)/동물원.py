import sys
dp = [0]*100001
dp[1],dp[2]=3,7
N = int(sys.stdin.readline())
for i in range(3,N+1):
    dp[i]=(dp[i-1]*2+dp[i-2])%9901
print(dp[N])