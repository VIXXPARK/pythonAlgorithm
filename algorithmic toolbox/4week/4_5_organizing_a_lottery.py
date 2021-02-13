import bisect
s,p = map(int,input().split())
segment=[]
lower=[]
upper=[]
ans=[]
for _ in range(s):
    left,right=map(int,input().split())
    segment.append([left,right])
segment.sort()
for val in segment:
    lower.append(val[0])
segment=sorted(segment,key=lambda x: x[1])
for val in segment:
    upper.append(val[1])
lst=list(map(int,input().split()))
for i in lst:
    lval=bisect.bisect_right(lower,i)
    uval=bisect.bisect_left(upper,i)
    ans.append(lval-uval)
print(' '.join(map(str,ans)))

 