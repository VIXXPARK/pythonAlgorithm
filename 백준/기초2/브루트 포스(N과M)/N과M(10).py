import sys
N,M = map(int,sys.stdin.readline().split())
li=[int(i) for i in sys.stdin.readline().split()]
check=[0]*10001
passing=[0]*10001
init=[False]*10001
for i in li:
    check[i]+=1
dic = set(li)
li=list(dic)
li.sort()
ans=[]

def func(celi):
    if celi==M:
        print(' '.join(ans))
        return
    for i in range(len(li)):
        if not ans:
            if init[li[i]]!=True:
                init[li[i]]=True
                passing[li[i]]=1
                ans.append(str(li[i]))
                func(celi+1)
                passing[li[i]]=0
                ans.pop()
        else:
            if passing[li[i]]<check[li[i]] and int(ans[-1])<=li[i]:
                passing[li[i]]+=1
                ans.append(str(li[i]))
                func(celi+1)
                passing[li[i]]-=1
                ans.pop()

func(0)


# from itertools import combinations

# N, M = map(int, input().split())
# N_list = list(map(int, input().split()))
# N_list = sorted(N_list) #순서대로 나오게 정렬 먼저
# output = [] #중복 제거하기 위한 리스트 생성

# for numbers in list(combinations(N_list, M)):
#     if not output:
#         output.append(numbers)
#     elif numbers not in output: # 중복 제거
#         output.append(numbers)
            
# for numbers in output:
#     for num in numbers:
#         print(num, end=' ')
#     print()

# #https://claude-u.tistory.com/308