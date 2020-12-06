import sys
N = int(sys.stdin.readline().rstrip())
li = list(map(int,sys.stdin.readline().split()))
findPoint=False
end=len(li)-1
for i in range(len(li)-1,0,-1):
    if li[i]<li[i-1]:
        findPoint=True
        end=i-1
        break
ans=10000
ret=len(li)-1
if findPoint:
    for j in range(len(li)-1,end,-1):
        if li[end]>li[j] and ans>(li[end]-li[j]):
            ans=(li[end]-li[j])
            ret=j
    li[end],li[ret]=li[ret],li[end]
    li=li[:end+1]+li[len(li)+1:end:-1]
    sys.stdout.write(' '.join(map(str,li))+'\n')
else:
    print(-1)
