import sys
from collections import deque
N=int(sys.stdin.readline())
graph=[list(input().rstrip()) for _ in range(N)]
colorBlindness=[[0]*N for _ in range(N)]
visited=[[0]*N for _ in range(N)]
dy,dx=[1,-1,0,0],[0,0,1,-1]
def scope(y,x):
    return 0<=y<N and 0<=x<N
def colorBlind(color):
    if color=='R' or color=='G':
        return True
    else:
        return False
def bfsColorBlindness(y,x,color):
    q=deque()
    q.append([y,x])
    colorBlindness[y][x]=True
    flag=colorBlind(color)
    while q:
        fy,fx=q.popleft()
        for i in range(4):
            my,mx=fy+dy[i],fx+dx[i]
            if scope(my,mx) and colorBlind(graph[my][mx])==flag and not colorBlindness[my][mx]:
                colorBlindness[my][mx]=True
                q.append([my,mx])
def bfs(y,x,color):
    que=deque()
    que.append([y,x])
    visited[y][x]=True
    while que:
        fy,fx=que.popleft()
        for i in range(4):
            my,mx=fy+dy[i],fx+dx[i]
            if scope(my,mx) and color==graph[my][mx] and not visited[my][mx]:
                visited[my][mx]=True
                que.append([my,mx])
normal=0
blind=0
for i in range(N):
    for j in range(N):
        if colorBlindness[i][j]==0:
            bfsColorBlindness(i,j,graph[i][j])
            blind+=1
        if visited[i][j]==0:
            bfs(i,j,graph[i][j])
            normal+=1

print(normal,blind)