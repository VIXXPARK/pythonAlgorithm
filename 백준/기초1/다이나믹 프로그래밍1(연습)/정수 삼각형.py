import sys
N = int(sys.stdin.readline())
ar = [0 for _ in range(N)]
for i in range(N):
    ar[i]=list(map(int,sys.stdin.readline().rstrip().split()))
for i in range(1,N):
    for j in range(0,i+1):
        if j==0:
            ar[i][j]+=ar[i-1][j]
        elif j==i:
            ar[i][j]+=ar[i-1][j-1]
        else:
            ar[i][j]=max(ar[i-1][j-1],ar[i-1][j])+ar[i][j]
ans=0
for i in range(N):
    ans=max(ar[N-1][i],ans)
print(ans)