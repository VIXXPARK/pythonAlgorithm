class Solution:
    def jump(self, nums: List[int]) -> int:
        dp=[0]*len(nums)
        dp[0]=1
        for i in range(len(nums)):
            for j in range(i+1,i+nums[i]+1):
                if j<len(nums):
                    if dp[j]==0:
                        dp[j]=dp[i]+1
                    else:
                        dp[j]=min(dp[j],dp[i]+1)
        return dp[len(nums)-1]-1

#################################################
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        n, start, end, step = len(nums), 0, 0, 0
        while end < n - 1:
            step += 1
            maxend = end + 1
            for i in range(start, end + 1):
                if i + nums[i] >= n - 1:
                    return step
                maxend = max(maxend, i + nums[i])
            start, end = end + 1, maxend
        return step