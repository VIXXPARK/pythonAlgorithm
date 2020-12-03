import sys
N = int(sys.stdin.readline().rstrip())
li = list(map(int,sys.stdin.readline().rstrip().split()))
li.reverse()
li = [0]+li
dp= [0]*(N+1)
ans=1
for i in range(1,N+1):
    dp[i]=1
    ans=max(dp[i],ans)
    for j in range(1,i):
        if li[j]<li[i]:
            dp[i]=max(dp[i],dp[j]+1)
            ans=max(dp[i],ans)
print(ans)


# n = int(input())
# a = list(map(int, input().split()))
# dp = [1 for i in range(n)]
# for i in range(1, n):
#     s = []
#     for j in range(i):
#         if a[i] < a[j]:
#             s.append(dp[j])
#     if not s:
#         continue
#     else:
#         dp[i] += max(s)
# print(max(dp))