N=int(input())
DP=[[0]*10 for _ in range(1001)]
for i in range(10):
    DP[1][i]=1
for i in range(2,N+1):
    for j in range(0,10):
        for k in range(j,10):
            DP[i][j]+=DP[i-1][k]
ans=0
for i in range(0,10):
    ans+=DP[N][i]
print(ans%10007)
