import sys
N=int(sys.stdin.readline())
ar=[]
passing=[False]*(N)
for _ in range(N):
    ar.append(list(map(int,sys.stdin.readline().split())))
li = [int(i) for i in range(N)]
ret=10e9
def func(ans,celi,aim):
    global li
    global passing
    global ret
    if celi==aim:
        val1=0
        val2=0
        link = set(li)
        link=link.difference(set(ans))
        for x in ans:
            for y in ans:
                if x!=y:
                    val1+=ar[x][y]
        for a in link:
            for b in link:
                if a!=b:
                    val2+=ar[a][b]
        ret=min(ret,abs(val1-val2))
        return
    for i in range(1,len(li)):
        if not passing[i] and ans[-1]<li[i]:
            passing[i]=True
            ans.append(i)
            func(ans,celi+1,aim)
            ans.pop()
            passing[i]=False
ans=[0]
passing[0]=True
func(ans,0,N//2-1)
print(ret)