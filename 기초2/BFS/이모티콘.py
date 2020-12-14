import sys
from collections import deque
S=int(input())
visited=[[-1]*3001 for _ in range(3001)]

def bfs(left,right):
    q=deque()
    q.append([left,right])
    visited[left][right]=0
    while q:
        emoti,clip=q.popleft()
        if emoti==S:
            break
        if clip:
            if visited[emoti+clip][clip]==-1 and emoti+clip<=S:
                visited[emoti+clip][clip]=visited[emoti][clip]+1
                q.append([emoti+clip,clip])

            if visited[emoti][emoti]==-1:
                q.append([emoti,emoti])
                visited[emoti][emoti]=visited[emoti][clip]+1

            if visited[emoti-1][clip]==-1 and emoti-1>0:
                visited[emoti-1][clip]=visited[emoti][clip]+1
                q.append([emoti-1,clip])
        else:
            q.append([emoti,emoti])
            visited[emoti][emoti]=visited[emoti][clip]+1
        
bfs(1,0)
ans=10e9
for i in range(S+1):
    if visited[S][i]!=-1:
        ans=min(ans,visited[S][i])
print(ans)