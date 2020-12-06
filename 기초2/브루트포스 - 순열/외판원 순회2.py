import sys
N = int(sys.stdin.readline().rstrip())
li=[]
for _ in range(N):
    li.append(list(map(int,sys.stdin.readline().rstrip().split())))
travel=[False]*N
final=0
ret=10000000000
def func(y,x,final,ans,cnt):
    global ret
    go=False
    ans+=li[y][x]
    for i in range(N):
        if not travel[i] and li[x][i]!=0:
            travel[i]=True
            func(x,i,final,ans,cnt+1)
            go=True
            travel[i]=False
    if cnt==N:
        if li[x][final]!=0:
            ans+=li[x][final]
            ret=min(ret,ans)
            return
        else:
            return



for i in range(N):
    for j in range(N):
        if i!=j and li[i][j]!=0:
            travel[i]=True
            travel[j]=True
            final=i
            func(i,j,final,0,2)
            travel[i]=False
            travel[j]=False
print(ret)