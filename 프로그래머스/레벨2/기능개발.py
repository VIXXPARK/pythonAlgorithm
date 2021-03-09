def solution(progresses, speeds):
    answer = []
    length=len(progresses)
    finish=[0 for _ in range(length)]
    cur=0
    while cur<length:
        count=0
        for i in range(cur,length):
            if finish[i]==0:
                progresses[i]+=speeds[i]
        for i in range(cur,length):
            if progresses[i]>=100 :
                if finish[i]==0:
                    finish[i]=1
        for i in range(cur,length):
             if i==cur and finish[cur]==1:
                for j in range(cur,length):
                    if finish[j]==1:
                        finish[j]=2
                        count+=1
                        cur+=1
                    else:
                        break
                if count>=1:
                    answer.append(count)
    return answer

###########################################
def solution2(progresses, speeds): ## deque를 이용하면 시간 개선 가능!
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer