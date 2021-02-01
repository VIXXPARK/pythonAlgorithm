from collections import deque

def func(y,x):
    if x>=0 and x<N and y>=0 and y<M:
        return True
    else:
        return False

def bfs():
    global count,ret
    while q:
        dot=q.popleft()
        for i in range(4):
            fy=dot[0]+dy[i]
            fx=dot[1]+dx[i]
            if func(fy,fx) and graph[fy][fx]!=-1 and not visited[fy][fx]:
                visited[fy][fx]=True
                graph[fy][fx]=graph[dot[0]][dot[1]]+1
                ret=max(ret,graph[fy][fx])
                count+=1
                q.append([fy,fx])
            

N,M=map(int,input().rstrip().split())
graph=[list(map(int,input().rstrip().split())) for _ in range(M)]
visited=[[False]*N for _ in range(M)]
dy=[1,-1,0,0]
dx=[0,0,1,-1]
q = deque()
total=0
count=0
ret=0
for i in range(M):
    for j in range(N):
        if graph[i][j]==1:
            q.append([i,j])
            visited[i][j]=True
            count+=1
        if graph[i][j]!=-1:
            total+=1
if total==count:
    print(0)
else:
    bfs()
    print(ret-1) if total==count else print(-1)
