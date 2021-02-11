ans=0
def merge(a:list,b:list):
    global ans
    c=[]
    while a and b:
        if a[0]<=b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))
            ans+=len(a)
    while a:
        c.append(a.pop(0))
    while b:
        c.append(b.pop(0))
    return c

def mergeSort(lst:list):
    if len(lst)<2:
        return lst
    mid = len(lst)//2
    l=mergeSort(lst[:mid])
    r=mergeSort(lst[mid:])
    return merge(l,r)

n=int(input())
lst=list(map(int,input().split()))
mergeSort(lst)
print(ans)

