import sys
N = int(sys.stdin.readline())
T=[0]
P=[0]
dp=[0]*(N+1)
ans=0
for _ in range(N):
    t,p=map(int,sys.stdin.readline().split())
    T.append(t)
    P.append(p)
for i in range(1,N+1):
    if T[i]+i-1<=N:
        dp[i]=max(dp[i],P[i])
        ans=max(dp[i],ans)
        for j in range(1,i):
            if T[j]+j-1>=i or T[j]+j-1>N:
                pass
            else:
                dp[i]=max(dp[i],P[i]+dp[j])
                ans=max(ans,dp[i])
print(ans)
