class Solution:
    def rotate(self, nums, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        parent = len(nums)
        if k % parent != 0:
            k=k%parent
            left = nums[:parent-k]
            right = nums[parent-k:]
            for i in range(len(right)):
                nums[i] = right[i]
            for i in range(len(left)):
                nums[len(right)+i] = left[i]
##########################################################################
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start 
            prev = nums[start] #store the value in the position
            
            while True:
                next = (current + k) % len(nums) #
                nums[next],prev=prev,nums[next]
                current = next #reset current
                count += 1

                if start == current:
                    break 
            
            start += 1
########################################################
class Solution:
    def rotate(self, nums, k) -> None:
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0, k-1)
        self.reverse(nums,k, len(nums)-1)

    def reverse(self, nums, start, end) -> None:
        """
        :type nums: List[int]
        :type start: int
        :type end: int
        :rtype: None
        """
        while start < end: #
            nums[start],nums[end]=nums[end],nums[start]
            start += 1
            end -= 1