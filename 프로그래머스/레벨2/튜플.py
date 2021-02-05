def solution(s):
    answer = [[] for _ in range(501)]
    check=[0 for _ in range(100001)]
    maxLen=0
    ans=[]
    s=s[1:-1]
    s=s.split('},')
    for val in s:
        if val[-1]!='}':
            val=val[1:].split(',')
            maxLen=max(maxLen,len(val))
            answer[len(val)].append(list(map(int,val)))
        else:
            val=val[1:-1].split(',')
            maxLen=max(maxLen,len(val))
            answer[len(val)].append(list(map(int,val)))
    for i in range(1,maxLen+1):
        val=answer[i][0]
        for x in (val):
            if check[x]==0:
                ans.append(x)
                check[x]=1    
    return ans
################################################################################################################
import re
from collections import Counter
def solution2(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)])) #숫자가 많은 순으로 

def solution5(s):
    s = Counter(re.findall('\d+', s)).most_common()
    return list(map(int, [k for k, v in s]))

################################################################################################################
def solution3(s):
    answer = []
    s1 = s.lstrip('{').rstrip('}').split('},{')
    new_s = []
    for i in s1:
        new_s.append(i.split(','))
    new_s.sort(key = len)
    for i in new_s:
        for j in range(len(i)):
            if int(i[j]) not in answer:
                answer.append(int(i[j]))
    return answer
#################################################################################################################
import collections
def solution4(s):
    answer = []
    s=s.lstrip('{').rstrip('}').split('},{')
    for val in s:
        val=val.split(',')
        for v in val:
            answer.append(int(v))
    s=collections.Counter(answer).most_common()
    return [k for k,v in s]

print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))