import sys

N,M = map(int,sys.stdin.readline().split())
ar = []
for _ in range(N):
    ar.append(list(map(int,sys.stdin.readline().split())))

def type1(y,x):
    if x+3<M:
        return ar[y][x]+ar[y][x+1]+ar[y][x+2]+ar[y][x+3]
    return 0
def type2(y,x):
    if y+3<N:
        return ar[y][x]+ar[y+1][x]+ar[y+2][x]+ar[y+3][x]
    return 0
def type3(y,x):
    if y+1<N and x+1<M:
        return ar[y][x]+ar[y][x+1]+ar[y+1][x]+ar[y+1][x+1]
    return 0
def type4(y,x):
    if x+1<M and y+2<N:
        return ar[y][x]+ar[y][x+1]+ar[y+1][x+1]+ar[y+2][x+1]
    return 0
def type5(y,x):
    if x+2<M and y-1>=0:
        return ar[y][x]+ar[y][x+1]+ar[y][x+2]+ar[y-1][x+2]
    return 0
def type6(y,x):
    if x+1<M and y+2<N:
        return ar[y][x]+ar[y+1][x]+ar[y+2][x]+ar[y+2][x+1]
    return 0
def type7(y,x):
    if x+2<M and y+1<N:
        return ar[y][x]+ar[y+1][x]+ar[y][x+1]+ar[y][x+2]
    return 0
def type8(y,x):
    if x+1<M and y+2<N:
        return ar[y][x]+ar[y][x+1]+ar[y+1][x]+ar[y+2][x]
    return 0
def type9(y,x):
    if x+1<M and y-2>=0:
        return ar[y][x]+ar[y][x+1]+ar[y-1][x+1]+ar[y-2][x+1]
    return 0
def type10(y,x):
    if x+2<M and y+1<N:
        return ar[y][x]+ar[y][x+1]+ar[y][x+2]+ar[y+1][x+2]
    return 0
def type11(y,x):
    if x+2<M and y+1<N:
        return  ar[y][x]+ar[y+1][x]+ar[y+1][x+1]+ar[y+1][x+2]
    return 0
def type12(y,x):
    if x+1<M and y+2<N:
        return ar[y][x]+ar[y+1][x]+ar[y+1][x+1]+ar[y+2][x+1]
    return 0
def type13(y,x):
    if x+2<M and y-1>=0:
        return ar[y][x]+ar[y][x+1]+ar[y-1][x+1]+ar[y-1][x+2]
    return 0
def type14(y,x):
    if x+1<M and y-1>=0 and y+1<N:
        return ar[y][x]+ar[y][x+1]+ar[y-1][x+1]+ar[y+1][x]
    return 0
def type15(y,x):
    if x+2<M and y+1<N:
        return ar[y][x]+ar[y][x+1]+ar[y+1][x+1]+ar[y+1][x+2]
    return 0
def type16(y,x):
    if x+2<M and y+1<N:
        return ar[y][x]+ar[y][x+1]+ar[y+1][x+1]+ar[y][x+2]
    return 0
def type17(y,x):
    if x+1<M and y-1>=0 and y+1<N:
        return ar[y][x]+ar[y][x+1]+ar[y-1][x+1]+ar[y+1][x+1]
    return 0
def type18(y,x):
    if x+2<M and y-1>=0:
        return ar[y][x]+ar[y][x+1]+ar[y-1][x+1]+ar[y][x+2]
    return 0
def type19(y,x):
    if x-1>=0 and y-1>=0 and y+1<N:
        return ar[y][x]+ar[y][x-1]+ar[y-1][x-1]+ar[y+1][x-1]
    return 0
ans=0
for i in range(N):
    for j in range(M):
        ans=max(ans,type1(i,j))
        ans=max(ans,type2(i,j))
        ans=max(ans,type3(i,j))
        ans=max(ans,type4(i,j))
        ans=max(ans,type5(i,j))
        ans=max(ans,type6(i,j))
        ans=max(ans,type7(i,j))
        ans=max(ans,type8(i,j))
        ans=max(ans,type9(i,j))
        ans=max(ans,type10(i,j))
        ans=max(ans,type11(i,j))
        ans=max(ans,type12(i,j))
        ans=max(ans,type13(i,j))
        ans=max(ans,type14(i,j))
        ans=max(ans,type15(i,j))
        ans=max(ans,type16(i,j))
        ans=max(ans,type17(i,j))
        ans=max(ans,type18(i,j))
        ans=max(ans,type19(i,j))
print(ans)