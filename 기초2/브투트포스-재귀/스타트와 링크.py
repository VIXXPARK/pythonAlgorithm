import sys
N=int(sys.stdin.readline())
ar=[]
passing=[False]*(N)
for _ in range(N):
    ar.append(list(map(int,sys.stdin.readline().split())))
li = [int(i) for i in range(N)]
ret=10e9
def func(ans,celi,aim):
    global li
    global passing
    global ret
    if celi==aim:
        val1=0
        val2=0
        link = set(li)
        link=link.difference(set(ans))
        for x in ans:
            for y in ans:
                if x!=y:
                    val1+=ar[x][y]
        for a in link:
            for b in link:
                if a!=b:
                    val2+=ar[a][b]
        ret=min(ret,abs(val1-val2))
        return
    for i in range(1,len(li)):
        if not passing[i] and ans[-1]<li[i]:
            passing[i]=True
            ans.append(i)
            func(ans,celi+1,aim)
            ans.pop()
            passing[i]=False
ans=[0]
passing[0]=True
func(ans,0,N//2-1)
print(ret)


# N = int(input())
# table = []
# for i in range(N):
#     table.append(list(map(int,input().split())))
# min_differ = 10000000

# def recursive(iteration, a_num, b_num, a_stat, b_stat, a_set, b_set):
#     global table
#     global min_differ
#     global N
#     if((a_num + b_num) == N):
#         differ = abs(a_stat - b_stat)
#         if(min_differ > differ):
#             min_differ = differ
#         return
    
#     if(a_num < int(N/2)):
#         new_stat = 0
#         for i in a_set:
#             new_stat += (table[iteration][i] + table[i][iteration])
#         a_set.append(iteration)
#         recursive(iteration + 1, a_num + 1, b_num, a_stat + new_stat, b_stat, a_set, b_set)
#         a_set.pop()
        
#     if(b_num < int(N/2)):
#         new_stat = 0
#         for i in b_set:
#             new_stat += (table[iteration][i] + table[i][iteration])
#         b_set.append(iteration)
#         recursive(iteration + 1, a_num, b_num + 1, a_stat, b_stat + new_stat, a_set, b_set) 
#         b_set.pop()

# recursive(0, 0, 0, 0, 0, [], [])
# print(min_differ)