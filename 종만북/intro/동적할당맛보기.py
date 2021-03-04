MIN=-987654321
def maxSum(lst):
    N=len(lst)
    ret=MIN
    psum=0
    for i in range(N):
        psum=max(psum,0)+lst[i]
        ret=max(psum,ret)
    return ret