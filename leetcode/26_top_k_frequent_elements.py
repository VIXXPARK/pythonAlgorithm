import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=collections.Counter(nums).most_common()
        ans=[]
        for idx,val in enumerate(dic):
            if idx<k:
                ans.append(val[0])
            else:
                break
        return ans