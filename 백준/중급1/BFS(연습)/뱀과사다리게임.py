import sys
from collections import deque
sys.setrecursionlimit(int(10e5))
input=sys.stdin.readline
N,M=map(int,input().split())
increase=[0]*101
decrease=[0]*101
lst=[sys.maxsize]*101
for _ in range(N):
    u,v=map(int,input().split())
    increase[u]=v
for _ in range(M):
    u,v=map(int,input().split())
    decrease[u]=v
lst[0],lst[1]=0,0
def bfs():
    q=deque()
    q.append(1)
    while q:
        start=q.popleft()
        if start==100:
            return
        for i in range(start+6,start,-1):
            if i<=100:
                if increase[i]:
                    lst[increase[i]]=min(lst[increase[i]],lst[start]+1)
                    q.appendleft(increase[i])
                elif decrease[i]:
                    lst[decrease[i]]=min(lst[decrease[i]],lst[start]+1)
                    q.append(decrease[i])
                else:
                    if lst[start]+1<lst[i]:
                        lst[i]=lst[start]+1
                        q.append(i)

bfs()
print(lst[100])

## 주사위 같이 한 번 던질 때 여러 범위가 동시에 확인해야 하는 경우에는 넓이 우선 순회 (bfs)!!