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


s = Solution()
s.rotate([1,2,3,4,5,6,7],3)
