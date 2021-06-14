class Solution:
    def firstMissingPositive(self, nums) -> int:
        maxNum=max(nums)
        nums=list(set(nums))
        nums.sort()
        length=len(nums)
        start=0
        while True:
            if start==length or nums[start]>0 :
                break
            start+=1
        num=1
        while True:
            if start==length:
                break
            if num==nums[start]:
                num+=1
                start+=1
            else:
                return num
        return maxNum+1 if maxNum>0 else 1
####################################################
def firstMissingPositive(self, nums):
    for i in range(len(nums)):
        while 0 <= nums[i]-1 < len(nums) and nums[nums[i]-1] != nums[i]:
            tmp = nums[i]-1
            nums[i], nums[tmp] = nums[tmp], nums[i]
    for i in range(len(nums)):
        if nums[i] != i+1:
            return i+1
    return len(nums)+1