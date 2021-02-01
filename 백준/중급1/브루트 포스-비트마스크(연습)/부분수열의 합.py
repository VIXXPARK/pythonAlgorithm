import sys
input=sys.stdin.readline
N=int(input())
li=list(map(int,input().split()))
num=[False]*int(2*10e6)
for i in range(1,1<<N):
    sum=0
    for j in range(N):
        if i & (1<<j)!=0:
            sum+=li[j]
    num[sum]=True
idx=1
while True:
    if not num[idx]:
        print(idx)
        break
    else:
        idx+=1