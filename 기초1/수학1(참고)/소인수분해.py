import sys
N = int(sys.stdin.readline().rstrip())
div = 2
while N!=1:
    if N%div==0:
        N=N//div
        print(div)
    else: div+=1