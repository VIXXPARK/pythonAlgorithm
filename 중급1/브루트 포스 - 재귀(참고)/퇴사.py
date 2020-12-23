import sys
input=sys.stdin.readline
T=[0]
P=[0]
N=int(input())
for _ in range(N):
    day,pay=map(int,input().split())
    T.append(day)
    P.append(pay)
DP=[0]*(N+1)
ans=0
for i in range(1,N+1):
    if i+T[i]-1<=N:
        DP[i]=P[i]
        ans=max(ans,DP[i])
        for j in range(1,N+1):
            if T[j]+j<=i:
                DP[i]=max(DP[j]+P[i],DP[i])
                ans=max(ans,DP[i])
print(ans)
