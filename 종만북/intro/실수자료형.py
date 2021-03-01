# 절대 오차와 상대오차를 모두 이용해서 두 수가 같은지 판정한다.
def doubleEqual(a,b):
    diff = abs(a-b)
    #절대 오차가 허용 범위 안일 경우 무조건 True를 반환한다.
    if diff<1e-10: return True
    #이 외의 경우에는 상대 오차를 사용한다.
    return diff<=1e-8*max(abs(a),abs(b))


cnt=0
for i in range(1,51):
    y=1/i
    if doubleEqual(1,y*i): # 이와 같이 표기한 이유는
        cnt+=1          # y를 구하는 과정에서 실수로 변하며 값이 바뀐 것을 고려하여
print(cnt)              #오차 범위를 1/10^-10 로 하면 이 이상 차이는 안나기 때문에..