import functools

def comparator(a,b): ## 당분간 매일 봐야겠다. 이해하기 힘들구만 .. 고독하구만 
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

print(solution([6,10,2]))

###########################################################################
def solution2(numbers): #나는 이 문제를 접근 할 때 마지막 숫자만 늘려서 접근했는데 그렇게 하면 같은 값이 나올 경우 처리가
    answer = ''         #힘들기 때문에 다음과 같이 3배수만 하면 된다.
    if sum(numbers)==0:
        return '0'
    numbers = list(map(str,numbers))
    numbers=sorted(numbers,key=lambda x: x*3,reverse=True)
    
    return ''.join(numbers)