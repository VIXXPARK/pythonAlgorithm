class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        
        prod = 1
        for i in range(len(nums)):
            res[i] = prod
            prod *= nums[i]
        
        prod = 1
        for i in reversed(range(len(nums))):
            res[i] *= prod
            prod *= nums[i]
            
        return res
######################################################################
class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer=1
        count=0
        ans=[]
        
        for val in nums:
            if val!=0:
                answer*=val
            else:
                count+=1
        
        for val in nums:
            if val !=0:
                if count==0:
                    ans.append(answer//val)
                else:
                    ans.append(0)
            else:
                if count-1==0:
                    ans.append(answer)
                else:
                    ans.append(0)
        return ans