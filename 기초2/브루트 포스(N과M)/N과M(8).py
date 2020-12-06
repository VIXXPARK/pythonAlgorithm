import sys
N,M = map(int,sys.stdin.readline().split())
li=[int(i) for i in sys.stdin.readline().split()]
li.sort()
ans=[]
def func(celi):
    if celi==M:
        print(' '.join(ans))
        return
    for i in range(N):
        if not ans:
            ans.append(str(li[i]))
            func(celi+1)
            ans.pop()
        else:
            if int(ans[-1])<=li[i]:
                ans.append(str(li[i]))
                func(celi+1)
                ans.pop()

func(0)