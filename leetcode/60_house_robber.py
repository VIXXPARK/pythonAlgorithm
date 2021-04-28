class Solution:
    def rob(self, nums: List[int]) -> int:
        nums=[0]+nums[:]
        for i in range(1,len(nums)):
            if i<=2:
                continue
            else:
                nums[i]+=max(nums[i-2],nums[i-3])
        return max(nums[-1],nums[-2])