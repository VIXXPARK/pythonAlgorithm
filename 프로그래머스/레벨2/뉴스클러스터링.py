def solution(str1, str2):
    answer = 0
    str1,str2=str1.lower(),str2.lower()
    dic1,dic2={},{}
    for i in range(0,len(str1)-1):
        val=str1[i:i+2]
        if val.isalpha():
            dic1[val]=dic1.get(val,0)+1
    for i in range(0,len(str2)-1):
        val=str2[i:i+2]
        if val.isalpha():
            dic2[val]=dic2.get(val,0)+1
    up,down=0,0
    dic3={}
    for k,v in dic1.items():
        if dic2.get(k,0):
            up+=min(dic1[k],dic2[k])
            dic3[k]=dic3.get(k,max(dic1[k],dic2[k]))
        else:
            dic3[k]=dic3.get(k,v)
    for k,v in dic2.items():
        if dic3.get(k,0):
            continue
        else:
            dic3[k]=dic3.get(k,v)
    for k,v in dic3.items():
        down+=v
    try:
        answer=int((up/down)*65536.0)
    except:
        answer=65536   
    return answer
#############################################################
import re
import math

def solution2(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)

###########################################################################################################################

from collections import Counter
def solution3(str1, str2):
    # make sets
    s1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    s2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    if not s1 and not s2:
        return 65536
    c1 = Counter(s1)
    c2 = Counter(s2)
    answer = int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536)
    return answer