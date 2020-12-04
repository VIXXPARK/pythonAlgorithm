import sys
N,M=map(int,sys.stdin.readline().split())
li=[]
def func(ar,celi):
    if celi>M:
        return
    if celi==M:
        print(' '.join(ar))
    
    for i in range(1,N+1):
        if not ar:
            ar.append(str(i))
            func(ar,celi+1)
            ar.pop()
        elif int(ar[-1])<=i:
            ar.append(str(i))
            func(ar,celi+1)
            ar.pop()
func(li,0)
