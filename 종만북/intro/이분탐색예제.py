def canCover(x):
    pass

def minRadiusCover():
    minRadius = 0
    maxRadius = 10
    while maxRadius-minRadius>1e-10:
        mid = (minRadius+maxRadius)/2
        if canCover(mid):
            maxRadius=mid
        else:
            minRadius=mid
    return maxRadius

def binary_search(lst,target):
    left,right=0,len(lst)-1
    while left<=right:
        mid=(left+right)//2
        if lst[mid]<target:
            left=mid+1
        elif lst[mid]>target:
            right=mid-1
        else:
            return mid
    return left

lst=[1,2,5,7,9,11,15,75,95]
