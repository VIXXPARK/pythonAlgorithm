class Solution:
    def nextPermutation(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)==1:
            pass
        else:
            maxNum=max(nums)
            idx=len(nums)-1
            turn=nums[idx]>nums[idx-1]
            while idx>=0:
                if idx==0 or turn != (nums[idx]>nums[idx-1]):
                    break
                idx-=1
            if nums[idx]==maxNum: ##분기점이 최대값일 때
                val=nums[idx] ## 분기 이후에서 idx-1에 위치한 값보다 큰 최소값 찾기
                for i in range(idx+1,len(nums)):
                    if nums[idx-1]<nums[i]:
                        val=min(val,nums[i])
                index=nums[idx:].index(val)+idx ## val의 인덱스 값

                if idx==0 and nums[idx]==maxNum: ## 만약에 마지막까지 돌았다면 
                    for i,val in enumerate(sorted(nums)):## 처음상태로
                        nums[i]=val

                elif val>nums[idx-1]:
                    nums[index],nums[idx-1]=nums[idx-1],nums[index]
                    temp=sorted(nums[idx:])
                    for i in range(idx,len(nums)):
                        nums[i]=temp[i-idx]
            else:
                if turn == False: ## 분기 이후에서 마지막 순번까지 돌았다면
                    val=nums[idx]
                    for i in range(idx+1,len(nums)):
                        if nums[idx-1]<nums[i]:
                            val=min(val,nums[i])
                    index=nums[idx:].index(val)+idx
                    nums[idx-1],nums[index]=nums[index],nums[idx-1]
                    for i,val in enumerate(sorted(nums[idx:])):
                        nums[i+idx]=val
                else:## 아직 돌아야할 순열이 있다면
                    nums[-1],nums[-2]=nums[-2],nums[-1]   

#################################################################################

def nextPermutation(self, nums):
    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1
    if i == 0:   # nums are in descending order
        nums.reverse()
        return 
    k = i - 1    # find the last "ascending" position
    while nums[j] <= nums[k]:
        j -= 1
    nums[k], nums[j] = nums[j], nums[k]  
    l, r = k+1, len(nums)-1  # reverse the second part
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l +=1 ; r -= 1