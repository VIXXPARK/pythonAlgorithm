import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small=[]
        large=[]
        nums1.reverse()
        nums2.reverse()
        while nums1 and nums2:
            if len(small)==len(large):
                self.sameLengthSmallAndLarge(nums1,nums2,small,large)
            else:
                self.differenceLengthSmallAndLarge(nums1,nums2,small,large)
        while nums1:
            self.heapPushSmallAndLarge(nums1,small,large)
        while nums2:
            self.heapPushSmallAndLarge(nums2,small,large)
        if len(small)==len(large):
            return (large[0]-small[0])/2
        else:
            return large[0]
        
    def sameLengthSmallAndLarge(self,nums1,nums2,small,large):
        if nums1[-1]>nums2[-1]:
            heapq.heappush(large,-heapq.heappushpop(small,-nums2.pop()))
        else:
            heapq.heappush(large,-heapq.heappushpop(small,-nums1.pop()))
            
    def differenceLengthSmallAndLarge(self,nums1,nums2,small,large):
        if nums1[-1]>nums2[-1]:
            heapq.heappush(small,-heapq.heappushpop(large,nums2.pop()))
        else:
            heapq.heappush(small,-heapq.heappushpop(large,nums1.pop()))
    def heapPushSmallAndLarge(self,lst,small,large):
        if len(small)==len(large):
            heapq.heappush(large,-heapq.heappushpop(small,-lst.pop()))
        else:
            heapq.heappush(small,-heapq.heappushpop(large,lst.pop()))

#########################################################################
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        new=nums1[:]+nums2[:]
        new.sort()
        length=len(new)
        return new[length//2] if length%2 else (new[length//2-1]+new[length//2])/2
#########################################################################
def findMedianSortedArrays(nums1, nums2):
    a, b = sorted((nums1, nums2), key=len)
    m, n = len(a), len(b)
    after = (m + n - 1) // 2
    lo, hi = 0, m
    while lo < hi:
        mid = (lo + hi) // 2
        if after-mid-1 < 0 or a[mid] >= b[after-mid-1]:
            hi = mid
        else:
            lo = mid + 1
    i = lo
    nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
    return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0