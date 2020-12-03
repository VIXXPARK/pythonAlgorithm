import sys
N = int(sys.stdin.readline().rstrip())
li = list(map(int,sys.stdin.readline().rstrip().split()))
upperdp = [1]*N
lowerdp = [1]*N
for i in range(N):
    for j in range(i):
        if li[i]>li[j]:
            upperdp[i]=max(upperdp[i],upperdp[j]+1)
li.reverse()
for i in range(N):
    for j in range(i):
        if li[i]>li[j]:
            lowerdp[i]=max(lowerdp[i],lowerdp[j]+1)
lowerdp.reverse()
ans=0
for i in range(N):
    ans=max(ans,upperdp[i]+lowerdp[i]-1)
print(ans)