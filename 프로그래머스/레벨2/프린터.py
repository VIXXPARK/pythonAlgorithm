def solution(priorities, location):
    answer = 0
    dic = {(i):v for i,v in enumerate(priorities)}
    lv=[0 for _ in range(10)]
    for i in priorities:
        lv[i]+=1
    queue=[ i  for i in range(len(priorities))]
    count=1
    while True:
        x=queue.pop(0)
        flag=True
        for i in range(dic[x]+1,10):
            if lv[i]!=0:
                queue.append(x)
                flag=False
                break
        if flag:
            if location==x:
                return count
            count+=1
            lv[dic[x]]-=1

################################################################

def solution2(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
