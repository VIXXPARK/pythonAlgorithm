class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        answer=[]
        k=max(T)
        cur=0
        memory=[0 for _ in range(101)]
        while cur<len(T):
            if T[cur]==k:
                cur+=1
            else:
                if memory[T[cur]]>cur:
                    answer.append(memory[T[cur]]-cur)
                    break
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

s=Solution()
print(s.dailyTemperatures([89,62,70,58,47,47,46,76,100,70]))