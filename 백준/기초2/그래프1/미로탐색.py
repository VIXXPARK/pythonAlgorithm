from collections import deque

def func(y,x):
    if x>=0 and x<M and y>=0 and y<N:
        return True
    else:
        return False

def bfs(y,x):
    q=deque()
    q.append([y,x])
    while q:
        dot=q.popleft()
        for i in range(4):
            fy=dot[0]+dy[i]
            fx=dot[1]+dx[i]
            if func(fy,fx) and not visited[fy][fx] and graph[fy][fx]!=0:
                visited[fy][fx]=True
                graph[fy][fx]=graph[dot[0]][dot[1]]+1
                q.append([fy,fx])



N,M=map(int,input().split())
graph=[list(map(int,input()))for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dy=[1,-1,0,0]
dx=[0,0,1,-1]
bfs(0,0)
print(graph[N-1][M-1])
