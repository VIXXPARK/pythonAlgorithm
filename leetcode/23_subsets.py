# import itertools
# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         answer=[]
#         for num in range(len(nums)+1):
#             for i in itertools.combinations(nums,num):
#                 answer.append(list(i))
#         return answer
##################################################################
class Solution2(object):
    def subsets(self, nums):
        nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result

s=Solution2()
print(s.subsets([1,2,3]))