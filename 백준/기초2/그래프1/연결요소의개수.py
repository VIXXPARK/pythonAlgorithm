import sys
from collections import deque
input=sys.stdin.readline

def bfs(n):
    q=deque()
    q.append(n)
    visited[n]=True
    while q:
        front=q.popleft()
        for i in edge[front]:
            if not visited[i]:
                visited[i]=True
                q.append(i)


N,M=map(int,input().split())
edge=[[]for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    go,to=map(int,input().split())
    edge[go].append(to)
    edge[to].append(go)

for i in range(1,N+1):
    edge[i].sort()

count=0
for i in range(1,N+1):
    if not visited[i]:
        count+=1
        bfs(i)

print(count)