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
            if passing[li[i]]<check[li[i]]:
                passing[li[i]]+=1
                ans.append(str(li[i]))
                func(celi+1)
                passing[li[i]]-=1
                ans.pop()

func(0)


# from itertools import permutations

# N, M = map(int, input().split())
# N_list = list(map(int, input().split()))
# N_list = sorted(N_list) #순서대로 나오게 정렬 먼저

# output = []
# for numbers in list(permutations(N_list, M)):
#     output.append(numbers)
# output = sorted(list(set(output))) #중복 제거 후 정렬 까지 한번에!

# for numbers in output:
#     for num in numbers:
#         print(num, end=' ')
#     print()
# # https://claude-u.tistory.com/311


# n, m = map(int, input().split())
# num_list = list(map(int, input().split()))
# num_list.sort()

# a = [0 for i in range(m)]
# c = [False for i in range(n)]
# ans = []

# def go(idx, n, m):
#     if idx == m:
#         ans.append(a.copy())
#         return
#     for i in range(n):
#         if c[i] == False:
#             c[i] = True
#             a[idx] = num_list[i]
#             go(idx + 1, n, m)
#             c[i] = False

# go(0, n, m)
# ans.sort()
# print(' '.join(map(str, ans[0])))
# for i in range(1, len(ans)):
#     if ans[i - 1] != ans[i]:
#         print(' '.join(map(str, ans[i])))

# # https://hjp845.tistory.com/85