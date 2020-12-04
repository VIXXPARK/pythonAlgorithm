import sys
N,M=map(int,sys.stdin.readline().split())
li=[]
passing=[False]*9
def func(ar,celi):
    if celi==M:
        print(' '.join(ar))
    for i in range(1,N+1):
        if passing[i]!=True:
            passing[i]=True
            ar.append(str(i))
            func(ar,celi+1)
            passing[i]=False
            ar.pop()
func(li,0)
