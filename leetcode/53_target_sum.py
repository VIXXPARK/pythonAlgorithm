# 자바 코드로 냈을 때는 통과지만 파이썬은 실패라고 뜸 ㅠㅠ
class Solution:
    def __init__(self):
        self.ans=0
    def findTargetSumWays(self, nums, target: int) -> int:
        def nNm(cur,total):
            if cur==len(nums):
                if total==target:
                    self.ans+=1
                    return
            else:
                nNm(cur+1,total+nums[cur])
                nNm(cur+1,total-nums[cur])
        nNm(0,0)
        return self.ans

#########################################################################
class Solution2(object):
    def findTargetSumWays(self, nums, S):
        
        def subset_sum_count(nums, n, w):
            dp = [[0] * (w+1) for _ in range(n+1)]
            
            dp[0][0] = 1
            
            for i in range(1, n+1):
                for j in range(0, w+1):
                    if nums[i-1] <= j:
                        dp[i][j] = dp[i-1][j-nums[i-1]] + dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
            return dp
        
        total = sum(nums)
        if S > total:
            return 0
        if (S + total) % 2 != 0:
            return 0
        
        w = (S + total) // 2
        n = len(nums)
        dp = subset_sum_count(nums, n, w)
        return dp[n][w]

s=Solution2()
print(s.findTargetSumWays([1,1,1,1,1],3))

###############################################################################

class Solution(object):
    def findTargetSumWays(self, nums, S):
        total = sum(nums)
        if S > total:
            return 0
        if (S + total) % 2 != 0:
            return 0
        
        w = (S + total) // 2
        n = len(nums)
        dp = [0]*(w+1)
        dp[0]=1
        for val in nums:
            dp=[dp[s]+dp[s-val] if val<=s else dp[s] for s in range(w+1)]
        return dp[w]