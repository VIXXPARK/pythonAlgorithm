import sys
N,M=map(int,input().split())
graph=[[] for _ in range(N)]
visited = [False]*N
start=0
for x in range(M):
    a,b=map(int,input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
    start=a

def dfs(n,val):
    global visited,graph
    if val==4:
        print(1)
        exit()
    if graph[n]:
        for i in graph[n]:
            if not visited[i]:
                visited[i]=True
                dfs(i,val+1)
                visited[i]=False


for i in range(N):
    visited[i]=True
    dfs(i,0)
    visited[i]=False

print(0)
