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
    print("=========================================================")
    print("lo",lo,"hi",hi)
    print("v",v)
    print("=========================================================")
    while i<=gt:
        print("i",i,"lt",lt,"gt",gt)
        print("before: ",lst)
        if lst[i]<v:
            lst[i],lst[lt]=lst[lt],lst[i]
            lt+=1
            i+=1
            print("lt Change!!")
        elif lst[i]>v:
            lst[i],lst[gt]=lst[gt],lst[i]
            gt-=1
            print("gt Change!!")
        else:
            i+=1
            print("just go!!")
        print("i",i,"lt",lt,"gt",gt)
        print("after: ",lst)
        print("=========================================================")
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
