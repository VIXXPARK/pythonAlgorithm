n=int(input())
dp=[0,1]
dpHist=[0,0]
ans=0
for i in range(2,n+1):
    if i%3==0 and i%2==0:
        if dp[i//3]<dp[i//2]:
            dp.append(dp[i//3]+1)
            dpHist.append(i//3)
        else:
            dp.append(dp[i//2]+1)
            dpHist.append(i//2)
    elif i%3==0:
        if dp[i//3]<dp[i-1]:
            dp.append(dp[i//3]+1)
            dpHist.append(i//3)
        else:
            dp.append(dp[i-1]+1)
            dpHist.append(i-1)
    elif i%2==0:
        if dp[i//2]<dp[i-1]:
            dp.append(dp[i//2]+1)
            dpHist.append(i//2)
        else:
            dp.append(dp[i-1]+1)
            dpHist.append(i-1)
    else:
        dp.append(dp[i-1]+1)
        dpHist.append(i-1)
answer=[n]
while n:
    answer.append(dpHist[n])
    n=dpHist[n]
    ans+=1
print(ans-1)
answer.reverse()
answer.pop(0)
print(' '.join(map(str,answer)))
        
