N=int(input())
dp = [0]*(30+1)
dp[2]=3
dp[4]=11
for i in range(5,N+1):
    if i%2==0:
        x=i
        dp[i]=3*dp[i-2]
        x-=2
        while x>0:
            dp[i]+=2*dp[x-2]
            x-=2
        dp[i]+=2
print(dp[N])
    
