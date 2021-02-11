lst=list(map(int,input().split()))
del lst[0]
find=list(map(int,input().split()))
del find[0]
def binary_search(arr:list,target:int)->int:
    lo,hi=0,len(arr)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid]<target:
            lo=mid+1
        elif arr[mid]>target:
            hi=mid-1
        else:
            return mid
    return -1
for val in find:
    print(binary_search(lst,val),end=" ")
