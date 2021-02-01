import sys
graph=[list(map(int,sys.stdin.readline().split()))for _ in range(9)]
xSet=[list([False]*10)for _ in range(9)]
ySet=[list([False]*10)for _ in range(9)]
box=[list([False]*10) for _ in range(9)]
dia=[[i//3*3+j//3 for j in range(9)]for i in range(9)]
spot=[]
for i in range(9):
    for j in range(9):
        if graph[i][j]==0:
            spot.append([i,j])
        else:
            xSet[i][graph[i][j]]=True
            ySet[j][graph[i][j]]=True
            box[dia[i][j]][graph[i][j]]=True

def travel(ceil):
    if ceil==len(spot):
        for i in range(9):
            print(' '.join(map(str,graph[i])))
        exit()
    y,x=spot[ceil]
    for val in range(1,10):
        if xSet[y][val] or ySet[x][val] or box[dia[y][x]][val]: continue

        xSet[y][val]=ySet[x][val]=box[dia[y][x]][val]=True
        graph[y][x]=val
        travel(ceil+1)
        xSet[y][val]=ySet[x][val]=box[dia[y][x]][val]=False
        graph[y][x]=0

travel(0)

