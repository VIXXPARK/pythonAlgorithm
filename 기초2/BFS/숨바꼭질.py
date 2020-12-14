import sys
from collections import deque
N,M = map(int,input().split())
loc=[sys.maxsize]*100001
loc[N]=0

def bfs(n):
    q=deque()
    cnt=0
    q.append([n,cnt])
    while q:
        a=q.popleft()
        if a[0]==M:
            print(a[1])
            sys.exit(0)
        if a[0]-1>=0:
            if a[1]+1<loc[a[0]-1]:
                loc[a[0]-1]=a[1]+1
                q.append([a[0]-1,a[1]+1])
        if a[0]+1<=100000:
            if a[1]+1<loc[a[0]+1]:
                loc[a[0]+1]=a[1]
                q.append([a[0]+1,a[1]+1])
        if a[0]*2<=100000:
            if a[1]+1<loc[a[0]*2]:
                loc[a[0]*2]=a[1]*2
                q.append([a[0]*2,a[1]+1])

bfs(N)
