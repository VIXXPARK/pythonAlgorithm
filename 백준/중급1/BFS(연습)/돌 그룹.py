import sys
lst= list(map(int,sys.stdin.readline().split()))

def func(cnt):
    if all(isAvg):
        print(1)
        sys.exit()
    if cnt>10:
        return
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            if not isAvg[i] and not isAvg[j]:
                if lst[i]<lst[j]:
                    tmp=lst[i]
                    lst[j]-=lst[i]
                    lst[i]=tmp*2
                    if lst[i]==avg:
                        isAvg[i]=True
                    if lst[j]==avg:
                        isAvg[j]=True
                    func(cnt+1)
                    lst[i]=tmp
                    lst[j]+=tmp
                    isAvg[i]=False
                    isAvg[j]=False
                if lst[i]>lst[j]:
                    tmp=lst[j]
                    lst[i]-=lst[j]
                    lst[j]=tmp*2
                    if lst[i]==avg:
                        isAvg[i]=True
                    if lst[j]==avg:
                        isAvg[j]=True
                    func(cnt+1)
                    lst[j]=tmp
                    lst[i]+=tmp
                    isAvg[i]=False
                    isAvg[j]=False


if (lst[0]+lst[1]+lst[2])%3!=0:
    print(0)
else:
    avg=(lst[0]+lst[1]+lst[2])//3
    isAvg=[False]*3
    for val in range(len(lst)):
        if lst[val]==avg:isAvg[val]=True
    func(0)
    print(0)

### short & quick verison
import math
G=math.gcd
a,b,c=map(int,input().split())
s=(a+b+c)//G(a,G(b,c))
print(+(s%3<1>s//3&~-s//3))

## stand version

from collections import deque
import sys
input = sys.stdin.readline

def bfs(A, B, C):
    if A == B == C: return 1
    T = A+B+C
    visit = [[False]*(T+1) for _ in range(T+1)]
    visit[A][B] = True
    queue = deque([[A, B, C]])
    while queue:
        a, b, c = queue.popleft()
        for x, y in [(a, b), (a, c), (b, c)]:
            if x != y:
                y -= x
                x *= 2
                z = T-x-y
                if x == y == z: return 1
                temp = sorted([x, y, z])
                if not visit[temp[0]][temp[1]]:
                    visit[temp[0]][temp[1]] = True
                    queue.append(temp)
    return 0

print(bfs(*sorted(list(map(int, input().split())))))