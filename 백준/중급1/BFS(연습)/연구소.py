import sys
from collections import deque
from copy import deepcopy
from itertools import combinations
input=sys.stdin.readline
N,M=map(int,input().split())
graph=[list(map(int,input().split())) for _ in range(N)]
dy,dx=[1,-1,0,0],[0,0,1,-1]
def scope(y,x):
    return y>=0 and y<N and x>=0 and x<M

def bfs(board,numList,wallCnt,virusCnt):
    q=numList
    secureArea=N*M-wallCnt-3-virusCnt
    count=0
    while q:
        info=q.popleft()
        y=info//M
        x=info%M
        for i in range(4):
            my,mx = y+ dy[i],x+dx[i]
            if scope(my,mx) and board[my][mx]!=1 and board[my][mx]!=2:
                board[my][mx]=2
                count+=1
                q.append(M*my+mx)
    secureArea-=count
    return secureArea

ans=0
queue=deque()
oneNum=0
virusArea=0
li=[]
for i in range(N):
    for j in range(M):
        if graph[i][j]==0:
            li.append(M*i+j)
        elif graph[i][j]==2:
            val=M*i+j
            virusArea+=1
            queue.append(val)
        elif graph[i][j]==1:
            oneNum+=1
for check in combinations(li,3): ## combinations는 조합의 기능으로서 역할을 한다.
    for k in check:
        graph[k//M][k%M]=1 ## 비트마스크에서 배웠던 표현에서 적용
    ans=max(ans,bfs(deepcopy(graph),deepcopy(queue),oneNum,virusArea)) ## deepcopy(복사를 원하는 value)하면 깊은 복사가 된다.
    for k in check:
        graph[k//M][k%M]=0
print(ans)
