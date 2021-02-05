import itertools
import time
n=2
data= ["M~C<2", "C~M>1"]	
mem = ['A','C','F','J','M','N','R','T']
pairs = list(map(list,itertools.permutations(mem,8)))
count=0
for pair in pairs: ## 한 개의 조합에 대하여 기준을 평가 하는 경우가 더 빠르다.  조합->기준
    for check in data:
        first,second,case,num=check[0],check[2],check[3],int(check[4])
        n1=pair.index(first)
        n2=pair.index(second)
        if case=='=':
            if int(abs(n1-n2))-1!=num:
                count+=1
                break
            elif int(abs(n1-n2))-1>=num:
                count+=1
                break
            elif int(abs(n1-n2))-1<=num:
                count+=1
                break



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

            

