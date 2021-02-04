from collections import deque
dy = [1,-1,0,0]
dx = [0,0,1,-1]
m,n=map(int,input().split())
visited = [[0 for _ in range(100)] for _ in range(100)]
def bfs(y,x):
    q=deque()
    q.append((y,x))
    while q:
        fy,fx=q.popleft()
        for i in range(4):
            gy,gx=fy+dy[i],fx+dx[i]
            if 0<=gy<m and 0<=gx<n:
                if visited[gy][gx]!=1:
                    visited[gy][gx]=1
                    q.append((gy,gx))
    