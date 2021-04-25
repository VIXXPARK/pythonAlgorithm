import bisect
s=[[72,50],[57,67],[74,55],[64,60]]
coord=[]

def isDominated(x,y):
    it=bisect.bisect_left(coord,[x,y],0,len(coord))
    if(it==len(coord)): return False
    return y<coord[it][1]

def removeDominated(x,y):
    it=bisect.bisect_left(coord,[x,y],0,len(coord))
    if it==0: return
    it-=1
    while True:
        if coord[it][1]>y: break
        if it==0:
            coord.pop()
            break
        else:
            del coord[it]


def registerd(x,y):
    if isDominated(x,y):return len(coord)
    removeDominated(x,y)
    coord.append([x,y])
    return len(coord)

ans=0
for val in s:
    ans+=registerd(val[0],val[1])

print(ans)