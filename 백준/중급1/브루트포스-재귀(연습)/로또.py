import sys
def func(celi,aim,ans):
    if celi==aim:
        print(' '.join(map(str,ans)))
        return
    
    for i in range(N):
        if not ans:
            visited[i]=True
            ans.append(li[i])
            func(celi+1,aim,ans)
            ans.pop()
            visited[i]=False
        else:
            if not visited[i] and ans[-1]<li[i]:
                visited[i]=True
                ans.append(li[i])
                func(celi+1,aim,ans)
                ans.pop()
                visited[i]=False
while True:
    li = list(map(int,sys.stdin.readline().rstrip().split()))
    if li[0]==0:
        break
    else:
        N=li[0]
        li=li[1:]
        visited=[False]*N
        func(0,6,[])
        print()