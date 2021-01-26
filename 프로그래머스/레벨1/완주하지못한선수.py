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
def solution3(participant, completion):
    participant.sort()
    completion.sort()
    for p, c in zip(participant, completion):
        if p != c:
            return p
    return participant[-1]
print(solution3(p,c))

