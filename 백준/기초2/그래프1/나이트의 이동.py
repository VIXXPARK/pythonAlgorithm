import sys
from collections import deque
def func(y,x):
    if x>=0 and x<N and y>=0 and y<N:
        return True
    else:
        return False

def bfs():
    q = deque()
    q.append([y,x])
    while q:
        dot=q.popleft()
        if dot[0]==fy and dot[1]==fx:
            break
        for i in range(8):
            my=dot[0]+dy[i]
            mx=dot[1]+dx[i]
            if func(my,mx) and not graph[my][mx]:
                graph[my][mx]=graph[dot[0]][dot[1]]+1
                q.append([my,mx])


input=sys.stdin.readline
testCase=int(input())
for _ in range(testCase):
    N=int(input())
    y,x=map(int,input().split())
    fy,fx=map(int,input().split())
    graph=[[0]*N for _ in range(N)]
    count=0
    dy=[-2,-2,-1,1,2,2,1,-1]
    dx=[-1,1,2,2,1,-1,-2,-2]
    bfs()
    print(graph[fy][fx])