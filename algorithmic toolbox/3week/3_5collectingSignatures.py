n=int(input())
pair=[]
for _ in range(n):
    pair.append(list(map(int,input().split())))

pair=sorted(pair,key=lambda x: x[1]) # 우측 기준으로 오름차순 정렬
total=len(pair) 
i=0
lst=[]
while i<len(pair) and total>0:
    cnt=1
    for j in range(i+1,len(pair)):
        val=pair[j]
        if val[0]>pair[i][1]: # 반복문 돌고 있는 값의 좌측 부분이 현재 값의 우측 보다
            break             # 크면 멈춘다
        elif val[0]<=pair[i][1]<=val[1]:
            cnt+=1
            
    total-=cnt # 해당 갯수만큼 총 갯수에서 제외
    lst.append(pair[i][1]) # 해당 값 저장
    i+=cnt
print(len(lst))
print(' '.join(map(str,lst)))

    