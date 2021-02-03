import collections
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic=collections.Counter(nums).most_common() ## most_common은 데이터의 개수가 많은 순으로 정렬된 배열을 리턴하는 매서드이다.
        return dic[0][0]