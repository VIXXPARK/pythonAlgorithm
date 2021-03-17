class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        d=defaultdict(list)
        for si in strs:
            d[str(sorted(si))].append(si)
        print(type(sorted(strs[0])))
        print(type(strs[0]))
        li=[]
        for i in d.keys():
            li.append(d[i])
        return li