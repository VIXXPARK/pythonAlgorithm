import sys
from collections import deque
input=sys.stdin.readline

def bfs(n):
    q=deque()
    q.append(n)
    visited[n]=True
    print(n+1,end=' ')
    while q:
        front=q.popleft()
        for i in range(N):
            if graph[front][i] and not visited[i]:
                print(i+1,end=' ')
                visited[i]=True
                q.append(i)

def dfs(n):
    visited[n]=True
    print(n+1,end=' ')
    for i in range(N):
        if graph[n][i] and not visited[i]:
            visited[i]=True
            dfs(i)

N,M,V=map(int,input().split())
graph=[[False]*N for _ in range(N)]
visited = [False]*N 
for _ in range(M):
    go,to=map(int,input().rstrip().split())
    graph[go-1][to-1]=True
    graph[to-1][go-1]=True
dfs(V-1)
visited=[False]*N
print()
bfs(V-1)


# import sys

# n ,m ,v = map(int, sys.stdin.readline().strip().split())

# edge = [[] for ii in range(n+1)]

# for i in range(m):
# 	a, b = map(int, sys.stdin.readline().strip().split())
# 	edge[a].append(b)
# 	edge[b].append(a)
	
# for e in edge:
# 	e.sort(reverse=True)
	
# def DFS():
# 	dfs = []
# 	stack = [v]
# 	visit = [0 for i in range(n+1)]
# 	while stack:
# 		node = stack.pop()
# 		if visit[node]:
# 			pass
# 		else:
# 			visit[node] = 1
# 			dfs.append(node)
# 			stack += edge[node]
# 	return dfs
	
# def BFS():
# 	bfs = []
# 	que = [v]
# 	visit = [0 for i in range(n+1)]
# 	visit[v] = 1
# 	while que:
# 		node = que.pop()
# 		bfs.append(node)
# 		for i in reversed(edge[node]):
# 			if visit[i]:
# 				continue
# 			visit[i] = 1
# 			que = [i] + que
# 	return bfs

# print(" ".join(map(str, DFS())))
# print(" ".join(map(str, BFS())))