def solution(bridge_length, weight, truck_weights):
    length=len(truck_weights)
    lst=[0]*length
    cur=0
    end=cur
    total=0
    time=0
    while cur<=length:
        if lst[cur]==bridge_length+1:
            cur+=1
            if cur<length:
                lst[cur]+=1
                total-=truck_weights[cur-1]
            else:
                break

        if end<length and truck_weights[end]+total<=weight:
            end+=1
            total+=truck_weights[end-1]
        
        if lst[cur]!=bridge_length+1 and end<=length:
            for i in range(cur,end):
                    lst[i]+=1
            
        time+=1
        
    return time
            

print(solution(100,100,[10]))