n=int(input())
dp=[0,1,2,1,1]
for i in range(5,n+1):
    x=min(min(dp[i-1],dp[i-3]),dp[i-4])+1
    dp.append(x)
print(dp[n])