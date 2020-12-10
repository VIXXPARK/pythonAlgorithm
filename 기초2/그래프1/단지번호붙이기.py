from collections import deque

def func(y,x):
    if x>=0 and x<N and y>=0 and y<N:
        return True
    else:
        return False

def bfs(y,x):
    q = deque()
    q.append([y,x])
    visited[y][x]=True
    count=1
    while q:
        dot=q.popleft()
        for i in range(4):
            fy=dot[0]+dy[i]
            fx=dot[1]+dx[i]
            if func(fy,fx) and not visited[fy][fx] and graph[fy][fx]:
                visited[fy][fx]=True
                count+=1
                q.append([fy,fx])
    return count

N=int(input())
graph=[list(map(int, input())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
dy=[1,-1,0,0]
dx=[0,0,1,-1]
ret=[]
count=0
for i in range(N):
    for j in range(N):
        if graph[i][j] and not visited[i][j]:
            count+=1
            ret.append(bfs(i,j))
ret.sort()
print(count)
for x in ret:
    print(x)

