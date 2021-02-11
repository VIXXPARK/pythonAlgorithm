import random,time
def sort(lst:list,lo=0,hi=None):
    if hi is None:
        hi=len(lst)-1
    if hi<=lo:
        return
    lt=lo
    gt=hi
    v=lst[lo]
    i=lo
    while i<=gt:
        if lst[i]<v:
            lst[i],lst[lt]=lst[lt],lst[i]
            lt+=1
            i+=1
        elif lst[i]>v:
            lst[i],lst[gt]=lst[gt],lst[i]
            gt-=1
        else:
            i+=1
    sort(lst,lo,lt-1)
    sort(lst,gt+1,hi)

lst=[]
start=time.time()
for val in range(10):
    lst.append(random.randint(1,10))
sort(lst)
end=time.time()
print("time",end-start)
# print(lst)
