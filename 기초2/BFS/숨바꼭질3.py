import sys
from collections import deque
def solve(visited,n,k):
    queue=deque()
    queue.append(n)
    travel[n]=True
    while queue:
        x=queue.popleft()
        if x==k:
            print(visited[x])
            return
        nx=set()
        nx.add(x+1)
        nx.add(x-1)
        nx.add(x*2)
        for t in nx:
            if 0<=t<100001 and visited[t]==0:
                if t==x*2 and not travel[t]:
                    visited[t]=visited[x]
                    travel[t]=True
                    queue.appendleft(t)
                else:
                    if visited[t]==0 and not travel[t]:
                        visited[t]=visited[x]+1
                        travel[t]=True
                        queue.append(t)

n,k=map(int,input().split())
visited=[0]*100001
travel=[False]*100001
solve(visited,n,k)