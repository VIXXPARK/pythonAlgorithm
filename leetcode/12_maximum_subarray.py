class Solution:
    def maxSubArray(self, nums: list) -> int:
        x=[]
        for i,num in enumerate(nums):
            if i==0:
                x.append(num)
            else:
                if x[-1]+num>num:
                    x.append(x[-1]+num)
                else:
                    x.append(num)
        return max(x)
            