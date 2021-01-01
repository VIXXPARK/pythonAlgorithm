import sys,copy
from collections import deque
input=sys.stdin.readline
COL,ROW= map(int,input().split())
graph=[list(input().rstrip()) for _ in range(COL)]
visited=[[0]*ROW for _ in range(COL)]
dy,dx=[0,1,0,-1],[-1,0,1,0]
spot=deque()
for i in range(COL):
    for j in range(ROW):
        if graph[i][j]=='S':
            startY,startX=i,j
        elif graph[i][j]=='*':
            spot.append([i,j])
        elif graph[i][j]=='D':
            finishY,finishX=i,j
def scope(y,x):
    return 0<=y<COL and 0<=x<ROW

def bfs():
    global spot
    q=deque()
    q.append([startY,startX])
    while q:
        water=deque()
        while spot:
            wy,wx=spot.popleft()
            for i in range(4):
                ky,kx=wy+dy[i],wx+dx[i]
                if scope(ky,kx):
                    if visited[ky][kx]!=0:
                        for k in range(4):
                            if scope(ky+dy[k],kx+dx[k]) and graph[ky+dy[k]][kx+dx[k]]=='D':
                                print(visited[ky][kx]+1)
                                return
                    elif graph[ky][kx]=='.':
                        if graph[ky][kx]!='*':
                            water.append([ky,kx])
                        graph[ky][kx]='*'
                        
                    
        que=deque(q)
        q=deque()
        spot=deque(water)
        while que:
            y,x=que.popleft()
            for i in range(4):
                my,mx=y+dy[i],x+dx[i]
                if scope(my,mx):
                    if graph[my][mx]=='.' and not visited[my][mx]:
                        visited[my][mx]=visited[y][x]+1
                        q.append([my,mx])
                    elif graph[my][mx]=='D':
                        print(visited[y][x]+1)
                        return


    print("KAKTUS")

bfs()
### 그래프 문제에서 어느 한 점에 도달하는 경우의 문제일 경우에는 visited를 둬서 거기에 값을 새겨 놓으면서 풀자
### 괜히 그래프 자체를 저장하면 deepcopy하는데 시간 걸릴 뿐만 아니라 메모리도 한 몫하기 때문이다.