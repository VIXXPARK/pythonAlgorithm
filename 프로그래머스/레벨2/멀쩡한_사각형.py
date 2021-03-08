import math
def solution(w,h):
    answer = 0
    g=math.gcd(w,h)
    mult=h/w
    width=w//g
    height=h//g
    for i in range(1,width+1):
        if i==1:
            answer+=math.ceil(mult)
        else:
            go=math.floor(mult*(i-1))
            to=math.ceil(mult*(i))
            answer+=(to-go)
    return w*h-answer*g # 11testCASE 한 개 막힘 ㅜㅜ

#################################
import math
def solution2(w,h):
    return w*h-(w+h-math.gcd(w,h))
# 문제의 원리는 우선 대각선의 갯수는 가로 길이+ 세로길이 에서 두 대각선의 최대공약수의 갯수만큼만 빼면 된다.