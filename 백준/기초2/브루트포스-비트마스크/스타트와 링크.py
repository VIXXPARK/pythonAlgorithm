import sys
N=int(sys.stdin.readline())
li = [list(map(int,sys.stdin.readline().split()))for _ in range(N)]
start=[]
link=[]
ans=10e9
for i in range(1<<N):
    start.clear()
    link.clear()
    for k in range(N):
        if (i &(1<<k))==0:
            start.append(k)
        else:
            link.append(k)
    
    if len(start)>N//2 : continue
    if len(link)>N//2 : continue

    startVal=0
    linkVal=0
    for x in range(N//2):
        for y in range(N//2):
            if x!=y:
                startVal+=li[start[x]][start[y]]
                linkVal+=li[link[x]][link[y]]
    
    diff=abs(startVal-linkVal)
    ans=min(ans,diff)

print(ans)