import sys

flag=False
def check(y,x,n1,n2,shape):
    if shape:
        if xSet[y][n1] or xSet[y][n2]:return False
        if ySet[x][n1] or ySet[x+1][n2]:return False
        if box[dia[y][x]][n1] or box[dia[y][x+1]][n2]:return False
        return True
    else:
        if xSet[y][n1] or xSet[y+1][n2]:return False
        if ySet[x][n1] or ySet[x][n2]:return False
        if box[dia[y][x]][n1] or box[dia[y+1][x]][n2]:return False
        return True

def engrave(y,x,n1,n2,shape,Inout):
    domino[n1][n2]=Inout
    domino[n2][n1]=Inout
    if shape:
        if Inout:
            graph[y][x]=n1
            graph[y][x+1]=n2
        else:
            graph[y][x]=0
            graph[y][x+1]=0
        xSet[y][n1],xSet[y][n2]=Inout,Inout
        ySet[x][n1],ySet[x+1][n2]=Inout,Inout
        box[dia[y][x]][n1],box[dia[y][x+1]][n2]=Inout,Inout
    else:
        if Inout:
            graph[y][x]=n1
            graph[y+1][x]=n2
        else:
            graph[y][x]=0
            graph[y+1][x]=0
        xSet[y][n1],xSet[y+1][n2]=Inout,Inout
        ySet[x][n1],ySet[x][n2]=Inout,Inout
        box[dia[y][x]][n1],box[dia[y+1][x]][n2]=Inout,Inout




def travel(ceil):
    global flag
    if flag: return
    if ceil==81:
        for i in range(9):
            print(''.join(map(str,graph[i])))
        flag=True
        return

    y,x=ceil//9,ceil%9
    if graph[y][x]!=0:
        travel(ceil+1)
    else:
        if x<=7 and graph[y][x+1]==0:
            for i in range(1,10):
                for j in range(i+1,10):
                    if not domino[i][j]:
                        if check(y,x,i,j,True):
                            engrave(y,x,i,j,True,True)
                            travel(ceil+2)
                            engrave(y,x,i,j,True,False)
                        if check(y,x,j,i,True):
                            engrave(y,x,j,i,True,True)
                            travel(ceil+2)
                            engrave(y,x,j,i,True,False)
        if y<=7 and graph[y+1][x]==0:
            for i in range(1,10):
                for j in range(i+1,10):
                    if not domino[i][j]:
                        if check(y,x,i,j,False):
                            engrave(y,x,i,j,False,True)
                            travel(ceil+1)
                            engrave(y,x,i,j,False,False)
                        if check(y,x,j,i,False):
                            engrave(y,x,j,i,False,True)
                            travel(ceil+1)
                            engrave(y,x,j,i,False,False)




count=1
while True:
    graph=[list([0]*9) for _ in range(9)]
    xSet=[list([False]*10)for _ in range(9)]
    ySet=[list([False]*10)for _ in range(9)]
    box=[list([False]*10) for _ in range(9)]
    dia=[[i//3*3+j//3 for j in range(9)]for i in range(9)]
    domino=[[False]*10 for _ in range(10)]
    N=int(sys.stdin.readline())
    if N==0:
        break
    for _ in range(N):
        u,lu,v,lv = map(str,sys.stdin.readline().rstrip().split())
        ly,lx,ry,rx=ord(lu[0])-ord('A'),int(lu[1])-1,ord(lv[0])-ord('A'),int(lv[1])-1
        graph[ly][lx]=int(u)
        graph[ry][rx]=int(v)
        domino[int(u)][int(v)]=domino[int(v)][int(u)]=True
        xSet[ly][int(u)]=True
        ySet[lx][int(u)]=True
        xSet[ry][int(v)]=True
        ySet[rx][int(v)]=True
        box[dia[ly][lx]][int(u)]=True
        box[dia[ry][rx]][int(v)]=True
    dot=list(sys.stdin.readline().rstrip().split())
    for i in range(9):
        y,x=ord(dot[i][0])-ord('A'),int(dot[i][1])-1
        graph[y][x]=i+1
        xSet[y][i+1]=True
        ySet[x][i+1]=True
        box[dia[y][x]][i+1]=True

    print("Puzzle ",end='')
    print(count)
    flag=False
    travel(0)
    count+=1
