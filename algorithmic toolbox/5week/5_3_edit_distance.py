lst=list(input())
lst2=list(input())
n=len(lst)
m=len(lst2)
dp=[[0 for _ in range(len(lst2)+1)]for _ in range(len(lst)+1)]
for i in range(len(lst2)+1):
    dp[0][i]=i
for i in range(len(lst)+1):
    dp[i][0]=i

def lcs(a,b):
    for i in range(1,len(lst)+1):
        for j in range(1,len(lst2)+1):
            if lst[i-1]==lst2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
    return dp[n][m]
print(lcs(0,0))
