import sys
from collections import deque
N=int(sys.stdin.readline().rstrip())
graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    graph[int(a)].append(int(b))
    graph[int(b)].append(int(a))

visited= [0]*(N+1)
visited[1]=1

def bfs():
    q=deque()
    q.append(1)
    while q:
        dot=q.popleft()
        for i in graph[dot]:
            if not visited[i]:
                visited[i]=dot
                q.append(i)
bfs()
for i in range(2,N+1):
    print(visited[i])