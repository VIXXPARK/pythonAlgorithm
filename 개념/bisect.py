def upperbound(arr:list,target:int,begin=0,end=None): ## target의 값보다 큰 첫번째 값의 위치를 찾는 것
    if end is None:
        end=len(arr)
    while begin<end:
        mid=(begin+end)//2
        if arr[mid]<=target: ## target의 값과 비교해서 그 이하인 값을 찾았을 때, left 값을 움직여 target의 값보다 큰 첫 번째 값의 위치를 찾기 위해서이다.
            begin=mid+1
        else:
            end=mid
    return begin

def lowerbound(arr,value,begin=0,end=None):
    if end is None:
        end=len(arr)
    while begin<end:
        mid=(begin+end)//2
        if arr[mid]<value:
            begin=mid+1
        else:
            end=mid
    return begin

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

lst=[1,2,4,5,6,8,9,11]
# print(upperbound(lst,3))
print(lowerbound(lst,2))