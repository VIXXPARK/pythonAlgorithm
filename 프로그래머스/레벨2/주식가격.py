def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] >prices[j]:
                break
            else:
                answer[i] +=1
    return answer
############################################
# 간단하게 생각하는 연습이 필요한 것 같다. 숫자 범위에 고려해서 처음에
# 생각한 방법을 제외하고 했는데 알고보니 처음 생각한 방법이 통과되는 코드일 줄은 ....
from collections import deque
def solution2(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft()

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)
    return answer
###############################################################################
def solution(prices):
    answer = [0] * len(prices)
    
    length=len(prices)
    stack=[]
    for i,v in enumerate(prices):
        while stack and prices[stack[-1]]>prices[i]:
            cur=stack.pop()
            answer[cur]=i-cur
        stack.append(i)
    for v in stack:
        answer[v]=length-v-1
    return answer
