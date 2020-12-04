import sys
N=int(sys.stdin.readline().rstrip())
loc=0
mod=1000000009
li=[]
for _ in range(N):
    li.append(int(sys.stdin.readline().rstrip()))
    loc=max(loc,li[-1])
dp = [[0]*(3+1) for _ in range(loc+1)]
dp[1]=[0,1,0,0]
dp[2]=[0,1,1,0]
dp[3]=[0,2,1,1]
for i in range(4,loc+1):
    dp[i][1]=(dp[i-1][1]+dp[i-1][2]+dp[i-1][3])%mod
    dp[i][2]=(dp[i-2][1]+dp[i-2][2]+dp[i-2][3])%mod
    dp[i][3]=(dp[i-3][1]+dp[i-3][2]+dp[i-3][3])%mod
for i in li:
    print((dp[i][1]+dp[i][2]+dp[i][3])%mod)



# dp = [0]*1000001
# dp[0]=1;dp[1]=1;dp[2]=2
# for i in range(3,1000001):
#     if dp[i]==0:
#         dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
#         dp[i] %= 1000000009
# for _ in range(int(input())):
#     n = int(input())
#     print(dp[n])
# https://hong-i.tistory.com/111
