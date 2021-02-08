import itertools
def solution(expression):
    answer=0
    giho=['+','-','*']
    cal=[]
    num=[]
    start=0
    for idx,c in enumerate(expression):
        if c in giho:
            cal.append(c)
            num.append(expression[start:idx])
            start=idx+1
    if start!=len(expression):
        num.append(expression[start:])
    num=list(map(int,num))
    for turn in itertools.permutations(giho,3):
        calx=cal[:]
        numx=num[:]
        while len(numx)>1:
            for order in turn:
                while True:
                    try:
                        if len(numx)>=2:
                            idxx=calx.index(order)
                            if order=='+':
                                numx[idxx]+=numx[idxx+1]
                            elif order=='-':
                                numx[idxx]-=numx[idxx+1]
                            elif order=='*':
                                numx[idxx]*=numx[idxx+1]
                            calx.remove(order)
                            del numx[idxx+1]
                        else:
                            break
                    except:
                        break
            answer=max(answer,abs(numx[0]))
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
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)
