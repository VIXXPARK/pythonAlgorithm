import sys 
from collections import deque 
def grouping(i, j): # 섬마다 번호 붙이기 
    q = deque([(i, j)]) 
    world[i][j] = gid 
    while q: 
        qi, qj = q.popleft() 
        for t in range(4): 
            x, y = qi + dx[t], qj + dy[t] 
            if 0 <= x < n and 0 <= y < n: 
                if world[x][y] == 1: 
                    world[x][y] = gid 
                    q.append((x, y)) 
                elif world[x][y] == 0 and not (qi, qj) in ocean: 
                    ocean.append((qi, qj))
            
def get_distance(): # 모든 섬에서 동시에 확장 
    loop = 0 
    ans = sys.maxsize 
    while ocean: 
        loop += 1 
        length = len(ocean) 
        for _ in range(length): 
            oi, oj = ocean.popleft() 
            for t in range(4): 
                x, y = oi + dx[t], oj + dy[t] 
                if 0 <= x < n and 0 <= y < n: 
                    if world[x][y] == 0: 
                        world[x][y] = world[oi][oj] 
                        ocean.append((x, y)) 
                    elif world[x][y] < world[oi][oj]: 
                        ans = min(ans, (loop - 1) * 2) 
                    elif world[x][y] > world[oi][oj]: 
                        ans = min(ans, loop * 2 - 1) 
    return ans 
dx, dy = (0, 0, 1, -1), (1, -1, 0, 0) 
n = int(sys.stdin.readline()) 
world = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] 
ocean = deque() 
gid = -1 
for i in range(n): 
    for j in range(n): 
        if world[i][j] > 0: 
            grouping(i, j) 
            gid -= 1
    
sys.stdout.write(str(get_distance()))

# 출처: https://suri78.tistory.com/133 [공부노트]



N=int(input())
M=[list(map(int,input().split())) for _ in range(N)]
T=[[-1]*N for _ in range(N)]
P=[]
st=[]
c=0
for i in range(N):
    for j in range(N):
        if T[i][j]==-1:
            c+=1
            st.append((i,j))
            if M[i][j]==0:
                st.pop()
                T[i][j]=0
                c-=1
            else:
                while st:
                    a,b=st.pop()
                    T[a][b]=c
                    if a!=0 and M[a-1][b]==1 and T[a-1][b]==-1:
                        st.append((a-1,b))
                    if a!=N-1 and M[a+1][b]==1 and T[a+1][b]==-1:
                        st.append((a+1,b))
                    if b!=0 and M[a][b-1]==1 and T[a][b-1]==-1:
                        st.append((a,b-1))
                    if b!=N-1 and M[a][b+1]==1 and T[a][b+1]==-1:
                        st.append((a,b+1))
st=[[],[]]
c=0
d=1
M=[[-1]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if T[i][j]!=0:
            st[c%2].append((i,j))
t=False
while 1:
    if t:
        break
    if st[0]==st[1]:
        c,d=1,0
        break
    while st[c%2]:
        a,b=st[c%2].pop()
        if b!=N-1:
            if T[a][b+1]==0:
                st[(c+1)%2].append((a,b+1))
                T[a][b+1]=T[a][b]
                M[a][b+1]=c
            elif T[a][b+1]!=T[a][b]:
                if M[a][b+1]!=c:
                    d=0
                t=True
        if a!=0:
            if T[a-1][b]==0:
                st[(c+1)%2].append((a-1,b))
                T[a-1][b]=T[a][b]
                M[a-1][b]=c
            elif T[a-1][b]!=T[a][b]:
                if M[a-1][b]!=c:
                    d=0
                t=True
        if b!=0:
            if T[a][b-1]==0:
                st[(c+1)%2].append((a,b-1))
                T[a][b-1]=T[a][b]
                M[a][b-1]=c
            elif T[a][b-1]!=T[a][b]:
                if M[a][b-1]!=c:
                    d=0
                t=True
        if a!=N-1:
            if T[a+1][b]==0:
                st[(c+1)%2].append((a+1,b))
                T[a+1][b]=T[a][b]
                M[a+1][b]=c
            elif T[a+1][b]!=T[a][b]:
                if M[a+1][b]!=c:
                    d=0
                t=True
    c+=1
print(2*(c-1)+d)

# 4등 코드