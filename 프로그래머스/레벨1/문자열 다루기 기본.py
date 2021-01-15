def solution(s):
    if len(s)==4 or len(s)==6:
        for i in range(len(s)):
            if '0'<=s[i]<='9':
                continue
            else:
                return False
    else:
        return False
    return True

## best code ##
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
    

