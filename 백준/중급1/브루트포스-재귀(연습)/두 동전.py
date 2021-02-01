from collections import deque
N,M= map(int,input().split())
board = [list('0'*(M+2))]
q = deque()
for _ in range(N):
    board.append(list('0'+input().strip()+'0'))
board.append(list('0'*(M+2)))
myMap = [[[[0 for _ in range(M+2)]for _ in range(N+2)]for _ in range(M+2)]for _ in range(N+2)]
x,y=-1,-1
a,b=0,0
for i in range(1,N+1):
    for j in range(1,M+1):
        if board[i][j]=='o':
            if x==-1:
                y,x=i,j
            else:
                b,a=i,j
                break
q.append([y,x,b,a])
dy,dx=[-1,0,1,0],[0,1,0,-1]
def escape(y,x):
    return x<1 or x>M or y<1 or y>N

def wall(y,x):
    return board[y][x]=='#'

def bfs():
    while q:
        y,x,b,a=q.popleft()    
        if myMap[y][x][b][a]>10:
            break

        if escape(y,x) ^ escape(b,a):
            print(myMap[y][x][b][a])
            return
        for i in range(4):
            my,mx,mb,ma=y+dy[i],x+dx[i],b+dy[i],a+dx[i]
            if escape(my,mx) and escape(mb,ma):
                continue
            if wall(my,mx) and wall(mb,ma):
                continue
            if wall(my,mx):
                my,mx=y,x
            elif wall(mb,ma):
                mb,ma=b,a
            if not myMap[my][mx][mb][ma]:
                q.append([my,mx,mb,ma])
                myMap[my][mx][mb][ma]=myMap[y][x][b][a]+1
                   
    print(-1)

bfs()  

