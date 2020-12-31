import sys
from collections import deque
N,M,K=map(int,input().split())
graph=[list(input().rstrip()) for _ in range(N)]
graph[0][0]=1
board=[[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
board[0][0]=[1]*(K+1)
dy,dx=[1,-1,0,0],[0,0,1,-1]
def scope(y,x,wall):
    return y<N and y>=0 and x>=0 and x<M and not board[y][x][wall]
def bfs():
    q=deque()
    q.append([0,0,0])
    while q:
        y,x,wall=q.popleft()
        dist=board[y][x][wall]+1
        if x==M-1 and y==N-1:
            print(board[y][x][wall])
            sys.exit(0)
        for i in range(4):
            fy,fx=y+dy[i],x+dx[i]
            if scope(fy,fx,wall):
                if graph[fy][fx]=='0':
                    board[fy][fx][wall]=dist
                    q.append([fy,fx,wall])
                elif wall<K:
                    board[fy][fx][wall+1]=dist
                    q.append([fy,fx,wall+1])
    print(-1)

bfs()
### 이렇게 범위에 관하여 다룰 때에는 [a][b][c]에서 c부분에 범위가 가장 적은 것을 두자. 그래야 시간적 손실이 덜하다.