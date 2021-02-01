# import sys
# N=int(sys.stdin.readline().rstrip())
# dp = [100000]*100001
# dp[1],dp[2],dp[3]=1,2,3
# for i in range(4,N+1):
#     if float(int(i**0.5))==i**0.5:
#         dp[i]=1
#     else:
#         dp[i]=i
#         for j in range(1,int(i**0.5)):
#             dp[i]=min(dp[i],dp[j*j]+dp[i-j*j])

# print(dp[N])

## 위의 코드는 c++로 제출했을때는 잘되었지만 파이썬 경우에는 시간초과가 난다,
n = int(input())
dp = [0]*(n+1)
for i in range(1, n+1):
    dp[i] = i
    j = 1
    while j*j <= i:
        if dp[i] > dp[i-j*j]+1:
            dp[i] = dp[i-j*j]+1
        j += 1
print(dp[n])

#참고 https://br-brg.tistory.com/17