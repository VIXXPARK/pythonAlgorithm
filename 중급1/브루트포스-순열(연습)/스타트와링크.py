import sys
N =int(sys.stdin.readline().rstrip())
graph=[list(map(int,sys.stdin.readline().rstrip().split())) for _ in range(N)]
start=[0]
link=set([int(i) for i in range(N)])
visited=[False]*N
visited[0]=True
ans=sys.maxsize
def func(celi,aim):
    global ans,start,link
    if celi==aim-1:
        left=0
        right=0
        for i in start:
            for j in start:
                left+=graph[i][j]
        
        tmp=link.difference(set(start))
        for i in tmp:
            for j in tmp:
                right+=graph[i][j]
        ans=min(ans,int(abs(right-left)))
        return
    for i in range(1,N):
        if not visited[i] and start[-1]<i: #대소관계 중요!!!
            visited[i]=True
            start.append(i)
            func(celi+1,aim)
            start.pop()
            visited[i]=False

func(0,N//2)
print(ans)
