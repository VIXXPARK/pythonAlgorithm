N=int(input())
passing =[False]*(N+1)
li=[]
def func(celi):
    if celi==N:
        print(' '.join(li))
        return
    for i in range(1,N+1):
        if not passing[i]:
            passing[i]=True
            li.append(str(i))
            func(celi+1)
            passing[i]=False
            li.pop()
func(0)
        

