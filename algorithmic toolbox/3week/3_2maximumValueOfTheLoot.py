n,W =map(int,input().split())
lst=[]
for _ in range(n):
    a,b=map(int,input().split())
    lst.append([a/b,a,b])
lst.sort(reverse=True)
forward=0
ans=0
while W>0:
    if forward==n:
        print(ans)
        quit()
    if W-lst[forward][2]>=0:
        W-=lst[forward][2]
        ans+=lst[forward][1]
    else:
        ans+=lst[forward][0]*W
        W=0
    forward+=1
print(ans)