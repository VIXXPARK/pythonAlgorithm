import sys
N,M = map(int,sys.stdin.readline().split())
li=[int(i) for i in sys.stdin.readline().split()]
init=[False]*10001
dic = set(li)
li=list(dic)
li.sort()
ans=[]

def func(celi):
    if celi==M:
        print(' '.join(ans))
        return
    for i in range(len(li)):
        if not ans:
            if init[li[i]]!=True:
                init[li[i]]=True
                ans.append(str(li[i]))
                func(celi+1)
                ans.pop()
        else:
            ans.append(str(li[i]))
            func(celi+1)
            ans.pop()

func(0)