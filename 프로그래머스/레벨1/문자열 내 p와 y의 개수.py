def solution(s):
    s=s.upper()
    pNum,yNum=0,0
    for i in range(len(s)):
        if s[i]=='P': pNum+=1
        elif s[i]=='Y': yNum+=1
    if pNum==yNum: return True
    else: return False

## clean code ##
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')