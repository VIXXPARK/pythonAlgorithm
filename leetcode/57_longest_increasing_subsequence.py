class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect
        stk=[]
        for i in range(len(nums)):
            if not stk or stk[-1]<nums[i]:
                stk.append(nums[i])
            else:
                loc=bisect.bisect_left(stk,nums[i],0,len(stk))
                stk[loc]=nums[i]
        
        return len(stk)