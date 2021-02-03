dic={1:2,
    2:4,
    3:1,
    5:7,
    6:10,
    15:9,
    13:6}
print(sorted(dic,key=lambda x:dic[x],reverse=False)) # key 값 오름차순 정렬
print(sorted(dic,key=lambda x:dic[x],reverse=True)) # key 값 내림차순 정렬