def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length
    total=0
    while q:
        time += 1
        total-=q.pop(0)
        if truck_weights:
            if total + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
                total+=q[-1]
            else:
                q.append(0)
    return time