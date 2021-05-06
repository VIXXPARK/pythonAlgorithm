class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        import bisect
        left=bisect.bisect_left(nums,target,0,len(nums))
        right=bisect.bisect_right(nums,target,0,len(nums))
        if left==right:
            return [-1,-1]
        else:
            return [left,right-1]

#########################################################################
class Solution:
    def searchRange(self, nums, target: int):
        def upperbound(arr:list,target:int,begin=0,end=None): 
            if end is None:
                end=len(arr)
            while begin<end:
                mid=(begin+end)//2
                if arr[mid]<=target: 
                    begin=mid+1
                else:
                    end=mid
            return begin

        def lowerbound(arr,value,begin=0,end=None):
            if end is None:
                end=len(arr)
            while begin<end:
                mid=(begin+end)//2
                if arr[mid]<value:
                    begin=mid+1
                else:
                    end=mid
            return begin
        
        left,right=lowerbound(nums,target),upperbound(nums,target)
        return [left,right-1] if left!=right else [-1,-1]