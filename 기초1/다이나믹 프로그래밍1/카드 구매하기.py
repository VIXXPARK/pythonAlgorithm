import sys
from collections import deque
N=int(input())
card=deque(map(int,sys.stdin.readline().split())) # = [0] + list(map(int,sys.stdin.readline().split()))
card.appendleft(0)
dp = [0]*1001
for i in range(1,N+1):
    dp[i]=card[i]
    for j in range(i):
        dp[i]=max(dp[i],dp[i-j]+dp[j])
print(dp[N])