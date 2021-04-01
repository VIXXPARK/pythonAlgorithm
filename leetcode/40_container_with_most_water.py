class Solution:
    def maxArea(self, height: List[int]) -> int:
        dic={}
        for idx,h in enumerate(height):
            if dic.get(h,0)==0:
                dic[h]=[idx]
            else:
                dic[h].append(idx)
        dic=sorted(dic.items(),key=lambda x: -x[0])
        ans=[]
        for val in dic:
            ans.append(list(val[:]))
        answer=0
        fin=len(dic)
        for idx,order in enumerate(ans):
            if len(order[1])>=2:
                order[1].sort()
                answer=max(answer,(order[1][-1]-order[1][0])*order[0])
                if idx<fin-1:
                    ans[idx+1][1]+=[order[1][-1],order[1][0]]
            else:
                if idx<fin-1:
                    ans[idx+1][1]+=order[1][:]
        return answer
        
        
##################################################################################

class Solution2:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        
        max_area = min(height[i], height[j]) * (j-i)
        while i < j:
            if height[i] < height[j]:
                i += 1
            else: 
                j -= 1

            max_area = max(max_area, min(height[i], height[j]) * (j-i))
            
        
        return max_area