import itertools
def solution(expression):
    answer = 0
    num=[]
    giho=[]
    start=0
    gh=['+','-','*']
    for idx,c in enumerate(expression):
        if c in gh:
            giho.append(c)
            num.append(int(expression[start:idx]))
            start=idx+1
    num.append(int(expression[start:]))
    for ords in itertools.permutations(gh,3):
        copyNum,copyGiho=num[:],giho[:]
        while len(copyNum)>1:
            for g in ords:
                while True:
                    try:
                        idxx=copyGiho.index(g)
                        if g=='+':copyNum[idxx]+=copyNum[idxx+1]
                        elif g=='-':copyNum[idxx]-=copyNum[idxx+1]
                        elif g=='*':copyNum[idxx]*=copyNum[idxx+1]
                        del copyNum[idxx+1]
                        copyGiho.remove(g)
                    except:
                        break
        answer=max(answer,abs(copyNum[0]))
    return answer
print(solution("100-200*300-500+20"	))