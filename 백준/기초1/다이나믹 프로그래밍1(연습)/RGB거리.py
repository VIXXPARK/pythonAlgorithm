import sys
N=int(sys.stdin.readline().rstrip())
val =[[0]*3 for _ in range(1001)]
dp = [[0]*3 for _ in range(1001)]
for i in range(1,N+1):
    num = list(map(int,sys.stdin.readline().rstrip().split()))
    val[i][0]=num[0]
    val[i][1]=num[1]
    val[i][2]=num[2]
for i in range(1,N+1):
    dp[i][0]=min(val[i][0]+dp[i-1][1],val[i][0]+dp[i-1][2])
    dp[i][1]=min(val[i][1]+dp[i-1][0],val[i][1]+dp[i-1][2])
    dp[i][2]=min(val[i][2]+dp[i-1][0],val[i][2]+dp[i-1][1])
print(min(dp[N][0],min(dp[N][1],dp[N][2])))

