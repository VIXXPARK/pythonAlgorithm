import bisect
coordX=[]
coordY={}
def isDominated(x,y):
    it=bisect.bisect_left(coordX,x,0,len(coordX))
    if it==len(coordX):
        return False
    return y<coordY[coordX[it]]

def removeDominated(x,y):
    it=bisect.bisect_left(coordX,x,0,len(coordX))
    if it==0:
        return
    it-=1
    while True:
        if coordY[coordX[it]]>y:
            break
        if it==0:
            del coordX[it]
            break
        else:
            del coordX[it]
            it-=1

def registered(x,y):
    if isDominated(x,y):
        return len(coordX)
    removeDominated(x,y)
    coordX.append(x)
    coordY[x]=y
    return len(coordX)


lst=[[1,5],[2,4],[3,3],[4,2],[5,1]]

for loc in lst:
    print(registered(loc[0],loc[1]))
    coordX.sort()