total,cap = map(int,input().split())
stk=list(map(int,input().split()))
dp = [[0 for _ in range(total+1)] for _ in range(len(stk))]
for j in range(0,len(stk)):
    for i in range(1,total+1):
        if stk[j]>i:
            dp[j][i]=dp[j-1][i]
        else:
            dp[j][i]=max(stk[j]+dp[j-1][i-stk[j]],dp[j-1][i])
print(dp[len(stk)-1][total])

