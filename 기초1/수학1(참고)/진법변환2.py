import sys
script=sys.stdin.readline().split()
N=int(script[0])
B=int(script[1])
stk=[]
def zari(x):
    if x//B==0:
        stk.append(x%B) 
        return 0
    else:
        stk.append(x%B) 
        x//=B
        return zari(x)
zari(N)
stk.reverse()
for x in stk:
    if x>=10:
       x=chr(ord('A')+x-10)
       print(x,end='')
    else:
        print(x,end='')
