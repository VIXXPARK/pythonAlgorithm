class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minusVal=0
        last=nums[0] #이전 단계
        ans=last 
        minusVal=nums[0] if nums[0]<0 else 0 # 음수값중 최솟값
        for i in range(1,len(nums)):
            now=last*nums[i] if last!=0 else nums[i] # 현재 값
            if now<0: ## 음수일때
                if minusVal==0: ## 초기 세팅이 0일 때
                    minusVal=now # 초기화 
                    last=now # 앞으로 전진
                else:
                    ans=max(ans,now//minusVal) # 이전 값에 음수가 있을 때
                    minusVal=max(minusVal,now)
                    last=now
            else: # 양수일 때
                if nums[i]==0: ## 만일 0이라면
                    minusVal=0
                ans=max(now,ans)
                last=now
        return ans
##########################################################################################
def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        current = 1
		# left to right pass. Captures all potential subarrays containing first odd n negative numbers
        for i in nums: 
            current*=i
            ans = max(ans, current)
			# zero is a delimiter, restart at 1. This is optimal since zero multiplied on is still zero.
            if current == 0:
                current = 1
        current = 1
		# right to left pass capturing all potential subarrays containing last odd n negative numbers
        for i in reversed(nums):
            current*=i
            ans = max(ans, current)
            if current == 0:
                current = 1
        return ans