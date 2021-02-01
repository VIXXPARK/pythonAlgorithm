import sys
from collections import deque
N=int(sys.stdin.readline())
graph=[[] for _ in range(N+1)] ## 그래프
isRoot = [0]*(N+1) ## 루트확인하는 리스트
distance= [[] for _ in range(N+1)] ## 거리값 저장하는 리스트
root=0
for _ in range(N):
    parent,left,right=map(int,sys.stdin.readline().rstrip().split())
    graph[parent].append(left)
    graph[parent].append(right)
    isRoot[parent]+=1
    if left!=-1:
        isRoot[left]+=1
    if right!=-1:
        isRoot[right]+=1
for i in range(1,N+1): #루트를 제외한 모든 점들은 2의 값을 가지기 때문에
    if isRoot[i]==1:
        root=i
num=1
def inorder(start,deep): #deep은 레벨에 관련된 값, num은 거리에 관련된 값이다.
    global num
    if graph[start][0]!=-1:
        inorder(graph[start][0],deep+1)
    distance[deep].append(num)
    num+=1
    if graph[start][1]!=-1:
        inorder(graph[start][1],deep+1)

inorder(root,1)
level=1
ans= max(distance[1])-min(distance[1])+1
for i in range(2,N+1):
    if distance[i]:
        small=min(distance[i]) ## 각 층마다의 거리를 계산하여 최댓값인지 확인한다.
        large=max(distance[i])
        if ans<large-small+1:
            ans=large-small+1
            level=i
print(level)
print(ans)

#https://pacific-ocean.tistory.com/331
