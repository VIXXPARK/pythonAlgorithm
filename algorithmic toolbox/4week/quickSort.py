def quickSort(a:list,left=0,right=None):
    if right is None:
        right=len(a)-1
    if left>=right:
        return
    m=partition(a,left,right)
    quickSort(a,left,m-1)
    quickSort(a,m+1,right)


def partition(a:list,left,right):
    x=a[left]
    j=left
    for i in range(left+1,right+1):
        if a[i]<=x:
            j+=1
            a[j],a[i]=a[i],a[j]
    a[left],a[j]=a[j],a[left]
    return j

lst=[7,5,2,3,4,1,9]
quickSort(lst)
print(lst)