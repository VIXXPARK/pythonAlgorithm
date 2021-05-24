from collections import defaultdict,deque
class Solution: # 내 풀이
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
                total+=1;item[val]=1;q.append(val)
                ans=max(ans,total)
        return ans

##########################################################
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        left=0
        output=0
        for right in range(len(s)):

            if s[right] not in seen:
                output = max(output,right-left+1)

            else:
                if seen[s[right]]<left:
                    output=max(output,right-left+1)
                else:
                    left=seen[s[right]]+1
            seen[s[right]]=right
        return output

'''
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
          ^                  ^
          |                  |
		left               right
		seen = {a : 0, c : 1, b : 2, d: 3} 
		# case 1: seen[b] = 2, current window  is s[0:4] , 
		#        b is inside current window, seen[b] = 2 > left = 0. Move left pointer to seen[b] + 1 = 3
		seen = {a : 0, c : 1, b : 4, d: 3} 
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
						 ^   ^
					     |   |
				      left  right		
indext    0    1    2    3   4   5   6   7
string    a    c    b    d   b   a   c   d
					     ^       ^
					     |       |
				       left    right		
		# case 2: seen[a] = 0,which means a not in current window s[3:5] , since seen[a] = 0 < left = 3 
		# we can keep moving right pointer.
'''