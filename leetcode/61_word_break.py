def wordBreak(self, s, words):
    ok = [True]
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in words for j in range(i)),
    return ok[-1]

    
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        dp = [False] * (len(s) + 1) # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
        dp[0] = True
        for i in range(len(s)):
            if dp[i]:
                for j in range(i, len(s)):
                    if s[i: j+1] in wordDict:
                            dp[j+1] = True
                    
        return dp[-1]

s = "catsandog";wordDict = ["cats","dog","sand","and","cat"]
ss=Solution()
print(ss.wordBreak(s,wordDict))
