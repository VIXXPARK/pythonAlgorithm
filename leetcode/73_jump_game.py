from collections import deque
class Solution:
    def canJump(self, nums) -> bool:
        ans=False
        for idx,val in enumerate(reversed(nums)):
            if idx==0:
                pass
            else:
                if idx<=nums[-idx-1]:
                    ans=True
                    break
        if ans==False and len(nums)>1:
            return ans
        dp=[False]*len(nums)
        dp[0]=True
        ret=False
        q=deque()
        q.append(0)
        while q:
            cur=q.popleft()
            if cur+nums[cur]>=len(nums)-1:
                ret=True
                break
            for i in range(cur+nums[cur],cur,-1):
                if not dp[i] and nums[i]:
                    dp[i]=True
                    q.append(i)
        return dp[-1] or ret

##########################################################
def canJump(self, nums):
    m = 0
    for i, n in enumerate(nums):
        if i > m:
            return False
        m = max(m, i+n)
    return True

###############################################################
def canJump(self, nums):
    goal = len(nums) - 1
    for i in range(len(nums))[::-1]:
        if i + nums[i] >= goal:
            goal = i
    return not goal