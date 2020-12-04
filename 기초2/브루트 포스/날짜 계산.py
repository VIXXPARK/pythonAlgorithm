import sys
E,S,M= map(int,sys.stdin.readline().split())
a,b,c=1,1,1
count=1
while True:
    if E==a and S==b and M==c:
        print(count)
        break

    if (a+1)%15!=0:
        a=(a+1)%15 
    else: a=15

    if (b+1)%28!=0:
        b=(b+1)%28
    else: b=28

    if (c+1)%19!=0:
        c=(c+1)%19
    else: c=19
    count+=1