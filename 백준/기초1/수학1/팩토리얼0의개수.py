import sys
fact=[-1]*501
def factorial(num):
    if num==0:
        fact[0]=1
        return fact[0]
    elif num==1:
        fact[1]=1
        return 1
    if fact[num]!=-1:
        return fact[num]
    else:
        fact[num]=num*factorial(num-1)
        return fact[num]
val = int(sys.stdin.readline())
li = list(str(factorial(val)))
cnt=0
while(True):
    if(li[-1]=='0'):
        cnt+=1
        li.pop()
    else:
        break
print(cnt)
