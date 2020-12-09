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
        return
    for i in range(1,len(li)):
        if not passing[i] and ans[-1]<li[i]:
            passing[i]=True
            ans.append(i)
            func(ans,celi+1,aim)
            ans.pop()
            passing[i]=False
ans=[0]
passing[0]=True
func(ans,0,N//2-1)
print(ret)


# import sys
# input = sys.stdin.readline

# N = int(input())
# S = [list(map(int,input().split())) for _ in range(N)]

# ret = []
# def sol(start,link,s1,s2,i):
#   if i == N:
#     ret.append(abs(s1-s2))
#     return
#   if len(start) < N//2:
#     start.append(i)
#     temp = 0
#     for j in start:
#       temp += S[j][i] + S[i][j]
#     sol(start,link,s1+temp,s2,i+1)
#     start.pop()
#   if len(link) < N//2:
#     link.append(i)
#     temp = 0
#     for j in link:
#       temp += S[j][i] + S[i][j]
#     sol(start,link,s1,s2+temp,i+1)
#     link.pop()
#   return
# sol([0],[],0,0,1)
# print(min(ret))