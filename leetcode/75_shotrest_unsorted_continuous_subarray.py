class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sorted=sorted(nums)
        start=0;end=len(nums)-1
        startFlag=True;endFlag=True
        while start<end:
            if not startFlag and not endFlag:
                break
            if startFlag:
                if nums[start]==nums_sorted[start]:
                    start+=1
                else:
                    startFlag=False
            if endFlag:
                if nums[end]==nums_sorted[end]:
                    end-=1
                else:
                    endFlag=False
        return end-start+1 if end!=start else 0