distance=int(input())
segment=int(input())
dist=int(input())
stops=[0]+list(map(int,input().split()))
curStop=0
cnt=0
while curStop<len(stops)-1:
    finishStop=curStop
    if stops[curStop]+segment>=distance: # 만약에 현재 정거장에서 세그먼트 더한 거리가 목적지까지의
        print(cnt)                      #거리보다 크면 정거장에서 정거한 횟수를 출력
        quit()
    while curStop<len(stops)-1 and stops[curStop+1]-stops[finishStop]<=segment: # 해당 간격이 안 넘어서는 선에서 반복문 돌린다.
        curStop+=1
    if curStop==finishStop or (curStop==len(stops)-1 and stops[curStop]+segment<distance): # 정거장 이동하지 않거나 마지막 정거장+세그먼트가 종착지까지 못가면
        print(-1)                                                                          # -1을 출력하고 종료
        quit()
    if curStop<len(stops): # 아직 종착역까지 거리가 남았다면 횟수 증가
        cnt+=1
print(cnt)
        

