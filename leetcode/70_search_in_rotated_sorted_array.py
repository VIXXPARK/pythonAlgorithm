class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)<=2:
            for i in range(len(nums)):
                if nums[i]==target:
                    return i
            return -1
        start=0;end=len(nums)-1
        pivot=-1
        while start<=end and nums[start]>nums[end]: ## 분기점 찾기
            mid=(start+end)//2
            if nums[mid-1]>nums[mid+1]:
                if nums[mid-1]<nums[mid]:
                    pivot=mid
                    break
                else:
                    pivot=mid-1
                    break
            else:
                if nums[start]>nums[mid]:
                    end=mid-1
                else:
                    start=mid
        def binary_search(arr:list,target:int)->int: ## 이분탐색
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
        if pivot==-1: ## 분기점 없으면
            return binary_search(nums,target)
        if nums[0]<=target<=nums[pivot]: ## 첫 번째 분기에 있으면
            x=binary_search(nums[:pivot+1],target)
            return x if x!=-1 else -1
        elif nums[pivot+1]<=target<=nums[len(nums)-1]: ## 두 번째 분기에 있으면
            x=binary_search(nums[pivot+1:],target)
            return x+pivot+1 if x!=-1 else -1
        else:
            return -1

####################################################################################

class Solution:
    # @param {integer[]} numss
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1