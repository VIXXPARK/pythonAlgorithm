N=int(input())
graph=[[] for _ in range(N)]
for _ in range(N):
    dot,left,right=map(str,input().split())
    graph[ord(dot)-ord('A')].append(left)
    graph[ord(dot)-ord('A')].append(right)

def pre_order(start):
    if start!='.':
        print(start,end='')
        pre_order(graph[ord(start)-ord('A')][0])
        pre_order(graph[ord(start)-ord('A')][1])
def mid_order(start):
    if start!='.':
        mid_order(graph[ord(start)-ord('A')][0])
        print(start,end='')
        mid_order(graph[ord(start)-ord('A')][1])
def post_order(start):
    if start!='.':
        post_order(graph[ord(start)-ord('A')][0])
        post_order(graph[ord(start)-ord('A')][1])
        print(start,end='')
pre_order('A')
print()
mid_order('A')
print()
post_order('A')

