import itertools
class Solution:
    def generateParenthesis(self, n: int) :
        temp=[')' for _ in range(n*2)]
        stk=[i for i in range(n*2)]
        ans={}
        def isParentheses(stk):
            check=[]
            for val in stk:
                if val=='(':
                    check.append(val)
                elif val==')' and not check:
                    return False
                else:
                    check.pop()
            return not check
        
        for lst in itertools.combinations(stk,n):
            stack=temp[:]
            for k in lst:
                stack[k]='('
            if not ans.get(''.join(stack),0):
                if isParentheses(stack):
                    s=''.join(stack)
                    ans[s]=ans.get(s,1)
        
        return sorted(ans,key=lambda x: x[0])

#################################################################
class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def backtrack(s, left, right):
            if left + right == 2 * n:
                ans.append(s)
            else:
                if left < n:
                    backtrack(s + '(', left + 1, right)
                if left > right:
                    backtrack(s + ')', left, right + 1)
        
        backtrack("", 0, 0)
            
        return ans