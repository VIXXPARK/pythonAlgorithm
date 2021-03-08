import itertools
import time
n=2
data= ["N~F=0", "R~T>2"]
mem = ['A','C','F','J','M','N','R','T']
pairs = list(map(list,itertools.permutations(mem,8)))
count=0
for idx,pair in enumerate(pairs): ## 한 개의 조합에 대하여 기준을 평가 하는 경우가 더 빠르다.  조합->기준
    for check in data:
        first,second,case,num=check[0],check[2],check[3],int(check[4])
        n1=pair.index(first)
        n2=pair.index(second)
        flag=False
        if pair!=[]:
            if case=='=':
                if abs(n1-n2)-1!=num:
                    flag=True
            elif case=='>':
                if abs(n1-n2)-1<=num:
                    flag=True
            else:
                if abs(n1-n2)-1>=num:
                    flag=True
            if flag:
                count+=1
                break
print(40320-count)



# start=time.time()

# for check in data: # 기준->조합
#     first,second,case,num=check[0],check[2],check[3],int(check[4])
#     for ods,pair in enumerate(pairs):
#         n1,n2=-1,-1
#         if len(pair)!=0:
#             n1=pair.index(first)
#             n2=pair.index(second)
#             if case=='=':
#                 if int(abs(n1-n2))-1!=num:
#                     pairs[ods]=[]
#                     count+=1
#             elif case=='<':
#                 if int(abs(n1-n2))-1>=num:
#                     pairs[ods]=[]
#                     count+=1
#             elif case=='>':
#                 if int(abs(n1-n2))-1<=num:
#                     pairs[ods]=[]
#                     count+=1
# end=time.time()-start

            

