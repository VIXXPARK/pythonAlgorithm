import collections
class Solution:
    def singleNumber(self, nums: list) -> int:
        dic=collections.Counter(nums)
        for k,v in dic.items():
            if v==1:
                return k