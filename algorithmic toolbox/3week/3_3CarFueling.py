distance=int(input())
segment=int(input())
dist=int(input())
stops=[0]+list(map(int,input().split()))
curStop=0
cnt=0
while curStop<len(stops)-1:
    finishStop=curStop
    if stops[curStop]+segment>=distance:
        print(cnt)
        quit()
    while curStop<len(stops)-1 and stops[curStop+1]-stops[finishStop]<=segment:
        curStop+=1
    if curStop==finishStop or (curStop==len(stops)-1 and stops[curStop]+segment<distance):
        print(-1)
        quit()
    if curStop<len(stops):
        cnt+=1
print(cnt)
        

