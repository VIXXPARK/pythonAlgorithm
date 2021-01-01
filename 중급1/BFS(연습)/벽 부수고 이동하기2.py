# import sys
# from collections import deque
# N,M,K=map(int,input().split())
# graph=[list(input().rstrip()) for _ in range(N)]
# graph[0][0]=1
# board=[[[0] * (K + 1) for _ in range(M)] for _ in range(N)]
# board[0][0]=[1]*(K+1)
# dy,dx=[1,-1,0,0],[0,0,1,-1]
# def scope(y,x,wall):
#     return y<N and y>=0 and x>=0 and x<M and not board[y][x][wall]
# def bfs():
#     q=deque()
#     q.append([0,0,0])
#     while q:
#         y,x,wall=q.popleft()
#         dist=board[y][x][wall]+1
#         if x==M-1 and y==N-1:
#             print(board[y][x][wall])
#             sys.exit(0)
#         for i in range(4):
#             fy,fx=y+dy[i],x+dx[i]
#             if scope(fy,fx,wall):
#                 if graph[fy][fx]=='0':
#                     board[fy][fx][wall]=dist
#                     q.append([fy,fx,wall])
#                 elif wall<K:
#                     board[fy][fx][wall+1]=dist
#                     q.append([fy,fx,wall+1])
#     print(-1)

# bfs()
### 이렇게 범위에 관하여 다룰 때에는 [a][b][c]에서 c부분에 범위가 가장 적은 것을 두자. 그래야 시간적 손실이 덜하다.

import sys
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n, m, k = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().rstrip() for _ in range(n)]
queue = deque()
queue.append((0, 0, 1, k))
cb = [[-1] * m for j in range(n)]
answer = -1
while queue:
    x, y, sub, block = queue.popleft()
    if x == n - 1 and y == m - 1:
        if answer == -1:
            answer = sub
        elif answer > sub:
            answer = sub
        continue
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if -1 < nx < n and -1 < ny < m:
            if board[nx][ny] == '1' and block > 0:
                if cb[nx][ny] < block - 1:
                    cb[nx][ny] = block - 1
                    queue.append((nx, ny, sub + 1, block - 1))
            elif board[nx][ny] == '0':
                if cb[nx][ny] < block:
                    cb[nx][ny] = block
                    queue.append((nx, ny, sub + 1, block))
print(answer)