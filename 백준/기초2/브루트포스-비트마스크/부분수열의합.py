import sys
N,S=map(int,sys.stdin.readline().rstrip().split())
li = list(map(int,sys.stdin.readline().split()))
passing=[False]*(N+1)
ans=[]
cnt=0
def func(ans,celi,aim,sum):
    global cnt,S
    if celi==aim:
        return
    for i in range(N):
        if not ans:
            passing[i]=True
            ans.append(i)
            sum+=li[i]
            if li[i]==S:
                cnt+=1
            func(ans,celi+1,aim,sum)
            sum-=li[i]
            ans.pop()
            passing[i]=False
        else:
            if not passing[i] and ans[-1]<i:
                passing[i]=True
                ans.append(i)
                sum+=li[i]
                if sum==S:
                    cnt+=1
                func(ans,celi+1,aim,sum)
                sum-=li[i]
                ans.pop()
                passing[i]=False
func(ans,0,N,0)
print(cnt)


# import sys
# input = sys.stdin.readline
# def dfs(idx, sum):
#     global cnt
#     if idx >= n:
#         return
#     sum += s_[idx]
#     if sum == s:
#         cnt += 1
#     dfs(idx + 1, sum - s_[idx])
#     dfs(idx + 1, sum)
# n, s = map(int, input().split())
# s_ = list(map(int, input().split()))
# cnt = 0
# dfs(0, 0)
# print(cnt)

#https://pacific-ocean.tistory.com/306

