import sys,copy
input=sys.stdin.readline
N=int(input())
graph=[list(map(int,input().split())) for _ in range(N)]
ans=0
def dfs(ceil,board,travel):
    global ans
    if ceil>=5:
        return
    for i in range(4): ## 0: left //1: up //2: right //3:down//
        travel=copy.deepcopy(board)
        if i==0:
            for y in range(N):
                li=copy.deepcopy(travel[y])
                nl=[]
                for item in li:
                    ans=max(item,ans)
                    if item!= 0:
                        nl.append(item)
                for i in range(len(nl)):
                    if i+1<len(nl) and nl[i]!=0 and nl[i]==nl[i+1]:
                        nl[i]=nl[i]*2
                        ans=max(nl[i],ans)
                        del nl[i+1]
                zero=[0]*(N-len(nl))
                nl.extend(zero)
                travel[y]=nl

            
            tmp=board
            board=travel
            dfs(ceil+1,board,travel)
            board=tmp
                        
        elif i==1:
            traveler=list(map(list,zip(*travel)))
            for y in range(N):
                li=copy.deepcopy(traveler[y])
                nl=[]
                for item in li:
                    ans=max(item,ans)
                    if item!= 0:
                        nl.append(item)
                for i in range(len(nl)):
                    if i+1<len(nl) and nl[i]!=0 and nl[i]==nl[i+1]:
                        nl[i]=nl[i]*2
                        ans=max(nl[i],ans)
                        del nl[i+1]
                zero=[0]*(N-len(nl))
                nl.extend(zero)
                traveler[y]=nl

            travel=list(map(list,zip(*traveler)))
            tmp=board
            board=travel
            dfs(ceil+1,board,travel)
            board=tmp

        elif i==2:
            for y in range(N):
                li=copy.deepcopy(travel[y])
                nl=[]
                for item in li:
                    ans=max(item,ans)
                    if item!= 0:
                        nl.append(item)
                nl.reverse()
                for i in range(len(nl)):
                    if i+1<len(nl) and nl[i]!=0 and nl[i]==nl[i+1]:
                        nl[i]=nl[i]*2
                        ans=max(nl[i],ans)
                        del nl[i+1]
                zero=[0]*(N-len(nl))
                nl.extend(zero)
                nl.reverse()
                travel[y]=nl
            
            tmp=board
            board=travel
            dfs(ceil+1,board,travel)
            board=tmp
        elif i==3:
            traveler=list(map(list,zip(*travel)))
            for y in range(N):
                li=copy.deepcopy(traveler[y])
                nl=[]
                for item in li:
                    ans=max(item,ans)
                    if item!= 0:
                        nl.append(item)
                nl.reverse()
                for i in range(len(nl)):
                    if i+1<len(nl) and nl[i]!=0 and nl[i]==nl[i+1]:
                        nl[i]=nl[i]*2
                        ans=max(nl[i],ans)
                        del nl[i+1]
                zero=[0]*(N-len(nl))
                nl.extend(zero)
                nl.reverse()
                traveler[y]=nl
            
            travel=list(map(list,zip(*traveler)))
            tmp=board
            board=travel
            dfs(ceil+1,board,travel)
            board=tmp
    
dfs(0,graph,[])
print(ans)
## 빠른 코드 참조
