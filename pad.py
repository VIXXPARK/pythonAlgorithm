from collections import defaultdict,deque
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        item=defaultdict(int)
        q=deque()
        ans=0;total=0
        for val in s:
            if item[val]!=0:
                while q:
                    x=q.popleft()
                    item[x]-=1;total-=1
                    if x==val:
                        total+=1;item[val]+=1;q.append(val)
                        break     
            else:
                q.append(val)
                total+=1;item[val]=1
                ans=max(ans,total)
        return ans
                
                
s=Solution()
print(s.lengthOfLongestSubstring("bbtablud"))