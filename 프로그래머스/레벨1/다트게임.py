lst=[]
val='1D2S#10S'
start=0
before=0
finish=len(val)
while start<=finish-1: ## 10때문에 이러한 과정ㅠㅠ. start,before,finish 숫자를 둬서 해당 위치까지 오면 끊고 집어놓고 하는 식
    if not val[start].isdigit():
        if start!=before:## start와 before이 같으면 바로 문자가 오는 경우이므로 넘어간다.
            lst.append((val[before:start]))
        lst.append(val[start])
        before=start+1
    start+=1
stk=[]
for i,v in enumerate(lst):
    if v.isdigit():
        stk.append(int(v))
    else:
        if v=='S':
            stk[-1]=int(stk[-1]**1)
        elif v=='D':
            stk[-1]=int(stk[-1]**2)
        elif v=='T':
            stk[-1]=int(stk[-1]**3)
        elif v=='*':
            stk[-1]=stk[-1]*2
            if len(stk)>1:
                stk[-2]=stk[-2]*2
        elif v=='#':
            stk[-1]=stk[-1]*-1
print(sum(stk))

####################################################

def solution(dartResult):
    point = []
    answer = []
    dartResult = dartResult.replace('10','k')## 하나의 숫자때문에 리스트화가 어렵다면 그 특정 숫자만 replace!!
    point = ['10' if i == 'k' else i for i in dartResult]
    print(point)

    i = -1
    sdt = ['S', 'D', 'T']
    for j in point:
        if j in sdt :
            answer[i] = answer[i] ** (sdt.index(j)+1)
        elif j == '*':
            answer[i] = answer[i] * 2
            if i != 0 :
                answer[i - 1] = answer[i - 1] * 2
        elif j == '#':
            answer[i] = answer[i] * (-1)
        else:
            answer.append(int(j))
            i += 1
    return sum(answer)