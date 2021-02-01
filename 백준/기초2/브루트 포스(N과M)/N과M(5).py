import sys
N,M = map(int,sys.stdin.readline().split())
li=[int(i) for i in sys.stdin.readline().split()]
ans=[]
passing=[False]*N
li.sort()
def func(celi):
    if celi==M:
        print(' '.join(ans))
    for i in range(N):
        if not ans:
            passing[i]=True
            ans.append(str(li[i]))
            func(celi+1)
            ans.pop()
            passing[i]=False
        else:
            if not passing[i]:
                passing[i]=True
                ans.append(str(li[i]))
                func(celi+1)
                ans.pop()
                passing[i]=False
func(0)


    