def upperbound(arr:list,target:int)->int: ## target의 값보다 큰 첫번째 값의 위치를 찾는 것
    left,right=0,len(arr)-1
    while left<right:
        mid=(left+right)//2
        if arr[mid]<=target: ## target의 값과 비교해서 그 이하인 값을 찾았을 때, left 값을 움직여 target의 값보다 큰 첫 번째 값의 위치를 찾기 위해서이다.
            left=mid+1
        else:
            right=mid
    return right

def lowerbound(arr:list,target:int)->int: ## target의 값보다 크거나 같은 값의 위치를 찾는 것이다.
    left,right=0,len(arr)-1
    while left<right:
        mid=(left+right)//2
        if arr[mid]<target:## target 값보다 작은 값을 찾았을 때, left 값을 움직여 target의 값보다 크거나 같은 첫번째 값의 위치를 찾기 위해서이다.
            left=mid+1
        else:
            right=mid
    return right

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

lst=[1,3,5,7,9,14,17,21]
print(upperbound(lst,1))
print(lowerbound(lst,1))