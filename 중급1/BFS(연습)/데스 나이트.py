import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
r1,c1,r2,c2=map(int,input().split())
dy,dx=[-2,-2,0,2,2,0],[-1,1,2,1,-1,-2]
visited=[[0]*N for _ in range(N)]
flag=False
def scope(y,x):
    return y>=0 and y<N and x>=0 and x<N

def bfs():
    global flag
    q=deque()
    q.append([r1,c1])
    visited[r1][c1]=0
    while q:
        fy,fx=q.popleft()
        if fy==r2 and fx==c2:
            flag=True
            print(visited[fy][fx])
            return
        for i in range(6):
            gy,gx=fy+dy[i],fx+dx[i]
            if scope(gy,gx) and not visited[gy][gx]:
                visited[gy][gx]=visited[fy][fx]+1
                q.append([gy,gx])
bfs()
if not flag:
    print(-1)