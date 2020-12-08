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
    if ans<ret:
        ans+=li[y][x]
        for i in range(N):
            if not travel[i] and li[x][i]!=0:
                travel[i]=True
                func(x,i,final,ans,cnt+1)
                travel[i]=False
        if cnt==N:
            if li[x][final]!=0:
                ans+=li[x][final]
                ret=min(ret,ans)
                return
            else:
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

# N=int(input())
# W=[list(map(int,input().split()))for i in range(N)]
# V=[0]*N
# M=1e10
# def back_track(n,c):
#     global N,W,V,M
#     if c<M:
#         if all(V) and n==0:
#             M=min(M,c)
#         for i in range(N):
#             if W[n][i]>0 and not V[i]:
#                 V[i]+=1
#                 back_track(i,c+W[n][i])
#                 V[i]-=1
# back_track(0,0)
# print(M)