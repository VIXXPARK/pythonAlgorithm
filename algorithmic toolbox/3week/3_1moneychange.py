money=int(input())
lst=[10,5,1]
cnt=0
for coin in lst:
    while money-coin>=0:
        money-=coin
        cnt+=1
print(cnt)
