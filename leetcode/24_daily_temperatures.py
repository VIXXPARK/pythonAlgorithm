class Solution:
    def dailyTemperatures(self, T):
        answer=[]
        k=max(T)
        cur=0
        memory=[0 for _ in range(101)]
        while cur<len(T):
            if T[cur]==k:
                answer.append(0)
                cur+=1
            else:
                if memory[T[cur]]>cur:
                    answer.append(memory[T[cur]]-cur)
                else:
                    for i in range(cur+1,len(T)):
                        if T[i]>T[cur]:
                            answer.append(i-cur)
                            memory[T[cur]]=i
                            break
                    else:
                        answer.append(0)
                cur+=1
        return answer

#################################################################
def dailyTemperatures(T):
    ans = [0] * len(T)
    stack = []
    for i, t in enumerate(T):
        while stack and T[stack[-1]] < t:
            cur = stack.pop()
            ans[cur] = i - cur
        stack.append(i)
    return ans

print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))