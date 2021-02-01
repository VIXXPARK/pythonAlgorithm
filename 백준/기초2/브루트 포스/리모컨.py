import sys
 
def solve(sub):
    global ans
    for p in possible:
        now = sub + str(p)
        ans = min( ans, len(str(int(now))) + abs(n-int(now)) )
        if len(now) < 6:
            solve(now)
    
n = int(input())
m = int(input())
ans = abs(n-100)
 
possible = set()
if m:
    broken = set(map(int, sys.stdin.readline().split()))
    possible = set(i for i in range(10)).difference(broken)
else:
    ans = min(ans, len(str(n)))
 
solve('')
print(ans)


# 출처: https://suri78.tistory.com/150 [공부노트]