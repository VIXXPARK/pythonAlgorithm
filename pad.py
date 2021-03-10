def solution(prices):
    answer = [0] * len(prices)
    stack=[]
    for i,v in enumerate(prices):
        while stack and prices[stack[-1]]>prices[i]:
            cur=stack.pop()
            answer[cur]=i-cur
        stack.append(i)
    print(stack)    
    return answer

solution([1,2,3,2,3])

