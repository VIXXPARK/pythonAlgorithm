def insertSort(x):
    for i in range(1,len(x)):
        j=i-1
        key=x[i]
        while x[j]<key and j>=0: # 현재 j 위치의 값보다 클 때까지
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=key
    return x

lst=[3,5,7,6,4,2,1,9]
print(insertSort(lst))
