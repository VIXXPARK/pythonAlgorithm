def moveZeroes(nums:list) -> None:
    write = 0
    count = 0
    for read in range(0,len(nums)):
        if nums[read]!=0:
            nums[write] = nums[read]
            write+=1
        else:
            count+=1
    for i in range(count):
        nums[-1-i] = 0
print(moveZeroes([0,1,0,3,-1,0,12]))


class Solution:
    def moveZeroes(self, nums:list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero = non_zero + 1