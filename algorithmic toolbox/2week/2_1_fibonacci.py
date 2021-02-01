n=int(input())
lst=[]
lst.append(0)
if n>=1:
    lst.append(1)
    for i in range(2,n+1):
        lst.append(lst[i-1]+lst[i-2])
    print(lst[n])
else:
    print(0)