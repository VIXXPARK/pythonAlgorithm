def solution1(N, stages):
    answer = []
    dic={}
    total=len(stages)
    for val in stages: 
        dic[val]=dic.get(val,0)+1 ## 만일 stages에 값이 없다면 1로 그렇지 않다면 1증가
    for i in range(1,N+1):
        dic[i]=dic.get(i,0) # 존재한다면 그대로 그렇지 않다면 0으로 초기화
        tmp=dic[i] # 사전에 값을 저장
        if total!=0: # 런타임에러를 방지하기 위해 조건문 작성
            dic[i]=dic[i]/total
        else:
            dic[i]=0
        total-=tmp 
    for k,v in dic.items(): # key, value를 reverse해서 저장
        if k!=N+1:
            answer.append((v,k))
    answer.sort(reverse=True) ## 내림차순으로 정렬
    fin=[]
    x=0
    while x<=len(answer)-1:
        k=x+1
        for y in range(x+1,len(answer)): # 값은값이 끝날때까지 반복문 
            if answer[x][0]!=answer[y][0]:
                break
            else:
                k+=1
        lst=[]
        for tmp in range(x,k): # 값은 값을 가진 값들을 임시로 저장
            lst.append(answer[tmp][1])
        lst.sort() ## 오름차순으로 정렬 
        fin+=lst
        x=k
    return fin

def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage) #해당 갯수 카운트
            result[stage] = count / denominator # 확률 계산
            denominator -= count # 이미 진행된 스테이지 감소
        else:
            result[stage] = 0 # 진행되지 않는 스테이지는 0으로 초기화
    return sorted(result, key=lambda x : result[x], reverse=True) # sorted에 result를 그냥 넘기면 result의 keys가 들어감
                                                                  # lambda는 기준을 result[x](=value)로 정렬 reverse는 오름차순