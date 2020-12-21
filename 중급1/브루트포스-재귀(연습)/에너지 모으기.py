import sys
input=sys.stdin.readline
N=int(input())
li=list(map(int,input().split()))
visited=[False]*N
visited[0]=True
visited[-1]=True
ans=list(li)
ret=0

def func(sum,x):
    global ret
    if all(visited):
        ret=max(ret,sum)
        return
    for i in range(1,N):
        if not visited[i]:
            visited[i]=True
            x[i]=-1
            left=0
            right=0
            for j in range(i-1,-1,-1):
                if x[j]!=-1:
                    left=x[j]
                    break
            for k in range(i+1,N):
                if x[k]!=-1:
                    right=x[k]
                    break
            tmp=left*right
            sum+=tmp
            func(sum,x)
            sum-=tmp
            x[i]=li[i]
            visited[i]=False
          
func(0,ans)
print(ret)

## 좀 느리므로 다른 코드 참조
n=int(input())
L=list(map(int,input().split()))
def f(L):
    if len(L)==3: return L[0]*L[2]
    ret=0
    for i in range(1,len(L)-1):
        r=L[i-1]*L[i+1]+f(L[:i]+L[i+1:])
        ret=max(ret,r)
    return ret
print(f(L))