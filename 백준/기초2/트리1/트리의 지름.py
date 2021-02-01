import sys
from collections import deque
N=int(sys.stdin.readline().rstrip())
graph=[[] for _ in range(N)]
for _ in range(N-1):
    a,b,val=map(int,sys.stdin.readline().rstrip().split())
    graph[a-1].append([b-1,val])
    graph[b-1].append([a-1,val])

def bfs(start,mode):
    q=deque()
    val=[-1]*N
    val[start]=0
    q.append(start)
    while q:
        dot=q.popleft()
        for x in graph[dot]:
            if val[x[0]]==-1:
                val[x[0]]=x[1]+val[dot]
                q.append(x[0])
    
    if mode==1:
        return val.index(max(val))
    else:
        return max(val)

print(bfs(bfs(0,1),2))

#https://chldkato.tistory.com/29
