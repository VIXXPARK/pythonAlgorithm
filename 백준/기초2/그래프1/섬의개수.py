from collections import deque
dy=[-1,-1,-1,0,1,1,1,0]
dx=[-1,0,1,1,1,0,-1,-1]
def func(y,x):
    if x>=0 and x<N and y>=0 and y<M:
        return True
    else:
        return False

def bfs(y,x):
    q = deque()
    q.append([y,x])
    while q:
        dot=q.popleft()
        for i in range(8):
            fy=dot[0]+dy[i]
            fx=dot[1]+dx[i]
            if func(fy,fx):
                if not visited[fy][fx] and graph[fy][fx]:
                    visited[fy][fx]=True
                    q.append([fy,fx])


while True:
    N,M = map(int,input().rstrip().split())
    if N==0 and M==0:
        break
    graph=[list(map(int,input().rstrip().split())) for _ in range(M)]
    visited=[[False]*N for _ in range(M)]
    count=0
    for i in range(M):
        for j in range(N):
            if not visited[i][j] and graph[i][j]:
                count+=1
                bfs(i,j)
    print(count)

