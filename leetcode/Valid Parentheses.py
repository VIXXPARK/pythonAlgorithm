def isValid(self, s: str) -> bool:
    left=['(','{','[']
    stk=[]
    for val in s:
        if val in left: stk.append(val)
        else:
            if len(stk)==0:
                return False
            if stk[-1]=='(':
                if val!=')':return False
                else:stk.pop()
            elif stk[-1]=='{':
                if val!='}':return False
                else:stk.pop()
            elif stk[-1]=='[':
                if val!=']':return False
                else:stk.pop()
    if len(stk)!=0:return False
    else:return True

################################################
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []        
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            elif c == ')' and (not stack or stack.pop() != '('):
                return False
            elif c == ']' and (not stack or stack.pop() != '['):
                return False
            elif c == '}' and (not stack or stack.pop() != '{'):
                return False
            
        return not stack