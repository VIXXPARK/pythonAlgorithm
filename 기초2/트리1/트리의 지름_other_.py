import sys
from collections import deque
N=int(sys.stdin.readline().rstrip())
graph=[[] for _ in range(N+1)]
for _ in range(N):
    info=list(map(int,sys.stdin.readline().rstrip().split()))
    start=info[0]
    for x in range(1,len(info)-1,2):
        graph[start].append([info[x],info[x+1]])

def bfs(n,mode):
    q =deque()
    q.append(n)
    val = [-1]*(N+1)
    val[n]=0
    while q:
        dot=q.popleft()
        for x in graph[dot]:
            if val[x[0]]==-1:
                val[x[0]]=val[dot]+x[1]
                q.append(x[0])
    
    if mode==1:
        return val.index(max(val))
    else:
        return max(val)

print(bfs(bfs(1,1),2))
