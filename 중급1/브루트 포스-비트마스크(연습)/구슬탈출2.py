import sys
from collections import deque
N,M= map(int,input().split())
graph=[list(input()) for _ in range(N)]
dist=[[[[0 for _ in range(M)]for _ in range(N)]for _ in range(M)]for _ in range(N)]
redY,redX=0,0
blueY,blueX=0,0
for i in range(N):
    for j in range(M):
        if graph[i][j]=='B':
            blueY,blueX=i,j
        elif graph[i][j]=='R':
            redY,redX=i,j
q=deque()
q.append([redY,redX,blueY,blueX])
dy,dx=[-1,0,1,0],[0,-1,0,1]
def wall(y,x,gy,gx):
    if gx==-1:
        for i in range(x-1,-1,-1):
            if graph[y][i]=='#' or graph[y][i]=='R' or graph[y][i]=='B':
                return (y,i+1)
        return (y,x)
    elif gx==1:
        for i in range(x+1,M):
            if graph[y][i]=='#' or graph[y][i]=='R' or graph[y][i]=='B':
                return (y,i-1)
        return (y,x)
    elif gy==1:
        for i in range(y+1,N):
            if graph[i][x]=='#' or graph[i][x]=='R' or graph[i][x]=='B':
                return (i-1,x)
        return (y,x)
    elif gy==-1:
        for i in range(y-1,-1,-1):
            if graph[i][x]=='#' or graph[i][x]=='R' or graph[i][x]=='B':
                return (i+1,x)
        return (y,x)
def escape(y,x,gy,gx):
    if gx==-1:
        for i in range(x-1,-1,-1):
            if graph[y][i]=='O':
                return True
            elif graph[y][i]=='#' :
                return False
        return False
    elif gx==1:
        for i in range(x+1,M):
            if graph[y][i]=='O':
                return True
            elif graph[y][i]=='#':
                return False
        return False
    elif gy==1:
        for i in range(y+1,N):
            if graph[i][x]=='O':
                return True
            elif graph[i][x]=='#' :
                return False
        return False
    elif gy==-1:
        for i in range(y-1,-1,-1):
            if graph[i][x]=='O':
                return True
            elif graph[i][x]=='#':
                return False
        return False

