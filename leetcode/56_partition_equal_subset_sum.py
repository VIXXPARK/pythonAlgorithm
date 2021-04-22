class Solution:
    def canPartition(self, nums) -> bool:
        target=sum(nums)
        if target%2:
            return False
        else:
            target=target//2
        
        dp=[[False]*(target+1) for _ in range(len(nums)+1)]
        
        dp[0][0]=True
        for i in range(1,len(nums)+1):
            for j in range(target+1):
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j-nums[i-1]] or dp[i-1][j] ## 이전 단계에서 현재 j값을 가져오거나 아니면 지금 단계의 무게를 뺀 이전 단계의 값을 가져오거나
                else:
                    dp[i][j]=dp[i-1][j]
        
        return dp[len(nums)][target]

#######################################################################3

def canPartition(nums):
	target, n = sum(nums), len(nums)
	if target & 1: return False
	target >>= 1
	dp = [True] + [False]*target
	for x in nums:
		dp = [dp[s] or (s >= x and dp[s-x]) for s in range(target+1)]
		if dp[target]: return True
	return False

print(canPartition([1,5,11,5]))