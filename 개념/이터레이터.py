import itertools
x=itertools.count(10,2)
# for i in x:
#     if i<20:
#         print(i)
#     else:
#         break
cyc='ABCDE'
# cnt=0
# for c in itertools.cycle(cyc):
#     if cnt<20:
#         print(c,end=' ')
#     else:
#         break
#     cnt+=1

for i in itertools.repeat(10,3):
    # print(i)
    pass

for i in itertools.accumulate([1,2,3,4,5]):
    # print(i) >> 1,3,6,10,15
    pass

x=list(itertools.chain('ABC','FGZ')) # ['A','B','C','F','G','Z']
# print(x)

x =(itertools.chain.from_iterable(['FGZ','ABC'])) #--> F G Z A B C

x=itertools.compress(['a','b','c','d','e','f'],[1,0,0,1,1,1]) # A D E F
# print(list(x))

for val in itertools.product(['a','b','c'],['!','%','^']): ## sql문에서 join과 비슷한 함수
    print(val)
    pass

for val in itertools.permutations(['a','b','c'],3): # 순열
    # print(val)
    pass

for val in itertools.combinations(['a','b','c'],3): #조합 반복되는 요소 없음
    # print(val)
    pass

for val in itertools.combinations_with_replacement(['a','b','c'],3): #조합 반복되는 요소 있음
    # print(val)
    pass
lst=list(itertools.islice('ABCDEFG',2,None)) #['C', 'D', 'E', 'F', 'G']
lst=list(itertools.islice('ABCDEFG',2,5)) #['C', 'D', 'E']
# print(lst)
s='ABCDEFG'
# print(list(s[2:5]))  #['C', 'D', 'E']
