def chan(n):
    ans=[]
    while n:
        ans.append(n%3)
        n//=3
    return ans[::-1]
def solution(n):
    answer = ''
    x=chan(n)
    lst=[]
    for i in range(len(x)):
        if x[i]==0:
            lst.append(i)
    while lst:
        val=lst.pop(0)

        if x[val-1]==4:
            x[val-1]=2
            x[val]=4
        elif x[val-1]==2:
            x[val-1]=1
            x[val]=4
        elif x[val-1]==1:
            x[val-1]=0
            x[val]=4
            if val-1>0:
                lst.insert(0,val-1)
    if x[0]==0:
        x.pop(0)
    x=list(map(str,x))
    return ''.join(x)

##########################################
def change124(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer
