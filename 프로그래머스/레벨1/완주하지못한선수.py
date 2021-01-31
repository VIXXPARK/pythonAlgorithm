p=["leo", "kiki", "eden"]
c = ["kiki", "eden"]
def solution1(p, c):
    dic={}
    answer=None
    for val in p:
        try:
            dic[val]+=1
        except:
            dic[val]=1
    for check in c:
        dic[check]-=1
    for k,v in dic.items():
        if v!=0:
            answer=k
            break
    return answer
#####################################################################################
import collections
def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
#####################################################################################
def sol3(participant, completion):
    answer = ''
    parti={}
    for x in participant:
        parti[x]=parti.get(x,0)+1
    for x in completion:
        parti[x]-=1
    for k,v in parti.items():
        if v==1:
            answer+=k
    return answer

