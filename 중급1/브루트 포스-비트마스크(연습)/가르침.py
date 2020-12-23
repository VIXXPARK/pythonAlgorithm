import sys
input=sys.stdin.readline
N,K=map(int,input().split())
alpha=[False]*26
alpha[0],alpha[2],alpha[13],alpha[19],alpha[8]=True,True,True,True,True
ceil=5
word=[]


if K<ceil:
    print(0)
elif K==26:
    print(N)
else:
    K-=5
    for _ in range(N):
        val=input().strip()
        word.append(val[3:len(val)-4])
    ans=0
