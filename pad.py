import itertools
def solution(relation):
    answer = 0
    minimality=[]
    col=len(relation[0])
    row=len(relation)
    hubo=[i for i in range(col)]
    for i in range(1,col+1):
        for itr in itertools.combinations(hubo,i):
            itr=list(itr)
            flag=True
            for mini in minimality:
                cnt=0
                for mi in mini:
                    if mi in itr:
                        cnt+=1
                if len(mini)==cnt:
                    flag=False
                    break
            tmp={}
            if flag:
                for rel in relation:
                    ss=''
                    for idx in itr:
                        ss+=rel[idx]
                    tmp[ss]=tmp.get(ss,0)+1
                    if tmp[ss]>1:
                        break
                if len(tmp)==row:
                    minimality.append(itr)
                    answer+=1
                    
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))