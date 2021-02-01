import sys
from collections import deque
N = int(sys.stdin.readline().rstrip())
graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b= map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1,N+1):
    graph[i].sort()
ans=list(map(int,sys.stdin.readline().split()))
stk=[]
flag=False
visited = [False]*(N+1)
def bfs(n):
    global flag
    q =deque()
    visited[n]=True
    q.append(n)
    start=1
    tmp=[]
    while q:
        stk=[]
        for i in graph[q.popleft()]:
            if not visited[i]:
                visited[i]=True
                stk.append(i)
        li=ans[start:start+len(stk)]
        tmp=list(li)
        start=start+len(stk)
        li.sort()
        if li!=stk:
            flag=True
            break
        else:
            for i in tmp:
                q.append(i)
if ans[0]==1:       
    bfs(1)
    print(1) if not flag else print(0)
else:
    print(0)