def dfs():
    beforeY1,beforeX1=-1,-1
    beforeY2,beforeX2=-1,-1
    while q:    
        ry,rx,by,bx=q.popleft()
        if beforeY2!=-1:
            if not(beforeY1==ry and beforeX1==rx):
                graph[ry][rx],graph[beforeY1][beforeX1]='R','.'
            if not(beforeY2==by and beforeX2==bx):
                graph[by][bx],graph[beforeY2][beforeX2]='B','.'
        for i in range(4): ## up/left/down/right
            gy,gx=dy[i],dx[i]
            escapeRed=escape(ry,rx,gy,gx)
            escapeBlue=escape(by,bx,gy,gx)
            if escapeRed and escapeBlue:
                continue
            elif escapeRed and not escapeBlue:
                if dist[ry][rx][by][bx]+1<=10:
                    print(dist[ry][rx][by][bx]+1)
                else:
                    print(-1)
                sys.exit(0)
                return
            elif not escapeRed and not escapeBlue:
                if i==0:
                    if rx==bx and ry>by:
                        nby,nbx=wall(by,bx,gy,gx)
                        if not(nby==by and nbx==bx):
                            graph[nby][nbx],graph[by][bx]='B','.'
                        nry,nrx=wall(ry,rx,gy,gx)
                        if not(nry==ry and nrx==rx):
                            graph[nry][nrx],graph[ry][rx]='R','.'
                    elif rx==bx and ry<by:
                        nry,nrx=wall(ry,rx,gy,gx)
                        if not(nry==ry and nrx==rx):
                            graph[nry][nrx],graph[ry][rx]='R','.'
                        nby,nbx=wall(by,bx,gy,gx)
                        if not(nby==by and nbx==bx):
                            graph[nby][nbx],graph[by][bx]='B','.'
                    
                    else:
                        nry,nrx=wall(ry,rx,gy,gx)
                        if not(nry==ry and nrx==rx):
                            graph[nry][nrx],graph[ry][rx]='R','.'
                        nby,nbx=wall(by,bx,gy,gx)
                        if not(nby==by and nbx==bx):
                            graph[nby][nbx],graph[by][bx]='B','.'

                elif i==1:
                    if ry==by and rx>bx:
                        nby,nbx=wall(by,bx,gy,gx)
                        if not(nby==by and nbx==bx):
                            graph[nby][nbx],graph[by][bx]='B','.'
                        nry,nrx=wall(ry,rx,gy,gx)
                        if not(nry==ry and nrx==rx):
                            graph[nry][nrx],graph[ry][rx]='R','.'
                    elif ry==by and rx<bx:
                        nry,nrx=wall(ry,rx,gy,gx)
                        if not(nry==ry and nrx==rx):
                            graph[nry][nrx],graph[ry][rx]='R','.'
                        nby,nbx=wall(by,bx,gy,gx)
                        if not(nby==by and nbx==bx):
                            graph[nby][nbx],graph[by][bx]='B','.'
                    else:
                        nry,nrx=wall(ry,rx,gy,gx)
                        if not(nry==ry and nrx==rx):
                            graph[nry][nrx],graph[ry][rx]='R','.'
                        nby,nbx=wall(by,bx,gy,gx)
                        if not(nby==by and nbx==bx):
                            graph[nby][nbx],graph[by][bx]='B','.'

                elif i==2:
                    if rx==bx and ry<by:
                        nby,nbx=wall(by,bx,gy,gx)
                        if not(nby==by and nbx==bx):
                            graph[nby][nbx],graph[by][bx]='B','.'
                        nry,nrx=wall(ry,rx,gy,gx)
                        if not(nry==ry and nrx==rx):
                            graph[nry][nrx],graph[ry][rx]='R','.'

                    elif rx==bx and ry>by:
                        nry,nrx=wall(ry,rx,gy,gx)
                        if not(nry==ry and nrx==rx):
                            graph[nry][nrx],graph[ry][rx]='R','.'
                        nby,nbx=wall(by,bx,gy,gx)
                        if not(nby==by and nbx==bx):
                            graph[nby][nbx],graph[by][bx]='B','.'
                    
                    else:
                        nry,nrx=wall(ry,rx,gy,gx)
                        if not(nry==ry and nrx==rx):
                            graph[nry][nrx],graph[ry][rx]='R','.'
                        nby,nbx=wall(by,bx,gy,gx)
                        if not(nby==by and nbx==bx):
                            graph[nby][nbx],graph[by][bx]='B','.'

                elif i==3:
                    if ry==by and rx<bx:
                        nby,nbx=wall(by,bx,gy,gx)
                        if not(nby==by and nbx==bx):
                            graph[nby][nbx],graph[by][bx]='B','.'
                        nry,nrx=wall(ry,rx,gy,gx)
                        if not(nry==ry and nrx==rx):
                            graph[nry][nrx],graph[ry][rx]='R','.'

                    elif ry==by and rx>bx:
                        nry,nrx=wall(ry,rx,gy,gx)
                        if not(nry==ry and nrx==rx):
                            graph[nry][nrx],graph[ry][rx]='R','.'
                        nby,nbx=wall(by,bx,gy,gx)
                        if not(nby==by and nbx==bx):
                            graph[nby][nbx],graph[by][bx]='B','.'
                    
                    else:
                        nry,nrx=wall(ry,rx,gy,gx)
                        if not(nry==ry and nrx==rx):
                            graph[nry][nrx],graph[ry][rx]='R','.'
                        nby,nbx=wall(by,bx,gy,gx)
                        if not(nby==by and nbx==bx):
                            graph[nby][nbx],graph[by][bx]='B','.'


                
                if not dist[nry][nrx][nby][nbx] and not(ry==nry and rx==nrx and by==nby and bx==nbx):
                    dist[nry][nrx][nby][nbx]=dist[ry][rx][by][bx]+1
                    q.append([nry,nrx,nby,nbx])
                if not(nry==ry and nrx==rx):
                    graph[nry][nrx],graph[ry][rx]='.','R'
                if not(nby==by and nbx==bx):
                    graph[nby][nbx],graph[by][bx]='.','B'
        beforeY1,beforeX1=ry,rx
        beforeY2,beforeX2=by,bx

       

dfs()
print(-1)

## short version ##

N, M = map(int, input().split())
B = [list(input().rstrip()) for _ in range(N)]  # Board
dx = [-1, 1, 0, 0]  # x축 움직임
dy = [0, 0, -1, 1]  # y축 움직임
queue = []  # BFS : queue 활용
# Red(rx,ry)와 Blue(bx,by)의 탐사 여부 체크
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

def pos_init():
    rx, ry, bx, by = 0, 0, 0, 0  # 초기화
    for i in range(N):
        for j in range(M):
            if B[i][j] == 'R':
                rx, ry = i, j
            elif B[i][j] == 'B':
                bx, by = i, j
    # 위치 정보와 depth(breadth 끝나면 +1)
    queue.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
    cnt = 0  # 이동 칸 수
    # 다음이 벽이거나 현재가 구멍일 때까지
    while B[x+dx][y+dy] != '#' and B[x][y] != 'O':
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt

def solve():
    pos_init()  # 시작 조건
    while queue:  # BFS : queue 기준
        rx, ry, bx, by, depth = queue.pop(0)
        if depth > 10:  # 실패 조건
            break
        for i in range(4):  # 4방향 이동 시도
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i])  # Red
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i])  # Blue
            if B[nbx][nby] != 'O':  # 실패 조건이 아니면
                if B[nrx][nry] == 'O':  # 성공 조건
                    print(depth)
                    return
                if nrx == nbx and nry == nby:  # 겹쳤을 때
                    if rcnt > bcnt:  # 이동거리가 많은 것을
                        nrx -= dx[i]  # 한 칸 뒤로
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                # breadth 탐색 후, 탐사 여부 체크
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    # 다음 depth의 breadth 탐색 위한 queue
                    queue.append((nrx, nry, nbx, nby, depth+1))
    print(-1)  # 실패 시

solve()