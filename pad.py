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
                            
print(solution("100-200*300-500+20"	))

