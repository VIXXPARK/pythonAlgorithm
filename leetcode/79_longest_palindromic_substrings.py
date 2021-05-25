class Solution:
    def __init__(self):
        self.ans=""
        self.size=0
        self.s=""
    def longestPalindrome(self, s: str) -> str:
        self.s=s
        self.checkSizeAndInsertAns(0,0)
        for start in range(len(s)):            
            left=start-1;right=start+1
            if left>=0 and right<len(s):
                if s[left]==s[right]:
                    self.checkSizeAndInsertAns(left,right)
                    self.goToLeftAndRight(left,right)
        for start in range(len(s)-1):
            partner=start+1
            if s[start]==s[partner]:
                self.checkSizeAndInsertAns(start,partner)
                self.goToLeftAndRight(start,partner)
        return self.ans
    
    def checkSizeAndInsertAns(self,left,right):
        if self.size<=right-left+1:
            self.ans=self.s[left:right+1];self.size=right-left+1
            
    def goToLeftAndRight(self,left,right):
        while left>=0 and right<len(self.s):
            left-=1;right+=1
            if left>=0 and right<len(self.s) and self.s[left]==self.s[right]:
                self.checkSizeAndInsertAns(left,right)
            else:
                break

#################################################
def longestPalindrome(self, s):
    res = ""
    for i in range(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res
 
# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def helper(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]