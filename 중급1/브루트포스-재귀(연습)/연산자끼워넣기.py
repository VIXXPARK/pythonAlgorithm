def func(s,idx,plus,minus,mult,div):
    global minVal,maxVal
    if idx>=N:
        minVal = s if s<minVal else minVal
        maxVal = s if s>maxVal else maxVal
    else:
        if plus : func(s+M[idx],idx+1,plus-1,minus,mult,div)
        if minus : func(s-M[idx],idx+1,plus,minus-1,mult,div)
        if mult : func(s*M[idx],idx+1,plus,minus,mult-1,div)
        if div : func(int(s/M[idx]),idx+1,plus,minus,mult,div-1)

minVal=10e10
maxVal=-10e10
N=int(input())
M=list(map(int,input().split()))
sign=list(map(int,input().split()))

func(M[0],1,sign[0],sign[1],sign[2],sign[3])
print(maxVal)
print(minVal)