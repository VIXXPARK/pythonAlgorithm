import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
def bfs(start,end):
    visited=[False]*10001
    q=deque()
    q.append([start,''])
    while q:
        dot,ans=q.popleft()
        val=(dot*2)%10000
        Lstr=(dot%1000)*10+(dot//1000) ##문제를 제대로 읽읍시다 ㅠㅠ
        Rstr=(dot%10)*1000+(dot//10)
        
        if val==end: return ans+'D'
        elif not visited[val]:
            visited[val]=True
            q.append([val,ans+'D'])
            
        minus = dot-1 if dot!=0 else 9999  
        if minus==end:
            return ans+'S'
        elif not visited[minus]:
            visited[minus]=True
            q.append([minus,ans+'S'])
            
        if Lstr==end: return ans+'L'
        elif not visited[Lstr]:
            visited[Lstr]=True
            q.append([Lstr,ans+'L'])

        if Rstr==end: return ans+'R'  
        elif not visited[Rstr]:
            visited[Rstr]=True
            q.append([Rstr,ans+'R'])

for _ in range(N):
    left,right=map(int,input().rstrip().split())
    print(bfs(left,right))
    
## 나중에 더 빠른 코드 참조
import sys
from collections import deque
input=sys.stdin.readline
N=int(input())
def D(a):
    return (a*2)%10000
def S(a):
    if a==0:
        return 9999
    else: return a-1
def L(a):
    if a<1000:return a*10
    else:
        b=a//1000
        return (a-(1000*b))*10+b
def R(a):
    b=a%10
    return a//10 + b*1000

def bfs2(node):
    q=deque()
    q.append(left)
    visited[left]=1
    while q:
        x=q.popleft()
        a=D(x)
        b=S(x)
        c=L(x)
        d=R(x)
        if visited[a]==-1:
            visited[a]=x
            chainVal[a]='D'
            q.append(a)

        if visited[b]==-1:
            visited[b]=x
            chainVal[b]='S'
            q.append(b)

        if visited[c]==-1:
            visited[c]=x
            chainVal[c]='L'
            q.append(c)

        if visited[d]==-1:
            visited[d]=x
            chainVal[d]='R'
            q.append(d)
        
        if a==node or b==node or c==node or d==node:
            return
        

for _ in range(N):
    visited=[-1]*10001
    chainVal=['']*10001
    left,right=map(int,input().rstrip().split())
    ans=""
    bfs2(right)
    while right!=left:
        ans+=str(chainVal[right])
        right=visited[right]
    print(ans[::-1])