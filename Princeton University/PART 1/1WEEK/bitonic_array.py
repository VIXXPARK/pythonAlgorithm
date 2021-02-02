def binary_search(lst:list,target:int):
    start=0
    end=len(lst)-1
    while start <= end:
        mid= start + (end-start)//2
        if lst[mid]>target:
            end=mid-1
        elif lst[mid]<target:
            start=mid+1
        else:
            return mid
    return -1

def binary_search2(lst:list,target:int):
    start=0
    end=len(lst)-1
    while start <= end:
        mid= start + (end-start)//2
        if lst[mid]<target:
            end=mid-1
        elif lst[mid]>target:
            start=mid+1
        else:
            return mid
    return -1

lst=[-5,-3,-2,-1,0,1,2,3,5,4,2,1,-2,-4,-6]
flag=lst.index(max(lst))
lst1=lst[:flag+1]
lst2=lst[flag+1:]
result1=binary_search(lst1,-2)
result2=binary_search2(lst2,-2)
if result1!=-1:
    print(result1)
if result2!=-1:
    print(result2+len(lst1))
