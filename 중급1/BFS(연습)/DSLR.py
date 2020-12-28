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

    