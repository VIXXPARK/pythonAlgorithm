import bisect
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.count=0
        self.storage=[]

    def addNum(self, num: int) -> None:
        loc=bisect.bisect_left(self.storage,num,0,len(self.storage))
        self.storage.insert(loc,num)
        self.count+=1

    def findMedian(self) -> float:
        if self.count%2==0:
            return (self.storage[self.count//2]+self.storage[self.count//2-1])/2
        else:
            return self.storage[self.count//2]

##################################################################################

from heapq import *


class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])