from collections import deque
N,M=map(int,input().split())
graph=[list(map(int,input())) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if graph[i][j]==1: graph[i][j]=-1
graph[0][0]=1
board=[[[graph[j][i] for i in range(M)]for j in range(N)]for _ in range(2)]
dy,dx=[1,-1,0,0],[0,0,1,-1]
def scope(y,x):
    return y<N and y>=0 and x>=0 and x<M
def bfs():
    q=deque()
    q.append([0,0])
    while q:
        bit,wall=q.popleft()
        y=bit//M
        x=bit%M
        if y==N-1 and x==M-1:
            print(board[wall][y][x])
            return
        for i in range(4):
            fy,fx=y+dy[i],x+dx[i]
            if scope(fy,fx):
                if board[wall][fy][fx]==0:
                    board[wall][fy][fx]=board[wall][y][x]+1
                    q.append([fy*M+fx,wall])
                elif wall==0 and board[0][fy][fx]==-1:
                    board[1][fy][fx]=board[0][y][x]+1
                    q.append([fy*M+fx,1])
    print(-1)

bfs()
### 나중에 더 빠른 코드 참조하기###