import sys
N,M = map(int,sys.stdin.readline().split())
li=[int(i) for i in sys.stdin.readline().split()]
passing=[False]*N
li.sort()
ans=[]
def func(celi):
    if celi==M:
        print(' '.join(ans))
    for i in range(N):
        if not ans:
            passing[i]=True
            ans.append(str(li[i]))
            func(celi+1)
            passing[i]=False
            ans.pop()
        else:
            if not passing[i] and int(ans[-1])<li[i]:
                passing[i]=True
                ans.append(str(li[i]))
                func(celi+1)
                passing[i]=False
                ans.pop()

func(0)