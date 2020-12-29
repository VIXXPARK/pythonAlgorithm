import sys
from collections import deque
col,row = map(int,sys.stdin.readline().split())
graph=[]
for _ in range(col):
    graph.append(list(sys.stdin.readline().rstrip()))
alpha=[False]*26
alpha[ord(graph[0][0])-ord('A')]=True
visited=[[False]*row for _ in range(col)]
dy,dx=[1,-1,0,0],[0,0,1,-1]
ret=0
def scope(y,x):
    return y>=0 and y<col and x>=0 and x<row

def dfs(y,x,q):
    global ret
    alpha[ord(graph[y][x])-ord('A')]=True
    visited[y][x]=True
    for i in range(4):
        ry,rx=y+dy[i],x+dx[i]
        if scope(ry,rx) and not alpha[ord(graph[ry][rx])-ord('A')] and not visited[ry][rx]:
            alpha[ord(graph[ry][rx])-ord('A')]=True
            visited[ry][rx]=True
            dfs(ry,rx,q+1)
            alpha[ord(graph[ry][rx])-ord('A')]=False
            visited[ry][rx]=False
       
    ret=max(ret,q)
dfs(0,0,1)
print(ret)
## 복습때 빠른 코드 참조
R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
cache = [['' for _ in range(C)] for _ in range(R)]
def bfs(x, y):
    queue = [(x, y, board[x][y])]
    ans = 0
    while queue:
        x, y, path = queue.pop()
        chk = False
        for i, j in (1, 0), (-1, 0), (0, 1), (0, -1):
            xx, yy = x+i, y+j
            if xx < 0 or yy < 0 or xx >= R or yy >= C:
                continue
            if board[xx][yy] not in path:
                chk = True
                if cache[xx][yy] != path + board[xx][yy]:
                    cache[xx][yy] = path + board[xx][yy]
                    queue.append((xx, yy, path + board[xx][yy]))
        if not chk:
            ans = max(ans, len(path))
    return ans
print(bfs(0, 0))