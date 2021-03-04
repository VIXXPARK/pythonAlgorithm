MIN = -987654321
def maxSum(lst,lo,hi):
    if lo==hi:
        return lst[lo]
    mid = (lo+hi)//2
    left,right= MIN,MIN
    total=0
    for i in range(mid,lo-1,-1):
        total+=lst[i]
        left=max(left,total)
    total=0
    for i in range(mid+1,hi+1):
        total+=lst[i]
        right=max(right,total)
    single = max(maxSum(lst,lo,mid),maxSum(lst,mid+1,hi))

    return max(left+right,single)
