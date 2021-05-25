class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans="";size=0
        for start in range(len(s)):
            if size<=1:
                ans=s[start]
                size=1
            left=start-1;right=start+1
            if left>=0 and right<len(s):
                if s[left]==s[right]:
                    flag=self.checkSizeAndInsertAns(s,left,right,ans,size)
                    (size,ans)=(flag[1],flag[2]) if flag[0] else (size,ans)
                    ans,size=self.goToLeftAndRight(s,left,right,ans,size)
        for start in range(len(s)-1):
            partner=start+1
            if s[start]==s[partner]:
                if size<=2:
                    size=2
                    ans=s[start:partner+1]
                left=start;right=partner
                ans,size=self.goToLeftAndRight(s,left,right,ans,size)
        return ans
    
    def checkSizeAndInsertAns(self,s,left,right,ans,size):
        if size<=right-left+1:
            ans=s[left:right+1]
            size=right-left+1
            return [True,size,ans]
        return [False]
    
    def goToLeftAndRight(self,s,left,right,ans,size):
        while left>=0 and right<len(s):
            left-=1;right+=1
            if s[left]==s[right]:
                if size<=right-left+1:
                    ans=s[left:right+1]
                    size=right-left+1
            else:
                break
        return [ans,size]

s=Solution()
print(s.longestPalindrome("bb"))