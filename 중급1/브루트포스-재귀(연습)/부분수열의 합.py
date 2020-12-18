import sys
input = sys.stdin.readline
cnt = 0
def dfs(idx, sum):
    global cnt
    if idx >= n:
        return
    sum += s_[idx]
    if sum == s:
        cnt += 1
    dfs(idx + 1, sum - s_[idx])
    dfs(idx + 1, sum)
n, s = map(int, input().split())
s_ = list(map(int, input().split()))
dfs(0, 0)
print(cnt)