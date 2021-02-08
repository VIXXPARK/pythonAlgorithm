import itertools
def solution(expression):
    answer = 0
    start=0
    num,cal=[],[]
    for idx,c in enumerate(expression):
        if c in ['+','-','*']:
            cal.append(c)
            num.append(int(expression[start:idx]))
            start=idx+1
    num.append(int(expression[start:]))
    for orders in itertools.permutations(['+','-','*'],3):
        copyNum=num[:]
        copyCal=cal[:]
        while len(copyNum)>1:
            for ods in orders:
                while True:
                    try:
                        idxx=copyCal.index(ods)
                        if ods=='+':
                            copyNum[idxx]=copyNum[idxx]+copyNum[idxx+1]
                        elif ods=='-':
                            copyNum[idxx]=copyNum[idxx]-copyNum[idxx+1]
                        elif ods=='*':
                            copyNum[idxx]=copyNum[idxx]*copyNum[idxx+1] 
                        del copyNum[idxx+1]
                        copyCal.remove(ods)  
                    except:
                        break
        answer=max(answer,abs(copyNum[0]))                    
    return answer
######################################################################
import re
from itertools import permutations

def solution2(expression):
    #1
    op = [x for x in ['*','+','-'] if x in expression]
    op = [list(y) for y in permutations(op)]
    ex = re.split(r'(\D)',expression)
    #2
    a = []
    for x in op:
        _ex = ex[:]
        for y in x:
            while y in _ex:
                tmp = _ex.index(y)
                _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
                _ex = _ex[:tmp]+_ex[tmp+2:]
        a.append(_ex[-1])
    #3
    return max(abs(int(x)) for x in a)

############################################################################
def solution3(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        print(a.join(temp_list))
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)
print(solution3("100-200*300-500+20"))