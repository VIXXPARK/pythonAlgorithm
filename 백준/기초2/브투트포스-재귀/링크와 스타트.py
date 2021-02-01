import sys
N=int(sys.stdin.readline())
ar=[]
passing=[False]*(N)
for _ in range(N):
    ar.append(list(map(int,sys.stdin.readline().split())))
li = [int(i) for i in range(N)]
ret=10e9
def func(ans,celi,aim):
    global li
    global passing
    global ret
    if celi==aim:
        return
    for i in range(1,len(li)):
        if not passing[i] and ans[-1]<li[i]:
            passing[i]=True
            ans.append(i)
            val1=0
            val2=0
            link = set(li)
            link=link.difference(set(ans))
            for x in ans:
                for y in ans:
                    if x!=y:
                        val1+=ar[x][y]
            for a in link:
                for b in link:
                    if a!=b:
                        val2+=ar[a][b]
            ret=min(ret,abs(val1-val2))
            func(ans,celi+1,aim)
            ans.pop()
            passing[i]=False
ans=[0]
passing[0]=True
func(ans,0,N)
print(ret)


# import sys
# input = sys.stdin.readline
# M = int(sys.stdin.readline())
# N = M // 2
# stat = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
# row = [sum(i) for i in stat]
# col = [sum(i) for i in zip(*stat)]
# newstat = [i+ j for i, j in zip(row, col)]
# allstat = sum(newstat) // 2
# newstat.sort()
# c = [0]
# for i in newstat[:N]:
#     c.extend([i + j for j in c])
# bot_up = [False] * (allstat + 1)
# for i in c:
#     bot_up[i] = True
# for i in newstat[N:]:
#     bot_up[i:] = [a or b for a, b in zip(bot_up[i:], bot_up)]
# for i in range(allstat, -1, -1):
#     if bot_up[i]:
#         print(allstat - i)
#         break