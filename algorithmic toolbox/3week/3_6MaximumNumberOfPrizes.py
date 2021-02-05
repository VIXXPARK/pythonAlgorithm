n=int(input())
def increSum(n):
    return (n*(n+1))//2
x=int(n**0.5)
while True:
    N=increSum(x)
    if x<n-N:
        x+=1
    else:
        if n-N<=x:
            lst=[i for i in range(1,x)]+[n-increSum(x-1)]
        else:
            lst=[i for i in range(1,x+1)]+[n-N]
        print(len(lst))
        print(' '.join(map(str,lst)))    
        quit()


