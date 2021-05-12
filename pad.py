class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums)<=2:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
            return -1
        start=0;end=len(nums)-1
        pivot=-1
        while start<=end and nums[start]>nums[end]:
            mid=(start+end)//2
            if nums[mid-1]>nums[mid+1]:
                if nums[mid-1]<nums[mid]:
                    pivot=mid
                    break
                else:
                    pivot=mid-1
                    break
            else:
                end=mid-1
        def binary_search(arr:list,target:int)->int:
            lo,hi=0,len(arr)-1
            while lo<=hi:
                mid=(lo+hi)//2
                if arr[mid]<target:
                    lo=mid+1
                elif arr[mid]>target:
                    hi=mid-1
                else:
                    return mid
            return -1
        if pivot==-1:
            return binary_search(nums,target)
        if nums[start]<=target<=nums[pivot]:
            x=binary_search(nums[:pivot+1],target)
            return x if x!=-1 else -1
        elif nums[pivot+1]<=target<=nums[len(nums)-1]:
            x=binary_search(nums[pivot+1:],target)
            return x+pivot+1 if x!=-1 else -1
        else:
            return -1

s=Solution()
print(s.search([6,7,1,2,3,4,5],))