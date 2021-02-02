import itertools
def solution(orders, course):
    answer = []
    for c in course:
        dic={}
        tmp=[]
        Max=0
        for ords in orders:
            ords=list(ords)
            ords.sort()
            for val in itertools.combinations(ords,c):
                dic[val]=dic.get(val,0)+1
                Max=max(Max,dic[val])
        for k,v in dic.items():
            if v==Max and v!=1:
                k=''.join(k)
                tmp.append(k)  
        answer+=tmp
    answer.sort()
    return answer

##########################################################
import collections
import itertools

def solution2(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common() ## most_common은 데이터의 개수가 많은 순으로 정렬된 배열을 리턴하는 매서드이다.
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]