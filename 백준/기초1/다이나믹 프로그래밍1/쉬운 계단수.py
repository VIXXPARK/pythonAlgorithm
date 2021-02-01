N=int(input())
div=1000000000
dp = [[0]*10 for _ in range(100+1)]
dp[1]=[1,1,1,1,1,1,1,1,1,0]
for i in range(2,N+1):
    for j in range(0,10):
        if j==0:
            dp[i][j]=dp[i-1][j+1]
        elif j==9:
            dp[i][j]=dp[i-1][j-1]
        else:
            dp[i][j]=(dp[i-1][j-1]%div+dp[i-1][j+1]%div)%div
ans=0
for i in range(0,10):
    ans+=dp[N][i]
ans%=div
print(ans)