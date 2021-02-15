import itertools
def solution(relation):
    answer = 0
    column=len(relation[0])
    row=len(relation)
    minimality=[]
    route = [k for k in range(column)]
    for val in range(1,column+1):
        for lst in map(list,itertools.combinations(route,val)):
            dic={}
            flag=True
            for mi in minimality:
                cnt=0
                for l in lst:
                    if l in mi:
                        cnt+=1
                if cnt==len(mi):
                    flag=False
                    break
            if flag:
                for rel in relation:
                    ans=''
                    x=[]
                    for l in lst:
                        x.append(rel[l])
                    ans=''.join(map(str,x))
                    dic[ans]=dic.get(ans,0)+1
                    if dic[ans]>1:
                        continue
                if len(dic)==row:
                    minimality.append(lst)
                    answer+=1
    return answer

##################################################################
def solution2(relation):
    answer_list = list()
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]	))