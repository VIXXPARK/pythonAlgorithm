def quicksort(lst:list,lo=0,hi=None):
    if hi is None:
        hi=len(lst)-1
    if lo>=hi:
        return
    lt,i=lo,lo
    gt=hi
    pivot=lst[lo]
    while i<=gt:
        if lst[i]<pivot:
            lst[i],lst[lt]=lst[lt],lst[i]
            lt+=1
            i+=1
        elif lst[i]>pivot:
            lst[i],lst[gt]=lst[gt],lst[i]
            gt-=1
        else:
            i+=1
    quicksort(lst,lo,lt-1)
    quicksort(lst,gt+1,hi)

n=int(input())
lst=list(map(int,input().split()))
quicksort(lst)
print(' '.join(map(str,lst)))
    

    