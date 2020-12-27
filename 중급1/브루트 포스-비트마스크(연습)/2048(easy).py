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

from itertools import chain
import sys
read = sys.stdin.readline

n = int(read().strip())
blocks = [list(map(int, read().strip().split())) for _ in range(n)]


def move_blocks(now_blocks, depth, direction):
    # 위 아래 경우에는 transpose
    if direction == 0 or direction == 1:
        now_blocks = list(map(list, zip(*now_blocks)))

    nxt_blocks = []
    for line in now_blocks:
        non_zero = [i for i in line if i] ##0이 아닌 값들만 추출

        # 왼쪽으로 move
        if direction == 0 or direction == 3:
            for i in range(1, len(non_zero)):
                if non_zero[i-1] == non_zero[i]:
                    non_zero[i-1] += non_zero[i]
                    non_zero[i] = 0

            non_zero = [i for i in non_zero if i]
            non_zero = non_zero + [0]*(n-len(non_zero))

        else:
            for i in range(len(non_zero)-1, 0, -1):
                if non_zero[i-1] == non_zero[i]:
                    non_zero[i] += non_zero[i-1]
                    non_zero[i-1] = 0

            non_zero = [i for i in non_zero if i]
            non_zero = [0] * (n - len(non_zero)) + non_zero

        nxt_blocks.append(non_zero)

    if direction == 0 or direction == 1:
        nxt_blocks = list(map(list, zip(*nxt_blocks)))

    if depth == 5:
        global max_value
        max_value = max(max_value, max(list(chain(*nxt_blocks))))
        return

    move_blocks(nxt_blocks, depth+1, 0)
    move_blocks(nxt_blocks, depth+1, 1)
    move_blocks(nxt_blocks, depth+1, 2)
    move_blocks(nxt_blocks, depth+1, 3)


max_value = 0
for i in range(4):
    move_blocks(blocks, 1, i)
print(max_value)