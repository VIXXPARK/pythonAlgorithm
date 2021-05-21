class Solution:
    def maxProduct(self, nums) -> int:
        minusVal=0
        dp=[0]*(len(nums))
        dp[0]=nums[0]
        ans=dp[0]
        minusVal=nums[0] if nums[0]<0 else 0
        for i in range(1,len(nums)):
            ans=max(ans,nums[i])
            dp[i]=dp[i-1]*nums[i] if dp[i-1]!=0 else nums[i]
            if dp[i]<0:
                if minusVal==0:
                    minusVal=dp[i]
                elif nums[i]==0:
                    minusVal=0
                    ans=max(ans,nums[i])
                else:
                    ans=max(ans,dp[i]//minusVal)
                    minusVal=max(minusVal,dp[i])
            else:
                ans=max(dp[i],ans)
        return ans
s=Solution()
print(s.maxProduct([-1,0,-2,2]))