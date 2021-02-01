import sys
N = int(sys.stdin.readline().rstrip())
quest = [0]+list(map(int,sys.stdin.readline().rstrip().split()))
dp = [0]*1001
li = []
ans=0
li.append([])
li[0].append(0)
for i in range(1,N+1):
    dp[i]=1
    li.append([])
    ans=max(dp[i],ans)
    
    for j in range(1,i+1):
        if quest[j]<quest[i]:
            if dp[i]<dp[j]+1:
                li[i]=list(li[j])
                dp[i]=dp[j]+1
                ans=max(dp[i],ans)
    li[i].append(quest[i])
del li[0]
for i in range(N):
    if ans==len(li[i]):
        print(ans)
        for j in li[i]:
            print(j,end=' ')
        break