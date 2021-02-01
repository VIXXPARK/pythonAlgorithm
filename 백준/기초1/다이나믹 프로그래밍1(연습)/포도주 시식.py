import sys
N=int(sys.stdin.readline().rstrip())
li=[]
dp = [0]*(N+1)
li.append(0)
for _ in range(N):
    li.append(int(sys.stdin.readline().rstrip()))
dp[1]=li[1]
ans=dp[1]
if N>=2:
    dp[2]=li[1]+li[2]
    ans=max(ans,dp[2])
for i in range(3,N+1):
    dp[i]=max(max(li[i-1]+dp[i-3],dp[i-2])+li[i],dp[i-1])
    ans=max(ans,dp[i])
print(ans)