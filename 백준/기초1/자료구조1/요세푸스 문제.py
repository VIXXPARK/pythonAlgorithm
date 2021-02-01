import sys
from collections import deque
a,b = map(int,sys.stdin.readline().split())
q = deque(range(1,a+1))
ans = []
while(len(q)!=0):
    for _ in range(b-1):
        val=q.popleft()
        q.append(val)
    ans.append(q.popleft())
print('<',end='')
ans = list(map(str,ans))
print(', '.join(ans),end='')
print('>')
 ## 순환에 관련된 문제는 큐로 푸는 것이 편하다.


