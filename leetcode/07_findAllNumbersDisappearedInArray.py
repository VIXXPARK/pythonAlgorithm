import heapq
#Solution1 clear
class Solution:
    def findDisappearedNumbers(self, nums:list) -> list:
        result = set(range(1, len(nums)+1))
            
        return result-set(nums)

#Solution2
class Solution2:
    def findDisappearedNumbers(self, nums: list) -> list:
        n = len(nums)
        result = []
        if n == 0 or n == 1:
            return None
        
        heapq.heapify(nums) # heapq 모듈은 이진트리 기반의 최소 힙 자료구조
        pre = heapq.heappop(nums)
        if pre != 1:
            n= pre - 1
            for i in range(n):
                result.append(i+1)
        while nums:
            curr = heapq.heappop(nums)
            if curr == pre:
                continue
            elif curr - pre == 1:
                pre = curr
                continue
            elif curr - pre > 1:
                m = curr - pre -1
                for i in range(m):
                    result.append(pre+i+1)
                pre = curr
        if pre < n:
            m = n - pre
            for i in range(m):
                result.append(pre+i+1)
        return result
#Solution3  cyclic sort
class Solution3:
    def findDisappearedNumbers(self, nums: list) -> list:

        for number in nums:

            present_indx = abs(number)-1
            if nums[present_indx] > 0 :
                # use negative number to mark number is presented in array
                nums[present_indx] = -nums[present_indx]
            else:
                pass


        # the disappeared numbers are those grids which are still with positive value
        return [ i+1 for i, num in enumerate(nums) if num > 0 ]
    
s= Solution3()
s.findDisappearedNumbers([4,3,2,7,8,2,3,1])