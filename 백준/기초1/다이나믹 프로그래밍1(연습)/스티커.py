import sys
tcase = int(sys.stdin.readline().rstrip())
for _ in range(tcase):
    line = int(input().rstrip())
    li = [0 for _ in range(2)]
    dp = [[0]*(line+1) for _ in range(2)]
    for i in range(2):
        li[i]=[0]+list(map(int,sys.stdin.readline().rstrip().split()))
    dp[0][1]=li[0][1]
    dp[1][1]=li[1][1]
    ans=0
    for i in range(2,line+1):
        dp[0][i]=max(dp[0][i-2],max(dp[1][i-1],dp[1][i-2]))+li[0][i]
        dp[1][i]=max(dp[1][i-2],max(dp[0][i-1],dp[0][i-2]))+li[1][i]
        ans=max(dp[0][i],max(dp[1][i],ans))
    print(ans)

