n=int(input())
pair=[]
for _ in range(n):
    pair.append(list(map(int,input().split())))

pair=sorted(pair,key=lambda x: x[1])
total=len(pair)
i=0
lst=[]
while i<len(pair) and total>0:
    cnt=1
    for j in range(i+1,len(pair)):
        val=pair[j]
        if val[0]>pair[i][1]:
            break
        elif val[0]<=pair[i][1]<=val[1]:
            cnt+=1
            
    total-=cnt
    lst.append(pair[i][1])
    i+=cnt
print(len(lst))
print(' '.join(map(str,lst)))

    